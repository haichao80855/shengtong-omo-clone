# 盛通教育 OMO 管理系统高精度复刻

目标：[一校平台](https://manage.shengtongedu.cn/#/choose)。范围：首页、教研、学员、教务，以及系统模块中的「机构管理」。

当前阶段为**取证与工程启动**，尚无业务实现或经验证的原系统黄金基线。候选流程须经证据确认，不能从工单标题认定原系统具有某项功能。

## 工作入口

- [版本化规格](SPEC.md)
- [GitHub Issues](https://github.com/haichao80855/shengtong-omo-clone/issues)
- [总规格 #8](https://github.com/haichao80855/shengtong-omo-clone/issues/8)
- [任务图与起步顺序](docs/planning/issue-map.md)
- [Matt 工作流与状态](docs/agents/issue-tracker.md)
- [证据规范](docs/evidence/README.md)、[页面覆盖表](docs/evidence/page-map.md)、[规则台账](docs/evidence/rule-ledger.md)
- [术语](GLOSSARY.md)、[取证与范围决策](docs/decisions/001-evidence-and-scope.md)

按「取证 → 澄清与规格 → 窄切片 → 实施、测试和 review → 验收」推进。仅领取 ready-for-agent 且所有前置条件满足的任务；父工单汇总。未知规则不能由智能体按行业经验补全。

当前可开始：[最小工程 #1](https://github.com/haichao80855/shengtong-omo-clone/issues/1) 与[访问和采集验证 #9](https://github.com/haichao80855/shengtong-omo-clone/issues/9)。

## 实现方向

保留 pnpm、Vue 3/Vite/TypeScript/Element Plus、NestJS/Prisma/PostgreSQL 与共享契约方向，模型和接口随证据增加。Playwright 为主工具，HAR/运行时/AST 按需使用，REA 的具体工具和必要性待确认。

## 规划修订

原七张工单保留编号，#1 缩小为最小工程，#2–#7 转为父工单。新增取证与待取证实施任务，采用原生父子/阻塞关系。旧规格及工单保留在 docs/planning/history，便于查证，不作为已验证业务规格。
