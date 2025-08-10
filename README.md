# HealthTrace 健迹 - 健康追踪系统

一款面向高校学生的健康管理平台，整合**睡眠监测**、**运动规划**和**饮食记录**三大核心功能，通过数据采集、可视化分析及智能建议，帮助学生改善生活习惯。


包含 Flask 后端和 Vue 3 前端。

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

✅ **个人健康档案管理**：用户注册、登录、注销以及个人健康档案管理。

✅ **睡眠记录模块**：记录用户每天入睡和起床时间，并计算睡眠时长，提供一周睡眠数据的可视化展示。

✅ **运动记录模块**：记录用户每天的运动情况，包括运动类型、运动时长和消耗的卡路里数等。

✅ **饮食记录模块**：记录用户每天的三餐饮食，包括食物名称、份量和估算的卡路里等，根据内置的常见食物卡路里参考值智能计算。

✅ **健康周报**：根据每周记录的睡眠、运动和饮食数据，由外接 LLM 提供健康建议，用户可以自由配置 LLM API。

✅ **健康目标**：允许用户设定个人健康目标，并在首页用圆环进度可视化展示。

✅ **智能饮食推荐**：根据用户近期的运动情况，外接 LLM 并对接开源营养数据库实现饮食的智能推荐，用户可以自由配置 LLM API。

✅ **异常预警**：当用户连续多天睡眠不足时，在睡眠记录界面弹出自动提醒。


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
npm install ant-design-vue@4.x --save
npm install echarts
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
- **Ant Design Vue**：UI 组件库
- **ECharts**：图表库
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

### 运动记录管理

路由均仿照睡眠管理

- `POST /exercise/records` - 添加运动记录
  ……

### 响应格式

```json
{
  "code": 0,
  "msg": "success",
  "data": {}
}
```
