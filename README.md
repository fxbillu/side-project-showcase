# 商序 · 商贸进销存

面向单公司、多仓库商贸业务的自主开发案例，将采购、销售、库存和往来结算沿来源单据关联起来，保留可追溯、可核对的业务记录。

**[查看业务流程与界面 →](https://fxbillu.github.io/side-project-showcase/#journey)** · [公开验证摘要](verification/README.md) · [查看设计取舍](https://fxbillu.github.io/side-project-showcase/#design)

[![商序业务总览：采购、销售、库存与往来款](assets/overview.png)](https://fxbillu.github.io/side-project-showcase/#screens)

## 已实现的业务

采购/销售订单、分批收发货、退货退款、分仓库存、调拨盘点、应收应付及对账报表；管理员、采购、销售、仓库、财务与只读角色按职责操作。

## 三个具体设计

- **分批金额对得上**：3件单价0.335，分三次各一件结算为0.34、0.33、0.34；退货沿用实际来源批次金额。
- **盘盈成本有人确认**：仓库先录数量，管理员或财务明确确认零库存盘盈成本，零价需原因，再按权限审核。
- **历史变化查得到**：审核保存关键资料快照，冲销保留原始与反向流水，资料修改记录前后值。

Java 21 / Spring Boot / PostgreSQL · Vue 3 / TypeScript / Element Plus。已有HTTP接口契约、OpenAPI描述及CSV交换能力，第三方连接器尚未实现。

## 可以核对的结果与当前状态

已实现本地主流程，有实际页面操作和测试记录。公开材料提供分仓库存、客户对账、历史批次金额三个离线复算算例，附CSV、API字段摘录、Python脚本和文件哈希，无需访问私有仓库。

**[查看材料与复算方法](verification/README.md)** · [直接阅读验证网页](https://fxbillu.github.io/side-project-showcase/verification/)

这是使用模拟数据的演示案例，暂无客户签收。实际文件上传、改密及账号变更尚待完整操作验收；完整系统的公网Demo后续部署。公开算例核对不等于全部功能或生产环境验收通过。

<details>
<summary>网站维护与发布方式</summary>

本公开仓库承载静态展示页；业务源码、完整架构、接口契约、运行部署和完整测试证据在实现仓库维护。

- `index.html`：流程讲解和截图查看器；`assets/`：截图及原图。
- `verification/`：公开验证摘要、模拟数据与离线复算脚本；`verification.zip`：独立材料包。
- `.nojekyll` 保持纯静态发布，`site-manifest.json` 记录发布文件哈希。

在本仓库目录预览：

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

内容由实现仓库的构建工具生成；先改源文件并验证，再同步结果，普通提交推送`main`，等待Pages部署成功并核对链接。网站使用授权另行确定，当前未指定开源许可证。

</details>
