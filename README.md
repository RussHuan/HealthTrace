# 只有这一段是我写的

2025/8/1 完成后端用户注册和登录部分，其他部分还在开发，用 cursor 生成了前端用于我的测试

# HealthTrace - 健康追踪系统

一个完整的健康数据管理应用，包含 Flask 后端和 Vue 3 前端。

## 项目结构

```
HealthTrace/
├── backend/           # Flask 后端应用
│   ├── models/       # 数据模型
│   ├── routes/       # API 路由
│   ├── services/     # 业务逻辑
│   ├── utils/        # 工具函数
│   └── __init__.py   # 应用入口
├── frontend/         # Vue 3 前端应用
│   ├── src/          # 源代码
│   ├── package.json  # 依赖配置
│   └── README.md     # 前端说明
└── README.md         # 项目说明
```

## 功能特性

### 后端功能

- ✅ 用户认证 (注册/登录)
- ✅ 用户管理
- ✅ 数据模型设计
- ✅ RESTful API
- ✅ 数据库集成
- ✅ 睡眠记录管理
- ✅ 睡眠数据统计

### 前端功能

- ✅ 用户界面 (登录/注册)
- ✅ 仪表盘数据展示
- ✅ 饮食记录管理
- ✅ 运动记录管理
- ✅ 睡眠记录管理
- ✅ 个人资料设置
- ✅ 响应式设计
- ✅ 睡眠数据可视化
- ✅ 睡眠健康建议

## 快速开始

### 1. 启动后端

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python __init__.py
```

后端将在 `http://localhost:5000` 启动。

#### 2. 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端将在 `http://localhost:3000` 启动。

#### 3. 访问应用

打开浏览器访问 `http://localhost:3000` 即可使用应用。

## 技术栈

### 后端

- **Flask**: Web 框架
- **SQLAlchemy**: ORM
- **SQLite**: 数据库
- **Werkzeug**: 安全工具

### 前端

- **Vue 3**: 前端框架
- **Element Plus**: UI 组件库
- **Vue Router**: 路由管理
- **Pinia**: 状态管理
- **Axios**: HTTP 客户端
- **Vite**: 构建工具

## API 接口

### 用户认证

- `POST /users/register` - 用户注册
- `POST /users/login` - 用户登录

### 睡眠记录管理

- `POST /sleep/records` - 添加睡眠记录
- `GET /sleep/records/{user_id}` - 获取用户睡眠记录
- `PUT /sleep/records/{record_id}` - 更新睡眠记录
- `DELETE /sleep/records/{record_id}` - 删除睡眠记录
- `GET /sleep/stats/{user_id}` - 获取睡眠统计

### 响应格式

```json
{
  "code": 0,
  "msg": "success",
  "data": {}
}
```

## 开发说明

### 后端开发

1. 在 `backend/models/` 中添加数据模型
2. 在 `backend/routes/` 中添加 API 路由
3. 在 `backend/services/` 中添加业务逻辑

### 前端开发

1. 在 `frontend/src/views/` 中添加页面组件
2. 在 `frontend/src/api/` 中添加 API 接口
3. 在 `frontend/src/stores/` 中添加状态管理

## 部署

### 后端部署

```bash
cd backend
pip install -r requirements.txt
python __init__.py
```

### 前端部署

```bash
cd frontend
npm run build
# 将 dist 目录部署到 Web 服务器
```

## 睡眠记录模块

睡眠记录模块是系统的核心功能之一，提供完整的睡眠数据管理：

- **记录功能**: 记录入睡时间、起床时间，自动计算睡眠时长
- **质量评估**: 1-10 分睡眠质量评分系统
- **数据统计**: 平均睡眠时长、质量评分、最佳睡眠记录等
- **健康建议**: 基于睡眠数据提供个性化健康建议
- **数据可视化**: 直观的图表展示睡眠趋势

详细文档请参考：[睡眠记录模块文档](backend/README_SLEEP.md)

## 注意事项

1. 确保 Python 3.7+ 和 Node.js 14+ 已安装
2. 后端使用 SQLite 数据库，生产环境建议使用 PostgreSQL 或 MySQL
3. 前端通过代理连接后端，生产环境需要配置正确的 API 地址
4. 当前为演示版本，生产环境需要添加更多安全措施
5. 睡眠记录支持跨天计算，自动处理日期变更

## 许可证

MIT License
