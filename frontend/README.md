# HealthTrace 前端应用

这是一个基于 Vue 3 + Element Plus 的健康追踪系统前端应用。

## 功能特性

- 🏠 **仪表盘**: 健康数据概览和快速操作
- 🍽️ **饮食记录**: 记录每日饮食和营养分析
- 🏃 **运动记录**: 记录运动类型、时长和消耗
- 😴 **睡眠记录**: 记录睡眠时长和质量
- 👤 **个人资料**: 健康目标设置和账户管理
- 🔐 **用户认证**: 登录注册功能

## 技术栈

- **Vue 3**: 渐进式 JavaScript 框架
- **Vue Router**: 官方路由管理器
- **Pinia**: 状态管理库
- **Element Plus**: Vue 3 组件库
- **Axios**: HTTP 客户端
- **Vite**: 构建工具

## 项目结构

```
frontend/
├── src/
│   ├── api/           # API 接口
│   ├── components/    # 公共组件
│   ├── router/        # 路由配置
│   ├── stores/        # 状态管理
│   ├── views/         # 页面组件
│   ├── App.vue        # 根组件
│   └── main.js        # 入口文件
├── index.html         # HTML 模板
├── package.json       # 依赖配置
├── vite.config.js     # Vite 配置
└── README.md          # 项目说明
```

## 安装和运行

### 1. 安装依赖

```bash
cd frontend
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

应用将在 `http://localhost:3000` 启动。

### 3. 构建生产版本

```bash
npm run build
```

### 4. 预览生产版本

```bash
npm run preview
```

## 开发说明

### 后端 API 配置

前端通过代理连接到后端 API，配置在 `vite.config.js` 中：

```javascript
proxy: {
  '/api': {
    target: 'http://localhost:5000',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, '')
  }
}
```

确保后端服务器在 `http://localhost:5000` 运行。

### 路由配置

应用包含以下路由：

- `/login` - 登录页面
- `/register` - 注册页面
- `/dashboard` - 仪表盘
- `/diet` - 饮食记录
- `/exercise` - 运动记录
- `/sleep` - 睡眠记录
- `/profile` - 个人资料

### 状态管理

使用 Pinia 进行状态管理：

- `auth` store: 用户认证状态
- 其他业务状态可以根据需要扩展

### 组件说明

- `Layout.vue`: 主布局组件，包含侧边栏和顶部导航
- 各页面组件: 对应不同功能模块的页面

## 自定义配置

### 修改 API 地址

在 `vite.config.js` 中修改 `target` 地址：

```javascript
target: "http://your-backend-url:port";
```

### 修改主题

Element Plus 支持主题定制，可以在 `main.js` 中配置：

```javascript
app.use(ElementPlus, {
  locale: zhCn,
  // 添加自定义主题配置
});
```

## 部署

### 构建

```bash
npm run build
```

构建产物在 `dist` 目录中。

### 部署到服务器

将 `dist` 目录中的文件部署到 Web 服务器即可。

## 开发建议

1. **代码规范**: 使用 ESLint 进行代码检查
2. **组件复用**: 将公共功能提取为组件
3. **API 封装**: 统一管理 API 请求
4. **错误处理**: 添加适当的错误处理和用户提示
5. **响应式设计**: 确保在不同设备上的良好体验

## 注意事项

- 确保后端 API 正常运行
- 检查网络连接和代理配置
- 注意跨域问题处理
- 生产环境需要配置正确的 API 地址

## 许可证

MIT License
