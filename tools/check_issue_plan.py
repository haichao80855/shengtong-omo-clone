#!/usr/bin/env python3
"""Validate the versioned issue graph; --remote also checks GitHub without writing."""
import argparse
import concurrent.futures
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def load_plan():
    return json.loads((ROOT / "docs/planning/issue-map.json").read_text())


def validate_local(plan):
    tasks = plan["tasks"]
    keyed = {t["key"]: t for t in tasks}
    assert len(keyed) == len(tasks), "Duplicate task key"
    numbers = [t["number"] for t in tasks]
    assert all(isinstance(n, int) and n > 0 for n in numbers), "Unpublished issue"
    assert len(set(numbers)) == len(numbers), "Duplicate issue number"
    for t in tasks:
        assert t["acceptance"] and t["what"], t["key"] + ": incomplete ticket"
        assert t["parent"] is None or t["parent"] in keyed, "Missing parent"
        assert len(t["blocked_by"]) == len(set(t["blocked_by"])), "Duplicate blocker"
        assert all(k in keyed and k != t["key"] for k in t["blocked_by"]), "Invalid blocker"
        if "ready-for-agent" in t["labels"]:
            assert all(keyed[k].get("state", "open") == "closed" for k in t["blocked_by"]), "Ready issue has open blockers"
            assert "needs-evidence" not in t["labels"], "Ready issue lacks evidence"
            assert t["kind"] not in ("spec", "epic"), "Tracking issue marked ready"
            assert t.get("state", "open") == "open", "Closed issue marked ready"
            if t["kind"] == "implementation" and t["key"] != "boot":
                assert t.get("evidence_status") in ("verified", "accepted-deviation") and t.get("evidence_ids"), "Ready implementation lacks evidence references"
        if t["kind"] == "implementation" and t["key"] != "boot" and t.get("state", "open") == "open" and t.get("evidence_status", "pending") == "pending":
            assert "needs-evidence" in t["labels"], "Initial candidate lacks evidence gate"
            assert t["rules"] and t["unknowns"], "Candidate lacks explicit unknowns"

    def check_graph(edges, label):
        done = set()
        def visit(key, stack):
            assert key not in stack, label + " cycle: " + " -> ".join(stack + [key])
            if key in done:
                return
            for dep in edges(key):
                visit(dep, stack + [key])
            done.add(key)
        for key in keyed:
            visit(key, [])

    check_graph(lambda k: keyed[k]["blocked_by"], "Dependency")
    check_graph(lambda k: [keyed[k]["parent"]] if keyed[k]["parent"] else [], "Parent")
    # Parent completion and blocker completion must not form a mixed deadlock.
    check_graph(
        lambda k: keyed[k]["blocked_by"] + [t["key"] for t in tasks if t["parent"] == k],
        "Completion",
    )
    return keyed


def gh_json(path):
    p = subprocess.run(
        ["gh", "api", path, "-H", "Accept: application/vnd.github+json"],
        capture_output=True, text=True,
    )
    if p.returncode:
        raise RuntimeError(path + ": " + p.stderr.strip())
    return json.loads(p.stdout)


def validate_remote(plan, keyed):
    base = "repos/" + plan["repository"]
    pages = []
    page = 1
    while True:
        items = gh_json(base + "/issues?state=all&per_page=100&page=" + str(page))
        pages.extend(i for i in items if "pull_request" not in i)
        if len(items) < 100:
            break
        page += 1
    actual = {i["number"]: i for i in pages}
    for t in plan["tasks"]:
        issue = actual[t["number"]]
        assert issue["id"] == t["github_id"], "Wrong GitHub id"
        assert issue["title"] == t["title"], "Title differs: #" + str(t["number"])
        assert issue["state"] == t.get("state", "open"), "Issue state differs"
        assert {x["name"] for x in issue["labels"]} == set(t["labels"]), "Labels differ"
        marker = "<!-- shengtong-plan:2026-10-10:" + t["key"] + " -->"
        assert marker in issue["body"], "Missing plan marker"
        assert t["what"] in issue["body"], "Description differs"
        assert all("- [ ] " + a in issue["body"] or "- [x] " + a in issue["body"] for a in t["acceptance"]), "Acceptance criteria differ"
        if t["key"] != "spec":
            assert "#" + str(keyed["spec"]["number"]) in issue["body"], "No source spec"
        if t["parent"]:
            assert "## Parent\n\n#" + str(keyed[t["parent"]]["number"]) in issue["body"], "Body parent differs"
        if t["key"] == "spec":
            snapshot = issue["body"].split("## Versioned specification snapshot\n\n", 1)[1].strip()
            assert snapshot == (ROOT / "SPEC.md").read_text().strip(), "Master spec snapshot differs"

    def check_native(t):
        path = base + "/issues/" + str(t["number"])
        blocked = gh_json(path + "/dependencies/blocked_by?per_page=100")
        expected = {keyed[k]["number"] for k in t["blocked_by"]}
        assert {x["number"] for x in blocked} == expected, "Native blockers differ: #" + str(t["number"])
        issue_body = actual[t["number"]]["body"]
        section = issue_body.split("## Blocked by\n\n", 1)[1].split("\n\n", 1)[0]
        expected_body = "\n".join("- #" + str(keyed[k]["number"]) for k in t["blocked_by"]) or "None"
        assert section == expected_body, "Body blockers differ: #" + str(t["number"])
        if t["parent"]:
            parent = gh_json(path + "/parent")
            assert parent["number"] == keyed[t["parent"]]["number"], "Native parent differs"
        return t["number"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        checked = list(pool.map(check_native, plan["tasks"]))
    return len(checked)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", action="store_true", help="Read GitHub titles, labels and native relations")
    args = parser.parse_args()
    plan = load_plan()
    keyed = validate_local(plan)
    count = len(plan["tasks"])
    edges = sum(len(t["blocked_by"]) for t in plan["tasks"])
    parents = sum(t["parent"] is not None for t in plan["tasks"])
    print(f"Local OK: {count} issues, {edges} blockers, {parents} parent links")
    if args.remote:
        checked = validate_remote(plan, keyed)
        print(f"GitHub OK: {checked} issues; titles, source spec, labels, bodies and native relations match")


if __name__ == "__main__":
    main()
