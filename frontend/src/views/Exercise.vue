<template>
  <Layout>
    <div class="exercise-page">
      <!-- 添加运动记录 -->
      <el-card class="add-record-card">
        <template #header>
          <div class="card-header">
            <span>添加运动记录</span>
          </div>
        </template>

        <el-form :model="exerciseForm" label-width="100px">
          <el-row :gutter="20">
            <el-col :span="8">
              <el-form-item label="运动类型">
                <el-select
                  v-model="exerciseForm.type"
                  placeholder="选择运动类型"
                >
                  <el-option label="跑步" value="running" />
                  <el-option label="步行" value="walking" />
                  <el-option label="骑行" value="cycling" />
                  <el-option label="游泳" value="swimming" />
                  <el-option label="健身" value="gym" />
                  <el-option label="瑜伽" value="yoga" />
                  <el-option label="其他" value="other" />
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="运动时长">
                <el-input-number
                  v-model="exerciseForm.duration"
                  :min="1"
                  :max="300"
                  placeholder="分钟"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="消耗卡路里">
                <el-input-number
                  v-model="exerciseForm.calories"
                  :min="0"
                  :max="2000"
                  placeholder="卡路里"
                />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row :gutter="20">
            <el-col :span="8">
              <el-form-item label="运动强度">
                <el-select
                  v-model="exerciseForm.intensity"
                  placeholder="选择强度"
                >
                  <el-option label="低强度" value="low" />
                  <el-option label="中强度" value="medium" />
                  <el-option label="高强度" value="high" />
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="运动时间">
                <el-time-picker
                  v-model="exerciseForm.time"
                  placeholder="选择时间"
                  format="HH:mm"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item>
                <el-button type="primary" @click="addExerciseRecord">
                  <el-icon><Plus /></el-icon>
                  添加记录
                </el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </el-card>

      <!-- 今日运动记录 -->
      <el-card class="records-card">
        <template #header>
          <div class="card-header">
            <span>今日运动记录</span>
            <div class="header-actions">
              <el-tag type="success">总时长: {{ totalDuration }} 分钟</el-tag>
              <el-tag type="warning">消耗: {{ totalCalories }} kcal</el-tag>
            </div>
          </div>
        </template>

        <el-table :data="todayRecords" style="width: 100%">
          <el-table-column prop="type" label="运动类型" width="120">
            <template #default="scope">
              <el-tag :type="getExerciseTypeColor(scope.row.type)">
                {{ getExerciseTypeLabel(scope.row.type) }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="duration" label="时长" width="100">
            <template #default="scope">
              {{ scope.row.duration }} 分钟
            </template>
          </el-table-column>
          <el-table-column prop="calories" label="消耗卡路里" width="120">
            <template #default="scope">
              {{ scope.row.calories }} kcal
            </template>
          </el-table-column>
          <el-table-column prop="intensity" label="强度" width="100">
            <template #default="scope">
              <el-tag
                :type="getIntensityColor(scope.row.intensity)"
                size="small"
              >
                {{ getIntensityLabel(scope.row.intensity) }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="time" label="时间" width="120">
            <template #default="scope">
              {{ formatTime(scope.row.time) }}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="120">
            <template #default="scope">
              <el-button
                type="danger"
                size="small"
                @click="deleteRecord(scope.$index)"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>

      <!-- 运动统计 -->
      <el-row :gutter="20" class="stats-row">
        <el-col :span="8">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Timer /></el-icon>
              </div>
              <div class="stat-info">
                <h3>本周运动时长</h3>
                <p class="stat-value">{{ weeklyDuration }} 分钟</p>
                <p class="stat-target">目标: 150 分钟</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="8">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Fire /></el-icon>
              </div>
              <div class="stat-info">
                <h3>本周消耗卡路里</h3>
                <p class="stat-value">{{ weeklyCalories }} kcal</p>
                <p class="stat-target">目标: 1000 kcal</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="8">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Calendar /></el-icon>
              </div>
              <div class="stat-info">
                <h3>运动天数</h3>
                <p class="stat-value">{{ exerciseDays }} 天</p>
                <p class="stat-target">目标: 5 天</p>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </Layout>
</template>

<script setup>
import { ref, computed } from "vue";
import { ElMessage } from "element-plus";
import Layout from "@/components/Layout.vue";

const exerciseForm = ref({
  type: "",
  duration: 30,
  calories: 0,
  intensity: "",
  time: null,
});

const todayRecords = ref([
  {
    type: "running",
    duration: 30,
    calories: 300,
    intensity: "medium",
    time: "07:00",
  },
  {
    type: "walking",
    duration: 20,
    calories: 100,
    intensity: "low",
    time: "18:30",
  },
]);

const totalDuration = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.duration, 0);
});

const totalCalories = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.calories, 0);
});

// 模拟统计数据
const weeklyDuration = ref(180);
const weeklyCalories = ref(850);
const exerciseDays = ref(4);

const getExerciseTypeColor = (type) => {
  const colors = {
    running: "danger",
    walking: "success",
    cycling: "warning",
    swimming: "info",
    gym: "primary",
    yoga: "success",
    other: "info",
  };
  return colors[type] || "info";
};

const getExerciseTypeLabel = (type) => {
  const labels = {
    running: "跑步",
    walking: "步行",
    cycling: "骑行",
    swimming: "游泳",
    gym: "健身",
    yoga: "瑜伽",
    other: "其他",
  };
  return labels[type] || type;
};

const getIntensityColor = (intensity) => {
  const colors = {
    low: "success",
    medium: "warning",
    high: "danger",
  };
  return colors[intensity] || "info";
};

const getIntensityLabel = (intensity) => {
  const labels = {
    low: "低强度",
    medium: "中强度",
    high: "高强度",
  };
  return labels[intensity] || intensity;
};

const formatTime = (time) => {
  return time;
};

const addExerciseRecord = () => {
  if (!exerciseForm.value.type || !exerciseForm.value.duration) {
    ElMessage.warning("请填写完整的运动信息");
    return;
  }

  const newRecord = {
    ...exerciseForm.value,
    time: exerciseForm.value.time
      ? `${exerciseForm.value.time
          .getHours()
          .toString()
          .padStart(2, "0")}:${exerciseForm.value.time
          .getMinutes()
          .toString()
          .padStart(2, "0")}`
      : new Date().toLocaleTimeString("zh-CN", {
          hour: "2-digit",
          minute: "2-digit",
        }),
  };

  todayRecords.value.push(newRecord);

  // 重置表单
  exerciseForm.value = {
    type: "",
    duration: 30,
    calories: 0,
    intensity: "",
    time: null,
  };

  ElMessage.success("运动记录添加成功");
};

const deleteRecord = (index) => {
  todayRecords.value.splice(index, 1);
  ElMessage.success("记录删除成功");
};
</script>

<style scoped>
.exercise-page {
  padding: 0;
}

.add-record-card {
  margin-bottom: 20px;
}

.records-card {
  margin-bottom: 20px;
}

.stats-row {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
  color: #333;
}

.header-actions {
  display: flex;
  gap: 10px;
}

.stat-card {
  height: 120px;
}

.stat-content {
  display: flex;
  align-items: center;
  height: 100%;
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-size: 24px;
  color: white;
  background: linear-gradient(135deg, #4ecdc4, #44a08d);
}

.stat-info h3 {
  margin: 0 0 5px 0;
  font-size: 14px;
  color: #666;
  font-weight: normal;
}

.stat-value {
  margin: 0 0 5px 0;
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.stat-target {
  margin: 0;
  font-size: 12px;
  color: #999;
}
</style>
