# 商序 · 项目展示站

**[打开在线展示 →](https://fxbillu.github.io/side-project-showcase/)**

项目介绍、界面截图和设计概览集中在展示页。本仓库用于维护该静态网站。

[![商序业务总览，点击进入在线展示](assets/overview.png)](https://fxbillu.github.io/side-project-showcase/)

## 网站维护

- `index.html`：展示页面与原图查看器。
- `assets/`：封面、展示图与原图。
- `.nojekyll`：保持纯静态发布；`site-manifest.json`：发布文件的校验清单。

在本仓库目录运行以下命令，可通过 `http://127.0.0.1:8000` 本地预览：

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

页面及本文件由实现仓库的展示构建工具生成。更新时先修改源文件并检查，再同步生成结果，普通提交推送 `main`；GitHub Pages 从根目录发布。发布后核对部署结果、展示链接和图片加载。

业务源码、架构、接口契约、运行部署与测试证据由实现仓库维护。本站使用模拟数据，完整系统的在线操作 Demo 后续部署。

当前尚未指定开源许可证，公开展示不等于任意使用授权。
