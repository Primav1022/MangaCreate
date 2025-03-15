# MangaCreate

MangaCreate 是一个用于漫画创作的系统，结合了前端的 React 和后端的 Flask。该系统提供了一系列工具，帮助用户轻松创建和管理漫画内容。

## 项目结构

- **manga-frontend**: 使用 React 构建的前端应用，提供用户界面和交互功能。
- **manga-backend**: 使用 Flask 构建的后端应用，处理前端请求并返回数据。

## 功能特性

### 前端

- **工具栏**: 提供上传画风、添加文字脚本、添加画面灵感等功能。
- **画布**: 大型画布用于绘制和编辑漫画。
- **分镜版面**: 横向展示漫画分镜，便于查看和管理。

### 后端

- **数据接口**: 提供 RESTful API，支持前端与后端的数据交互。

## 安装与运行

### 前端

1. 进入 `manga-frontend` 目录：
   ```bash
   cd manga-frontend
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm start
   ```

### 后端

1. 进入 `manga-backend` 目录：
   ```bash
   cd manga-backend
   ```

2. 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 使用 venv\Scripts\activate
   ```

3. 安装 Flask：
   ```bash
   pip install flask
   ```

4. 启动 Flask 应用：
   ```bash
   flask run
   ```

## 使用说明

- 启动前端和后端后，打开浏览器访问 `http://localhost:3000` 查看前端应用。
- 前端应用会通过 Axios 向后端发送请求，获取和提交数据。

## 贡献

欢迎对本项目进行贡献！请提交 pull requests 或 issues 来帮助我们改进。

## 许可证

本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。 