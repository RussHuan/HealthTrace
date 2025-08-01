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
                <el-date-picker
                  v-model="sleepForm.sleepTime"
                  type="datetime"
                  placeholder="选择入睡时间"
                  format="YYYY-MM-DD HH:mm"
                  value-format="YYYY-MM-DDTHH:mm:ss"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="起床时间">
                <el-date-picker
                  v-model="sleepForm.wakeTime"
                  type="datetime"
                  placeholder="选择起床时间"
                  format="YYYY-MM-DD HH:mm"
                  value-format="YYYY-MM-DDTHH:mm:ss"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="睡眠质量">
                <el-rate
                  v-model="sleepForm.qualityRating"
                  :max="10"
                  show-score
                  :texts="['很差', '差', '一般', '良好', '很好', '优秀', '极好', '完美', '卓越', '理想']"
                />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row :gutter="20">
            <el-col :span="16">
              <el-form-item label="备注">
                <el-input
                  v-model="sleepForm.notes"
                  type="textarea"
                  placeholder="添加备注信息（可选）"
                  :rows="2"
                />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item>
                <el-button type="primary" @click="addSleepRecord" :loading="loading">
                  <el-icon><Plus /></el-icon>
                  添加记录
                </el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </el-card>

      <!-- 睡眠记录列表 -->
      <el-card class="records-card">
        <template #header>
          <div class="card-header">
            <span>睡眠记录</span>
            <div class="header-actions">
              <el-date-picker
                v-model="dateRange"
                type="daterange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                format="YYYY-MM-DD"
                value-format="YYYY-MM-DD"
                @change="loadSleepRecords"
                style="margin-right: 10px;"
              />
              <el-tag type="success">平均时长: {{ avgDuration }} 小时</el-tag>
              <el-tag type="info">记录数: {{ sleepRecords.length }}</el-tag>
            </div>
          </div>
        </template>

        <el-table :data="sleepRecords" style="width: 100%" v-loading="tableLoading">
          <el-table-column prop="sleep_time" label="入睡时间" width="160">
            <template #default="scope">
              {{ formatDateTime(scope.row.sleep_time) }}
            </template>
          </el-table-column>
          <el-table-column prop="wake_time" label="起床时间" width="160">
            <template #default="scope">
              {{ formatDateTime(scope.row.wake_time) }}
            </template>
          </el-table-column>
          <el-table-column prop="duration_hours" label="睡眠时长" width="120">
            <template #default="scope">
              <el-tag :type="getDurationColor(scope.row.duration_hours)">
                {{ scope.row.duration_hours }} 小时
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="quality_rating" label="睡眠质量" width="120">
            <template #default="scope">
              <el-rate
                v-model="scope.row.quality_rating"
                :max="10"
                disabled
                show-score
                text-color="#ff9900"
              />
            </template>
          </el-table-column>
          <el-table-column prop="notes" label="备注" min-width="200">
            <template #default="scope">
              {{ scope.row.notes || '-' }}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="150">
            <template #default="scope">
              <el-button
                type="primary"
                size="small"
                @click="editRecord(scope.row)"
              >
                编辑
              </el-button>
              <el-button
                type="danger"
                size="small"
                @click="deleteRecord(scope.row.id)"
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
                <p class="stat-value">{{ sleepStats.average_duration || 0 }} 小时</p>
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
                <p class="stat-value">{{ sleepStats.average_quality || 0 }}/10</p>
                <p class="stat-target">目标: 8/10</p>
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
                <h3>记录总数</h3>
                <p class="stat-value">{{ sleepStats.total_records || 0 }} 条</p>
                <p class="stat-target">最近7天</p>
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
                <h3>最佳睡眠</h3>
                <p class="stat-value">{{ sleepStats.best_sleep ? sleepStats.best_sleep.duration_hours : 0 }} 小时</p>
                <p class="stat-target">{{ sleepStats.best_sleep ? formatDate(sleepStats.best_sleep.sleep_time) : '暂无' }}</p>
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
import { ref, computed, onMounted } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import { addSleepRecord as addSleepRecordAPI, getSleepRecords, updateSleepRecord, deleteSleepRecord as deleteSleepRecordAPI, getSleepStats } from "@/api/sleep.js";
import { useAuthStore } from "@/stores/auth.js";

const authStore = useAuthStore();

const sleepForm = ref({
  sleepTime: null,
  wakeTime: null,
  qualityRating: 5,
  notes: "",
});

const sleepRecords = ref([]);
const sleepStats = ref({});
const loading = ref(false);
const tableLoading = ref(false);
const dateRange = ref([]);

// 计算平均睡眠时长
const avgDuration = computed(() => {
  if (sleepRecords.value.length === 0) return 0;
  const total = sleepRecords.value.reduce((sum, record) => sum + record.duration_hours, 0);
  return (total / sleepRecords.value.length).toFixed(1);
});

// 睡眠建议
const sleepAdvice = computed(() => {
  const advice = [];
  const avgDuration = sleepStats.value.average_duration || 0;
  const avgQuality = sleepStats.value.average_quality || 0;

  if (avgDuration < 7) {
    advice.push({
      title: "睡眠时长不足",
      description: "您的平均睡眠时长低于推荐标准，建议保持7-9小时睡眠以获得最佳休息效果。",
      type: "warning",
    });
  } else if (avgDuration > 9) {
    advice.push({
      title: "睡眠时长过长",
      description: "您的睡眠时长可能过长，建议控制在7-9小时范围内。",
      type: "info",
    });
  } else {
    advice.push({
      title: "睡眠时长良好",
      description: "您的睡眠时长在健康范围内，继续保持！",
      type: "success",
    });
  }

  if (avgQuality < 6) {
    advice.push({
      title: "睡眠质量待改善",
      description: "您的睡眠质量评分较低，建议改善睡眠环境和习惯。",
      type: "warning",
    });
  } else if (avgQuality >= 8) {
    advice.push({
      title: "睡眠质量优秀",
      description: "您的睡眠质量很好，继续保持良好的睡眠习惯！",
      type: "success",
    });
  }

  return advice;
});

// 格式化日期时间
const formatDateTime = (dateTimeStr) => {
  if (!dateTimeStr) return '-';
  const date = new Date(dateTimeStr);
  return date.toLocaleString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
};

// 格式化日期
const formatDate = (dateTimeStr) => {
  if (!dateTimeStr) return '-';
  const date = new Date(dateTimeStr);
  return date.toLocaleDateString('zh-CN');
};

// 获取睡眠时长颜色
const getDurationColor = (duration) => {
  if (duration >= 7 && duration <= 9) return 'success';
  if (duration >= 6 && duration < 7) return 'warning';
  if (duration > 9) return 'info';
  return 'danger';
};

// 加载睡眠记录
const loadSleepRecords = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  tableLoading.value = true;
  try {
    const params = {};
    if (dateRange.value && dateRange.value.length === 2) {
      params.start_date = dateRange.value[0];
      params.end_date = dateRange.value[1];
    }
    
    const response = await getSleepRecords(authStore.userId, params);
    sleepRecords.value = response.data || [];
  } catch (error) {
    ElMessage.error(error.message || "加载睡眠记录失败");
  } finally {
    tableLoading.value = false;
  }
};

// 加载睡眠统计
const loadSleepStats = async () => {
  if (!authStore.userId) return;

  try {
    const response = await getSleepStats(authStore.userId, 7);
    sleepStats.value = response.data || {};
  } catch (error) {
    console.error("加载睡眠统计失败:", error);
  }
};

// 添加睡眠记录
const addSleepRecord = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  if (!sleepForm.value.sleepTime || !sleepForm.value.wakeTime) {
    ElMessage.warning("请填写完整的睡眠信息");
    return;
  }

  loading.value = true;
  try {
    const sleepData = {
      user_id: authStore.userId,
      sleep_time: sleepForm.value.sleepTime,
      wake_time: sleepForm.value.wakeTime,
      quality_rating: sleepForm.value.qualityRating,
      notes: sleepForm.value.notes || "",
    };

    await addSleepRecordAPI(sleepData);
    
    // 重置表单
    sleepForm.value = {
      sleepTime: null,
      wakeTime: null,
      qualityRating: 5,
      notes: "",
    };

    ElMessage.success("睡眠记录添加成功");
    
    // 重新加载数据
    await loadSleepRecords();
    await loadSleepStats();
  } catch (error) {
    ElMessage.error(error.message || "添加睡眠记录失败");
  } finally {
    loading.value = false;
  }
};

// 编辑睡眠记录
const editRecord = (record) => {
  // 这里可以实现编辑功能，暂时显示提示
  ElMessage.info("编辑功能开发中...");
};

// 删除睡眠记录
const deleteRecord = async (recordId) => {
  try {
    await ElMessageBox.confirm("确定要删除这条睡眠记录吗？", "确认删除", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning",
    });

    await deleteSleepRecordAPI(recordId);
    ElMessage.success("睡眠记录删除成功");
    
    // 重新加载数据
    await loadSleepRecords();
    await loadSleepStats();
  } catch (error) {
    if (error !== "cancel") {
      ElMessage.error(error.message || "删除睡眠记录失败");
    }
  }
};

// 页面加载时获取数据
onMounted(async () => {
  await loadSleepRecords();
  await loadSleepStats();
});
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
