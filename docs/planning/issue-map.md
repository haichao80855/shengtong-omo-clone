# 工单地图与实施顺序

修订日期：2026-10-10。此表记录本次规划修复初始状态；后续推进须同步更新任务图，并以 GitHub 当前状态为准。

总规格：[#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8)。共 43 张工单：1 张总规格、6 张模块父工单、8 张取证任务、27 张实施任务（含最小工程）、1 张终验。

## 当前起步

1. [#1](https://github.com/haichao80855/shengtong-omo-clone/issues/1) 最小全栈工程；无业务取证前置。
2. [#9](https://github.com/haichao80855/shengtong-omo-clone/issues/9) 访问、测试环境与工具可行性；明确访问缺口和操作边界。
3. 访问条件成立后推进 [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10) 页面地图与 [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) 采集管线。
4. 按模块取证，将具体证据/预期填入子工单并校准粒度和依赖；证据不足的实施候选保持阻塞。
5. 先会话授权和全局导航，再按就绪节点推进业务切片。看板和 AST 不阻塞所有模块。

仅 #1、#9 带 ready-for-agent；父工单不能作为一个巨大任务领取。其他实施工单有 needs-evidence，不允许按假设编码。

## 模块与任务

| 工单 | 类型 | 内容 | 父工单 | 阻塞工单 |
| --- | --- | --- | --- | --- |
| [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | spec | 总规格：五个范围的证据驱动高精度复刻 | — | 无 |
| [#1](https://github.com/haichao80855/shengtong-omo-clone/issues/1) | implementation | 01：最小全栈工程与真实服务健康链路 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#2](https://github.com/haichao80855/shengtong-omo-clone/issues/2) | epic | 02：父工单／首页、入口与全局导航 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#3](https://github.com/haichao80855/shengtong-omo-clone/issues/3) | epic | 03：父工单／系统中的机构管理 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | epic | 04：父工单／教研模块 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | epic | 05：父工单／学员模块 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | epic | 06：父工单／教务产品、班级与排课 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#7](https://github.com/haichao80855/shengtong-omo-clone/issues/7) | epic | 07：父工单／报名、教学服务与课消评价 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#9](https://github.com/haichao80855/shengtong-omo-clone/issues/9) | discovery | 取证：访问条件、测试环境与采集工具可行性 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | 无 |
| [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10) | discovery | 取证：五个范围的完整页面与权限入口地图 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | [#9](https://github.com/haichao80855/shengtong-omo-clone/issues/9) |
| [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) | discovery | 取证工具：可复现采集、脱敏与视觉基线管线 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | [#9](https://github.com/haichao80855/shengtong-omo-clone/issues/9) |
| [#12](https://github.com/haichao80855/shengtong-omo-clone/issues/12) | discovery | 取证：首页、会话、上下文、导航与指标 | [#2](https://github.com/haichao80855/shengtong-omo-clone/issues/2) | [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10), [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) |
| [#13](https://github.com/haichao80855/shengtong-omo-clone/issues/13) | discovery | 取证：机构管理层级、字段、权限与资源归属 | [#3](https://github.com/haichao80855/shengtong-omo-clone/issues/3) | [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10), [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) |
| [#14](https://github.com/haichao80855/shengtong-omo-clone/issues/14) | discovery | 取证：教研全部页面、课程与素材文件行为 | [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10), [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) |
| [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) | discovery | 取证：学员档案、导入、账户与各类异动 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10), [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) |
| [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) | discovery | 取证：产品、班级、排课、报名与教学服务 | [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | [#10](https://github.com/haichao80855/shengtong-omo-clone/issues/10), [#11](https://github.com/haichao80855/shengtong-omo-clone/issues/11) |
| [#17](https://github.com/haichao80855/shengtong-omo-clone/issues/17) | implementation | 切片：会话、组织校区上下文与服务端授权 | [#2](https://github.com/haichao80855/shengtong-omo-clone/issues/2) | [#1](https://github.com/haichao80855/shengtong-omo-clone/issues/1), [#12](https://github.com/haichao80855/shengtong-omo-clone/issues/12) |
| [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18) | implementation | 切片：入口选择与全局导航 | [#2](https://github.com/haichao80855/shengtong-omo-clone/issues/2) | [#17](https://github.com/haichao80855/shengtong-omo-clone/issues/17), [#12](https://github.com/haichao80855/shengtong-omo-clone/issues/12) |
| [#19](https://github.com/haichao80855/shengtong-omo-clone/issues/19) | implementation | 切片：首页内容与已验证看板口径 | [#2](https://github.com/haichao80855/shengtong-omo-clone/issues/2) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#12](https://github.com/haichao80855/shengtong-omo-clone/issues/12) |
| [#20](https://github.com/haichao80855/shengtong-omo-clone/issues/20) | implementation | 切片：机构资料查看与保存 | [#3](https://github.com/haichao80855/shengtong-omo-clone/issues/3) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#13](https://github.com/haichao80855/shengtong-omo-clone/issues/13) |
| [#21](https://github.com/haichao80855/shengtong-omo-clone/issues/21) | implementation | 候选切片：机构管理中的场地或教室维护 | [#3](https://github.com/haichao80855/shengtong-omo-clone/issues/3) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#13](https://github.com/haichao80855/shengtong-omo-clone/issues/13) |
| [#22](https://github.com/haichao80855/shengtong-omo-clone/issues/22) | implementation | 切片：教研课程浏览、检索与详情 | [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#14](https://github.com/haichao80855/shengtong-omo-clone/issues/14) |
| [#23](https://github.com/haichao80855/shengtong-omo-clone/issues/23) | implementation | 切片：教研课程表单与保存 | [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | [#22](https://github.com/haichao80855/shengtong-omo-clone/issues/22), [#14](https://github.com/haichao80855/shengtong-omo-clone/issues/14) |
| [#24](https://github.com/haichao80855/shengtong-omo-clone/issues/24) | implementation | 切片：教研素材列表与详情 | [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#14](https://github.com/haichao80855/shengtong-omo-clone/issues/14) |
| [#25](https://github.com/haichao80855/shengtong-omo-clone/issues/25) | implementation | 切片：教研素材上传与下载结果 | [#4](https://github.com/haichao80855/shengtong-omo-clone/issues/4) | [#24](https://github.com/haichao80855/shengtong-omo-clone/issues/24), [#14](https://github.com/haichao80855/shengtong-omo-clone/issues/14) |
| [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26) | implementation | 切片：学员列表、检索与档案详情 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#27](https://github.com/haichao80855/shengtong-omo-clone/issues/27) | implementation | 切片：新增学员与验证失败 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#28](https://github.com/haichao80855/shengtong-omo-clone/issues/28) | implementation | 切片：编辑学员与资料回显 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#29](https://github.com/haichao80855/shengtong-omo-clone/issues/29) | implementation | 候选切片：学员删除与引用约束 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#30](https://github.com/haichao80855/shengtong-omo-clone/issues/30) | implementation | 切片：学员模板导入与错误结果 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#27](https://github.com/haichao80855/shengtong-omo-clone/issues/27), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#31](https://github.com/haichao80855/shengtong-omo-clone/issues/31) | implementation | 切片：学员账户与流水查询 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15) |
| [#32](https://github.com/haichao80855/shengtong-omo-clone/issues/32) | implementation | 切片：教务售卖产品与表单保存 | [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | [#18](https://github.com/haichao80855/shengtong-omo-clone/issues/18), [#22](https://github.com/haichao80855/shengtong-omo-clone/issues/22), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#33](https://github.com/haichao80855/shengtong-omo-clone/issues/33) | implementation | 切片：班级创建、列表与详情 | [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | [#32](https://github.com/haichao80855/shengtong-omo-clone/issues/32), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#34](https://github.com/haichao80855/shengtong-omo-clone/issues/34) | implementation | 切片：学员报名、合同与支付登记 | [#7](https://github.com/haichao80855/shengtong-omo-clone/issues/7) | [#26](https://github.com/haichao80855/shengtong-omo-clone/issues/26), [#32](https://github.com/haichao80855/shengtong-omo-clone/issues/32), [#31](https://github.com/haichao80855/shengtong-omo-clone/issues/31), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#35](https://github.com/haichao80855/shengtong-omo-clone/issues/35) | implementation | 切片：学员入班与班级成员结果 | [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | [#33](https://github.com/haichao80855/shengtong-omo-clone/issues/33), [#34](https://github.com/haichao80855/shengtong-omo-clone/issues/34), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#36](https://github.com/haichao80855/shengtong-omo-clone/issues/36) | implementation | 切片：课次排定、资源选择与冲突结果 | [#6](https://github.com/haichao80855/shengtong-omo-clone/issues/6) | [#33](https://github.com/haichao80855/shengtong-omo-clone/issues/33), [#13](https://github.com/haichao80855/shengtong-omo-clone/issues/13), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#37](https://github.com/haichao80855/shengtong-omo-clone/issues/37) | implementation | 切片：课次点名与考勤结果 | [#7](https://github.com/haichao80855/shengtong-omo-clone/issues/7) | [#36](https://github.com/haichao80855/shengtong-omo-clone/issues/36), [#35](https://github.com/haichao80855/shengtong-omo-clone/issues/35), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#38](https://github.com/haichao80855/shengtong-omo-clone/issues/38) | implementation | 切片：课消、重复操作与实际撤销规则 | [#7](https://github.com/haichao80855/shengtong-omo-clone/issues/7) | [#37](https://github.com/haichao80855/shengtong-omo-clone/issues/37), [#34](https://github.com/haichao80855/shengtong-omo-clone/issues/34), [#31](https://github.com/haichao80855/shengtong-omo-clone/issues/31), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#39](https://github.com/haichao80855/shengtong-omo-clone/issues/39) | implementation | 切片：课后评价与回显 | [#7](https://github.com/haichao80855/shengtong-omo-clone/issues/7) | [#37](https://github.com/haichao80855/shengtong-omo-clone/issues/37), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#40](https://github.com/haichao80855/shengtong-omo-clone/issues/40) | implementation | 切片：学员转班与关系变更 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#35](https://github.com/haichao80855/shengtong-omo-clone/issues/35), [#38](https://github.com/haichao80855/shengtong-omo-clone/issues/38), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#41](https://github.com/haichao80855/shengtong-omo-clone/issues/41) | implementation | 切片：休学与复学状态往返 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#34](https://github.com/haichao80855/shengtong-omo-clone/issues/34), [#35](https://github.com/haichao80855/shengtong-omo-clone/issues/35), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#42](https://github.com/haichao80855/shengtong-omo-clone/issues/42) | implementation | 切片：退费办理与账务结果 | [#5](https://github.com/haichao80855/shengtong-omo-clone/issues/5) | [#34](https://github.com/haichao80855/shengtong-omo-clone/issues/34), [#38](https://github.com/haichao80855/shengtong-omo-clone/issues/38), [#31](https://github.com/haichao80855/shengtong-omo-clone/issues/31), [#15](https://github.com/haichao80855/shengtong-omo-clone/issues/15), [#16](https://github.com/haichao80855/shengtong-omo-clone/issues/16) |
| [#43](https://github.com/haichao80855/shengtong-omo-clone/issues/43) | verification | 终验：全范围页面、权限与跨模块业务差分 | [#8](https://github.com/haichao80855/shengtong-omo-clone/issues/8) | [#19](https://github.com/haichao80855/shengtong-omo-clone/issues/19), [#20](https://github.com/haichao80855/shengtong-omo-clone/issues/20), [#21](https://github.com/haichao80855/shengtong-omo-clone/issues/21), [#23](https://github.com/haichao80855/shengtong-omo-clone/issues/23), [#25](https://github.com/haichao80855/shengtong-omo-clone/issues/25), [#27](https://github.com/haichao80855/shengtong-omo-clone/issues/27), [#28](https://github.com/haichao80855/shengtong-omo-clone/issues/28), [#29](https://github.com/haichao80855/shengtong-omo-clone/issues/29), [#30](https://github.com/haichao80855/shengtong-omo-clone/issues/30), [#31](https://github.com/haichao80855/shengtong-omo-clone/issues/31), [#35](https://github.com/haichao80855/shengtong-omo-clone/issues/35), [#36](https://github.com/haichao80855/shengtong-omo-clone/issues/36), [#38](https://github.com/haichao80855/shengtong-omo-clone/issues/38), [#39](https://github.com/haichao80855/shengtong-omo-clone/issues/39), [#40](https://github.com/haichao80855/shengtong-omo-clone/issues/40), [#41](https://github.com/haichao80855/shengtong-omo-clone/issues/41), [#42](https://github.com/haichao80855/shengtong-omo-clone/issues/42) |

## 取证后必须校准的边

- 产品与教研关系、报名是否必须指定班级，按证据删增依赖，不能保留不真实的阻塞。
- 模块证据任务过大时，按实际页面/流程拆取证子任务，实施依赖转向必要的子任务，避免等待整个模块取证完成。
- 机构管理中的场地/教室归属未确定；可能移动父工单、缩小范围或记录不适用。
- 点名与课消若为不可分割事务，先合并 #37/#38 并重建关系，不能发布部分成功链路。
- 评价若要求已课消，补 #38 前置；退费/转班/休复学若有多页审批，先拆审批切片。
- 钱包写入、学员导出及任何新增发现的范围内页面，补独立任务并加入对应父工单和终验依赖。
- 账号不足造成不可见的页面保持未知；候选工单关闭或不适用时记录依据，不以此偷偷缩小用户范围。

## 关系校验

[机器可读任务图](issue-map.json) 保存来源、未知问题、验收项与关系。下列命令为只读验证：

```sh
python3 tools/check_issue_plan.py
python3 tools/check_issue_plan.py --remote
```

检查重复/缺失节点、依赖/父子/完成循环、标签条件，以及 GitHub 正文和原生关系的一致性。这是规划修复快照校验；推进工单后应同时更新快照，不能将已完成任务仍写为初始开放状态。

推进时在任务图更新 state、evidence_status、evidence_ids 与标签，保留已完成的真实阻塞边；ready-for-agent 可以依赖已关闭任务，但不能依赖仍开放的任务。默认省略字段表示 open / pending。

历史规格及原工单见 [history](history)。它们供追溯，不是已验证的业务证据。
