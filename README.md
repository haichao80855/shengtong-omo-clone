# 盛通教育 OMO 平台（一校平台）高精度全栈复刻工程

高精度还原盛通教育 OMO 平台（`manage.shengtongedu.cn`）核心功能，涵盖：
1. **门户与工作台看板**（校区准入卡片与关键运营指标）
2. **系统模块**（机构管理、教学场地与多媒体教室）
3. **教研模块**（标准课程大纲管理与编程素材库）
4. **学员模块**（学员档案全生命周期、选课报名、电子钱包与 Excel 批量导入）
5. **教务模块**（售卖课程商品包装、班级日历排课冲突检测、教学点名考勤、自动课消与课后评价）

## 架构与技术栈

- **Monorepo**: pnpm 工作区
- **前端应用 (`apps/web`)**: Vue 3 + Vite + Element Plus + Pinia + Vue Router
- **后端服务 (`apps/server`)**: NestJS + Prisma ORM + PostgreSQL 16 模块化单体
- **共享契约 (`packages/api-contract`)**: OpenAPI 3.0 / TypeScript 共享类型与数据字典
- **逆向与测试 (`tools/crawler`)**: AST 静态规则抽取 + Playwright 离线 1920x1080 黄金比对测试套件

## 项目管理与工单

本项目使用 GitHub Issues 进行全流程任务跟踪：
- 仓库地址: [haichao80855/shengtong-omo-clone](https://github.com/haichao80855/shengtong-omo-clone)
- 工单列表: [Issues 列表](https://github.com/haichao80855/shengtong-omo-clone/issues)
