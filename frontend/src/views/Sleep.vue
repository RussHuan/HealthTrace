<template>
  <Layout>
    <div class="sleep-page">
      <!-- 添加睡眠记录 -->
      <el-card class="add-record-card">
        <template #header>
          <div class="card-header">
            <span>添加睡眠记录</span>
          </div>
        </template>

        <el-form :model="sleepForm" label-width="100px">
          <el-row :gutter="20">
            <el-col :span="8">
              <el-form-item label="入睡时间">
                <el-time-picker
                  v-model="sleepForm.bedtime"
                  placeholder="选择入睡时间"
                  format="HH:mm"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="起床时间">
                <el-time-picker
                  v-model="sleepForm.wakeTime"
                  placeholder="选择起床时间"
                  format="HH:mm"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="睡眠质量">
                <el-select
                  v-model="sleepForm.quality"
                  placeholder="选择睡眠质量"
                >
                  <el-option label="很好" value="excellent" />
                  <el-option label="良好" value="good" />
                  <el-option label="一般" value="fair" />
                  <el-option label="较差" value="poor" />
                  <el-option label="很差" value="very_poor" />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>

          <el-row :gutter="20">
            <el-col :span="8">
              <el-form-item label="深睡时长">
                <el-input-number
                  v-model="sleepForm.deepSleep"
                  :min="0"
                  :max="8"
                  :precision="1"
                  placeholder="小时"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="浅睡时长">
                <el-input-number
                  v-model="sleepForm.lightSleep"
                  :min="0"
                  :max="8"
                  :precision="1"
                  placeholder="小时"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item>
                <el-button type="primary" @click="addSleepRecord">
                  <el-icon><Plus /></el-icon>
                  添加记录
                </el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </el-card>

      <!-- 今日睡眠记录 -->
      <el-card class="records-card">
        <template #header>
          <div class="card-header">
            <span>今日睡眠记录</span>
            <div class="header-actions">
              <el-tag type="success">总时长: {{ totalSleepHours }} 小时</el-tag>
              <el-tag type="info">深睡: {{ totalDeepSleep }} 小时</el-tag>
            </div>
          </div>
        </template>

        <el-table :data="todayRecords" style="width: 100%">
          <el-table-column prop="bedtime" label="入睡时间" width="120">
            <template #default="scope">
              {{ formatTime(scope.row.bedtime) }}
            </template>
          </el-table-column>
          <el-table-column prop="wakeTime" label="起床时间" width="120">
            <template #default="scope">
              {{ formatTime(scope.row.wakeTime) }}
            </template>
          </el-table-column>
          <el-table-column prop="duration" label="睡眠时长" width="120">
            <template #default="scope">
              {{ scope.row.duration }} 小时
            </template>
          </el-table-column>
          <el-table-column prop="deepSleep" label="深睡时长" width="120">
            <template #default="scope">
              {{ scope.row.deepSleep }} 小时
            </template>
          </el-table-column>
          <el-table-column prop="quality" label="睡眠质量" width="120">
            <template #default="scope">
              <el-tag :type="getQualityColor(scope.row.quality)">
                {{ getQualityLabel(scope.row.quality) }}
              </el-tag>
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

      <!-- 睡眠统计 -->
      <el-row :gutter="20" class="stats-row">
        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Moon /></el-icon>
              </div>
              <div class="stat-info">
                <h3>平均睡眠时长</h3>
                <p class="stat-value">{{ avgSleepHours }} 小时</p>
                <p class="stat-target">目标: 8 小时</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Star /></el-icon>
              </div>
              <div class="stat-info">
                <h3>平均睡眠质量</h3>
                <p class="stat-value">{{ avgQuality }}</p>
                <p class="stat-target">目标: 良好</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Timer /></el-icon>
              </div>
              <div class="stat-info">
                <h3>深睡比例</h3>
                <p class="stat-value">{{ deepSleepRatio }}%</p>
                <p class="stat-target">目标: 25%</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon">
                <el-icon><Calendar /></el-icon>
              </div>
              <div class="stat-info">
                <h3>连续达标天数</h3>
                <p class="stat-value">{{ consecutiveDays }} 天</p>
                <p class="stat-target">目标: 7 天</p>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <!-- 睡眠建议 -->
      <el-card class="advice-card">
        <template #header>
          <div class="card-header">
            <span>睡眠建议</span>
          </div>
        </template>

        <div class="advice-content">
          <el-alert
            v-if="sleepAdvice.length > 0"
            v-for="(advice, index) in sleepAdvice"
            :key="index"
            :title="advice.title"
            :description="advice.description"
            :type="advice.type"
            show-icon
            :closable="false"
            class="advice-item"
          />
          <el-empty v-else description="暂无睡眠建议" />
        </div>
      </el-card>
    </div>
  </Layout>
</template>

<script setup>
import { ref, computed } from "vue";
import { ElMessage } from "element-plus";
import Layout from "@/components/Layout.vue";

const sleepForm = ref({
  bedtime: null,
  wakeTime: null,
  quality: "",
  deepSleep: 0,
  lightSleep: 0,
});

const todayRecords = ref([
  {
    bedtime: "23:00",
    wakeTime: "07:30",
    duration: 8.5,
    deepSleep: 2.5,
    lightSleep: 6.0,
    quality: "good",
  },
]);

const totalSleepHours = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.duration, 0);
});

const totalDeepSleep = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.deepSleep, 0);
});

// 模拟统计数据
const avgSleepHours = ref(7.8);
const avgQuality = ref("良好");
const deepSleepRatio = ref(28);
const consecutiveDays = ref(5);

const sleepAdvice = ref([
  {
    title: "睡眠时长建议",
    description:
      "您的睡眠时长略低于推荐标准，建议保持8小时睡眠以获得最佳休息效果。",
    type: "warning",
  },
  {
    title: "深睡质量良好",
    description: "您的深睡比例达到28%，超过了推荐标准，说明睡眠质量不错。",
    type: "success",
  },
]);

const getQualityColor = (quality) => {
  const colors = {
    excellent: "success",
    good: "success",
    fair: "warning",
    poor: "danger",
    very_poor: "danger",
  };
  return colors[quality] || "info";
};

const getQualityLabel = (quality) => {
  const labels = {
    excellent: "很好",
    good: "良好",
    fair: "一般",
    poor: "较差",
    very_poor: "很差",
  };
  return labels[quality] || quality;
};

const formatTime = (time) => {
  return time;
};

const addSleepRecord = () => {
  if (!sleepForm.value.bedtime || !sleepForm.value.wakeTime) {
    ElMessage.warning("请填写完整的睡眠信息");
    return;
  }

  // 计算睡眠时长
  const bedtime = sleepForm.value.bedtime;
  const wakeTime = sleepForm.value.wakeTime;

  let duration = 0;
  if (bedtime && wakeTime) {
    const bedtimeHours = bedtime.getHours() + bedtime.getMinutes() / 60;
    const wakeHours = wakeTime.getHours() + wakeTime.getMinutes() / 60;

    if (wakeHours > bedtimeHours) {
      duration = wakeHours - bedtimeHours;
    } else {
      duration = 24 - bedtimeHours + wakeHours;
    }
  }

  const newRecord = {
    bedtime: `${bedtime.getHours().toString().padStart(2, "0")}:${bedtime
      .getMinutes()
      .toString()
      .padStart(2, "0")}`,
    wakeTime: `${wakeTime.getHours().toString().padStart(2, "0")}:${wakeTime
      .getMinutes()
      .toString()
      .padStart(2, "0")}`,
    duration: Math.round(duration * 10) / 10,
    deepSleep: sleepForm.value.deepSleep || 0,
    lightSleep: sleepForm.value.lightSleep || 0,
    quality: sleepForm.value.quality || "fair",
  };

  todayRecords.value.push(newRecord);

  // 重置表单
  sleepForm.value = {
    bedtime: null,
    wakeTime: null,
    quality: "",
    deepSleep: 0,
    lightSleep: 0,
  };

  ElMessage.success("睡眠记录添加成功");
};

const deleteRecord = (index) => {
  todayRecords.value.splice(index, 1);
  ElMessage.success("记录删除成功");
};
</script>

<style scoped>
.sleep-page {
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

.advice-card {
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
  background: linear-gradient(135deg, #a8edea, #fed6e3);
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

.advice-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.advice-item {
  margin-bottom: 0;
}
</style>
