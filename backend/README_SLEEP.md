# 接下来的计划
- 完成账号密码更改和注销功能
- 实际部署所有功能
- 开发新的功能
- 现在需要解决的问题：1.每次切换页面或者提交请求后，界面不会自动刷新，需要手动刷新后才会改变 2.后端提交运动和饮食记录没有bug，但是前端没有真正显示实际数据，一直保持无数据的状态 

# 睡眠记录模块

## 功能概述

睡眠记录模块是 HealthTrace 健康管理系统的重要组成部分，用于记录和管理用户的睡眠数据，包括：

- 记录用户的入睡时间和起床时间
- 自动计算睡眠时长
- 睡眠质量评分（1-10 分）
- 睡眠记录备注
- 睡眠数据统计和分析
- 睡眠健康建议

## 数据库模型

### Sleep 模型

```python
class Sleep(db.Model):
    __tablename__ = 'sleep_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sleep_time = db.Column(db.DateTime, nullable=False)  # 入睡时间
    wake_time = db.Column(db.DateTime, nullable=False)   # 起床时间
    duration_hours = db.Column(db.Float, nullable=False) # 睡眠时长（小时）
    quality_rating = db.Column(db.Integer)  # 睡眠质量评分 1-10
    notes = db.Column(db.Text)  # 备注
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

## API 接口

### 1. 添加睡眠记录

**POST** `/sleep/records`

**请求体：**

```json
{
  "user_id": 1,
  "sleep_time": "2024-01-15T23:00:00",
  "wake_time": "2024-01-16T07:30:00",
  "quality_rating": 8,
  "notes": "睡眠质量不错"
}
```

**响应：**

```json
{
  "success": true,
  "message": "睡眠记录添加成功",
  "data": {
    "id": 1,
    "user_id": 1,
    "sleep_time": "2024-01-15T23:00:00",
    "wake_time": "2024-01-16T07:30:00",
    "duration_hours": 8.5,
    "quality_rating": 8,
    "notes": "睡眠质量不错",
    "created_at": "2024-01-16T08:00:00",
    "updated_at": "2024-01-16T08:00:00"
  }
}
```

### 2. 获取用户睡眠记录

**GET** `/sleep/records/{user_id}`

**查询参数：**

- `start_date`: 开始日期（可选）
- `end_date`: 结束日期（可选）
- `limit`: 限制返回记录数量（默认 30）

**响应：**

```json
{
  "success": true,
  "message": "获取睡眠记录成功",
  "data": [
    {
      "id": 1,
      "user_id": 1,
      "sleep_time": "2024-01-15T23:00:00",
      "wake_time": "2024-01-16T07:30:00",
      "duration_hours": 8.5,
      "quality_rating": 8,
      "notes": "睡眠质量不错",
      "created_at": "2024-01-16T08:00:00",
      "updated_at": "2024-01-16T08:00:00"
    }
  ]
}
```

### 3. 更新睡眠记录

**PUT** `/sleep/records/{record_id}`

**请求体：**

```json
{
  "quality_rating": 9,
  "notes": "更新后的备注"
}
```

### 4. 删除睡眠记录

**DELETE** `/sleep/records/{record_id}`

### 5. 获取睡眠统计

**GET** `/sleep/stats/{user_id}`

**查询参数：**

- `days`: 统计天数（默认 7 天）

**响应：**

```json
{
  "success": true,
  "message": "获取睡眠统计成功",
  "data": {
    "total_records": 7,
    "average_duration": 7.8,
    "average_quality": 7.5,
    "best_sleep": {
      "id": 3,
      "duration_hours": 9.2,
      "sleep_time": "2024-01-14T22:30:00"
    },
    "worst_sleep": {
      "id": 1,
      "duration_hours": 6.5,
      "sleep_time": "2024-01-12T23:30:00"
    }
  }
}
```

## 前端功能

### 主要功能

1. **添加睡眠记录**

   - 选择入睡时间和起床时间
   - 睡眠质量评分（1-10 分）
   - 添加备注信息

2. **睡眠记录列表**

   - 显示所有睡眠记录
   - 按日期范围筛选
   - 编辑和删除记录

3. **睡眠统计**

   - 平均睡眠时长
   - 平均睡眠质量
   - 记录总数
   - 最佳睡眠记录

4. **睡眠建议**
   - 基于睡眠数据提供健康建议
   - 睡眠时长建议
   - 睡眠质量改善建议

### 技术特性

- 响应式设计，支持移动端
- 实时数据更新
- 数据可视化展示
- 用户友好的界面

## 安装和运行

### 后端

1. 安装依赖：

```bash
cd backend
pip install -r requirements.txt
```

2. 运行应用：

```bash
python __init__.py
```

3. 测试 API：

```bash
python test_sleep.py
```

### 前端

1. 安装依赖：

```bash
cd frontend
npm install
```

2. 运行开发服务器：

```bash
npm run dev
```

## 使用示例

### 添加睡眠记录

```javascript
import { addSleepRecord } from "@/api/sleep.js";

const sleepData = {
  user_id: 1,
  sleep_time: "2024-01-15T23:00:00",
  wake_time: "2024-01-16T07:30:00",
  quality_rating: 8,
  notes: "睡眠质量不错",
};

try {
  const response = await addSleepRecord(sleepData);
  console.log("睡眠记录添加成功:", response.data);
} catch (error) {
  console.error("添加失败:", error.message);
}
```

### 获取睡眠统计

```javascript
import { getSleepStats } from "@/api/sleep.js";

try {
  const response = await getSleepStats(1, 7); // 用户ID=1，最近7天
  console.log("睡眠统计:", response.data);
} catch (error) {
  console.error("获取统计失败:", error.message);
}
```

## 健康建议算法

系统会根据用户的睡眠数据自动生成健康建议：

1. **睡眠时长建议**

   - 少于 7 小时：建议增加睡眠时间
   - 7-9 小时：睡眠时长良好
   - 超过 9 小时：建议控制睡眠时间

2. **睡眠质量建议**
   - 评分低于 6 分：建议改善睡眠环境
   - 评分 8 分以上：睡眠质量优秀

## 注意事项

1. 时间格式必须使用 ISO 8601 格式（YYYY-MM-DDTHH:mm:ss）
2. 睡眠时长会自动计算，无需手动输入
3. 质量评分范围为 1-10 分
4. 所有 API 都需要有效的用户 ID
5. 建议定期备份睡眠数据

## 扩展功能

未来可以考虑添加的功能：

1. 睡眠阶段分析（深睡、浅睡、REM）
2. 睡眠环境监测（温度、湿度、噪音）
3. 睡眠习惯追踪
4. 睡眠报告生成
5. 智能闹钟推荐
6. 睡眠数据导出
