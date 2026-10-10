# 01: 全栈 Monorepo 基础工程骨架与离线逆向契约套件

**What to build:** 建立整个复刻工程的基础工作区与离线分析管线。从开发者和自动化测试视角，构建一个统一构建、前后端共享类型契约的开发大仓环境，能够自动解析目标前端静态 Bundle 提取接口结构与校验规则，并具备执行离线 Playwright 黑盒测试的环境基础。

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] 初始化基于 pnpm 的 Monorepo 仓储架构，组织前端应用、后端服务、共享契约包与离线逆向测试工具包
- [ ] 共享契约包沉淀基础 OpenAPI 契约与系统规格定义原型，前后端可共享 TypeScript 类型
- [ ] 逆向工具库具备静态 AST 解析脚本，能从 Webpack Bundle 中自动提取路由表结构与表单规则
- [ ] 配置 Playwright 无头浏览器运行基准环境，并提供一个基础的全局健康检查端到端验证通过
