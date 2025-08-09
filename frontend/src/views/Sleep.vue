<template>
  <Layout>
    <div class="sleep-page">
      <!-- 睡眠统计 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <!-- 平均睡眠时长 -->
          <a-col :xs="24" :sm="12" :md="6" style="height: 140px">
            <a-card
              :bordered="false"
              style="
                height: 100%;
                display: flex;
                align-items: center;
                min-width: 0;
              "
            >
              <div
                style="
                  display: flex;
                  align-items: center;
                  width: 100%;
                  min-width: 0;
                "
              >
                <div
                  style="
                    font-size: 32px;
                    color: #1890ff;
                    margin-right: 12px;
                    flex-shrink: 0;
                  "
                >
                  <el-icon><Moon /></el-icon>
                </div>
                <div
                  style="
                    display: flex;
                    flex-direction: column;
                    overflow: hidden;
                    min-width: 0;
                  "
                >
                  <h3
                    style="
                      margin: 0;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    平均睡眠时长
                  </h3>
                  <p
                    style="
                      margin: 0;
                      font-weight: bold;
                      font-size: 26px;
                      line-height: 1.4;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    {{ sleepStats.average_duration || 0 }} 小时
                  </p>
                  <p
                    style="
                      margin: 0;
                      color: #888;
                      font-size: 14px;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    目标: 8 小时
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>

          <!-- 平均睡眠质量 -->
          <a-col :xs="0" :sm="12" :md="6" style="height: 140px" class="hide-xs">
            <a-card
              :bordered="false"
              style="
                height: 100%;
                display: flex;
                align-items: center;
                min-width: 0;
              "
            >
              <div
                style="
                  display: flex;
                  align-items: center;
                  width: 100%;
                  min-width: 0;
                "
              >
                <div
                  style="
                    font-size: 32px;
                    color: #1890ff;
                    margin-right: 12px;
                    flex-shrink: 0;
                  "
                >
                  <el-icon><Star /></el-icon>
                </div>
                <div
                  style="
                    display: flex;
                    flex-direction: column;
                    overflow: hidden;
                    min-width: 0;
                  "
                >
                  <h3
                    style="
                      margin: 0;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    平均睡眠质量
                  </h3>
                  <p
                    style="
                      margin: 0;
                      font-weight: bold;
                      font-size: 26px;
                      line-height: 1.4;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    {{ sleepStats.average_quality || 0 }}/10
                  </p>
                  <p
                    style="
                      margin: 0;
                      color: #888;
                      font-size: 14px;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    目标: 8/10
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>

          <!-- 记录总数 -->
          <a-col
            :xs="0"
            :sm="0"
            :md="6"
            style="height: 140px"
            class="hide-sm-xs"
          >
            <a-card
              :bordered="false"
              style="
                height: 100%;
                display: flex;
                align-items: center;
                min-width: 0;
              "
            >
              <div
                style="
                  display: flex;
                  align-items: center;
                  width: 100%;
                  min-width: 0;
                "
              >
                <div
                  style="
                    font-size: 32px;
                    color: #1890ff;
                    margin-right: 12px;
                    flex-shrink: 0;
                  "
                >
                  <el-icon><Timer /></el-icon>
                </div>
                <div
                  style="
                    display: flex;
                    flex-direction: column;
                    overflow: hidden;
                    min-width: 0;
                  "
                >
                  <h3
                    style="
                      margin: 0;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    记录总数
                  </h3>
                  <p
                    style="
                      margin: 0;
                      font-weight: bold;
                      font-size: 26px;
                      line-height: 1.4;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    {{ sleepStats.total_records || 0 }} 条
                  </p>
                  <p
                    style="
                      margin: 0;
                      color: #888;
                      font-size: 14px;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    最近7天
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>

          <!-- 最佳睡眠 -->
          <a-col
            :xs="0"
            :sm="0"
            :md="6"
            style="height: 140px"
            class="hide-sm-xs"
          >
            <a-card
              :bordered="false"
              style="
                height: 100%;
                display: flex;
                align-items: center;
                min-width: 0;
              "
            >
              <div
                style="
                  display: flex;
                  align-items: center;
                  width: 100%;
                  min-width: 0;
                "
              >
                <div
                  style="
                    font-size: 32px;
                    color: #1890ff;
                    margin-right: 12px;
                    flex-shrink: 0;
                  "
                >
                  <el-icon><Calendar /></el-icon>
                </div>
                <div
                  style="
                    display: flex;
                    flex-direction: column;
                    overflow: hidden;
                    min-width: 0;
                  "
                >
                  <h3
                    style="
                      margin: 0;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    最佳睡眠
                  </h3>
                  <p
                    style="
                      margin: 0;
                      font-weight: bold;
                      font-size: 26px;
                      line-height: 1.4;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    {{
                      sleepStats.best_sleep
                        ? sleepStats.best_sleep.duration_hours
                        : 0
                    }}
                    小时
                  </p>
                  <p
                    style="
                      margin: 0;
                      color: #888;
                      font-size: 14px;
                      white-space: nowrap;
                      overflow: hidden;
                      text-overflow: ellipsis;
                    "
                  >
                    {{
                      sleepStats.best_sleep
                        ? formatDate(sleepStats.best_sleep.sleep_time)
                        : "暂无"
                    }}
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 一周睡眠趋势 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="一周睡眠趋势" style="height: 100%">
              <!-- ECharts 容器 -->
              <div ref="sleepChartRef" style="height: 300px; width: 100%;"></div>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 睡眠记录列表 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="睡眠记录列表" style="height: 100%">
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
                  style="margin-right: 10px"
                />
                <el-tag type="success">平均时长: {{ avgDuration }} 小时</el-tag>
                <el-tag type="info">记录数: {{ sleepRecords.length }}</el-tag>
              </div>
              <el-table
                :data="sleepRecords"
                style="width: 100%"
                v-loading="tableLoading"
              >
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
                <el-table-column
                  prop="duration_hours"
                  label="睡眠时长"
                  width="120"
                >
                  <template #default="scope">
                    <el-tag :type="getDurationColor(scope.row.duration_hours)">
                      {{ scope.row.duration_hours }} 小时
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column
                  prop="quality_rating"
                  label="睡眠质量"
                  width="120"
                >
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
                    {{ scope.row.notes || "-" }}
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
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 添加睡眠记录 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="添加睡眠记录" style="height: 100%">
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
                        :texts="[
                          '很差',
                          '差',
                          '一般',
                          '良好',
                          '很好',
                          '优秀',
                          '极好',
                          '完美',
                          '卓越',
                          '理想',
                        ]"
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
                      <el-button
                        type="primary"
                        @click="addSleepRecord"
                        :loading="loading"
                      >
                        <el-icon><Plus /></el-icon>
                        添加记录
                      </el-button>
                    </el-form-item>
                  </el-col>
                </el-row>
              </el-form>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 睡眠建议 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="睡眠建议" style="height: 100%">
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
            </a-card>
          </a-col>
        </a-row>
      </div>
    </div>
  </Layout>
  <el-dialog v-model="editDialogVisible" title="编辑睡眠记录" width="600px">
    <el-form :model="editForm" label-width="100px">
      <el-form-item label="入睡时间">
        <el-date-picker
          v-model="editForm.sleepTime"
          type="datetime"
          placeholder="选择入睡时间"
          format="YYYY-MM-DD HH:mm"
          value-format="YYYY-MM-DDTHH:mm:ss"
        />
      </el-form-item>
      <el-form-item label="起床时间">
        <el-date-picker
          v-model="editForm.wakeTime"
          type="datetime"
          placeholder="选择起床时间"
          format="YYYY-MM-DD HH:mm"
          value-format="YYYY-MM-DDTHH:mm:ss"
        />
      </el-form-item>
      <el-form-item label="睡眠质量">
        <el-rate
          v-model="editForm.qualityRating"
          :max="10"
          show-score
          text-color="#ff9900"
        />
      </el-form-item>
      <el-form-item label="备注">
        <el-input
          v-model="editForm.notes"
          type="textarea"
          :rows="2"
          placeholder="备注"
        />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="editDialogVisible = false">取消</el-button>
      <el-button type="primary" @click="submitEdit">保存</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed, onMounted, reactive, nextTick } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import {
  addSleepRecord as addSleepRecordAPI,
  getSleepRecords,
  updateSleepRecord,
  deleteSleepRecord as deleteSleepRecordAPI,
  getSleepStats,
} from "@/api/sleep.js";
import { useAuthStore } from "@/stores/auth.js";
import { Bicycle, Moon, Plus } from "@element-plus/icons-vue";
import * as echarts from "echarts";

let sleepChart = null;

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
const sleepChartRef = ref(null);

// 计算平均睡眠时长
const avgDuration = computed(() => {
  if (sleepRecords.value.length === 0) return 0;
  const total = sleepRecords.value.reduce(
    (sum, record) => sum + record.duration_hours,
    0
  );
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
      description:
        "您的平均睡眠时长低于推荐标准，建议保持7-9小时睡眠以获得最佳休息效果。",
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
  if (!dateTimeStr) return "-";
  const date = new Date(dateTimeStr);
  return date.toLocaleString("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
};

// 格式化日期
const formatDate = (dateTimeStr) => {
  if (!dateTimeStr) return "-";
  const date = new Date(dateTimeStr);
  return date.toLocaleDateString("zh-CN");
};

// 获取睡眠时长颜色
const getDurationColor = (duration) => {
  if (duration >= 7 && duration <= 9) return "success";
  if (duration >= 6 && duration < 7) return "warning";
  if (duration > 9) return "info";
  return "danger";
};

// 初始化图表
const initSleepChart = (dates = [], hours = [], isAverageFlags = []) => {
  const chartDom = sleepChartRef.value;
  if (!chartDom) return;

  if (!sleepChart) {
    sleepChart = echarts.init(chartDom);
    window.addEventListener('resize', () => sleepChart.resize());
  }

  // 计算最大值，保证最大值至少是10，超过则取最大值的上取整
  const maxHour = Math.max(...hours);
  const yAxisMax = maxHour > 10 ? Math.ceil(maxHour) : 10;

  const option = {
    tooltip: {
      trigger: 'axis',
      formatter: params => {
        const p = params[0];
        const avgFlag = isAverageFlags[p.dataIndex];
        return `${p.axisValue}<br/>睡眠时长: ${p.data} 小时` + (avgFlag ? '（无记录，使用平均值）' : '');
      }
    },
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'category', data: dates },
    yAxis: {
      type: 'value',
      name: '小时',
      min: 0,
      max: yAxisMax
    },
    series: [
      {
        name: '睡眠时长',
        type: 'line',
        smooth: true,
        data: hours,
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: {
          color: params => (isAverageFlags[params.dataIndex] ? '#FFA500' : '#1890ff'), // 平均值点橙色，真实记录蓝色
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(24,144,255,0.5)' },
            { offset: 1, color: 'rgba(24,144,255,0.1)' }
          ])
        }
      }
    ]
  };

  sleepChart.setOption(option);
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
    sleepRecords.value = []; // 确保设置为空数组而不是undefined
  } finally {
    tableLoading.value = false;
  }
};

const loadSleepStats = async () => {
  if (!authStore.userId) return;

  try {
    if (sleepRecords.value && sleepRecords.value.length > 0) {
      // 按日期排序，找最新日期
      const sortedRecords = sleepRecords.value.slice().sort((a, b) => new Date(a.sleep_time) - new Date(b.sleep_time));
      const latestDate = new Date(sortedRecords[sortedRecords.length - 1].sleep_time);

      // 生成最近7天日期数组（从最新日期往前推）
      const dateList = [];
      for (let i = 6; i >= 0; i--) {
        const d = new Date(latestDate);
        d.setDate(d.getDate() - i);
        dateList.push(d);
      }

      const formatDate = d => {
        const y = d.getFullYear();
        const m = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        return `${y}-${m}-${day}`;
      };

      // 只筛选最近7天有记录的条目
      const recent7Records = sortedRecords.filter(r => {
        const recDate = r.sleep_time.slice(0, 10);
        return dateList.some(d => formatDate(d) === recDate);
      });

      // 计算最近7天有记录的平均睡眠时长
      const totalDuration = recent7Records.reduce((sum, r) => sum + r.duration_hours, 0);
      const avgDuration = recent7Records.length > 0 ? totalDuration / recent7Records.length : 0;

      // 构造图表数据
      const dates = [];
      const hours = [];
      const isAverageFlags = [];

      dateList.forEach(d => {
        const dateStr = formatDate(d);
        // 找最近7天记录中是否有这天的睡眠数据
        const record = recent7Records.find(r => r.sleep_time.startsWith(dateStr));

        dates.push(d.toLocaleDateString('zh-CN', { weekday: 'short' }));
        if (record) {
          hours.push(record.duration_hours);
          isAverageFlags.push(false);
        } else {
          hours.push(parseFloat(avgDuration.toFixed(2)));
          isAverageFlags.push(true);
        }
      });

      initSleepChart(dates, hours, isAverageFlags);

      // 统计数据只用最近7天的记录
      sleepStats.value = {
        total_records: recent7Records.length,
        average_duration: avgDuration,
        average_quality: 0,
        best_sleep: recent7Records.reduce((best, cur) => (cur.duration_hours > (best?.duration_hours || 0) ? cur : best), null),
        worst_sleep: recent7Records.reduce((worst, cur) => (cur.duration_hours < (worst?.duration_hours || Infinity) ? cur : worst), null)
      };
    }
  } catch (error) {
    console.error("加载睡眠统计失败:", error);
    sleepStats.value = {
      total_records: 0,
      average_duration: 0,
      average_quality: 0,
      best_sleep: null,
      worst_sleep: null,
    };
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

const editDialogVisible = ref(false);
const editForm = reactive({
  id: null,
  sleepTime: null,
  wakeTime: null,
  qualityRating: 5,
  notes: "",
});

const editRecord = (record) => {
  editForm.id = record.id;
  editForm.sleepTime = record.sleep_time;
  editForm.wakeTime = record.wake_time;
  editForm.qualityRating = record.quality_rating;
  editForm.notes = record.notes;
  editDialogVisible.value = true;
};

const submitEdit = async () => {
  try {
    const updateData = {
      sleep_time: editForm.sleepTime,
      wake_time: editForm.wakeTime,
      quality_rating: editForm.qualityRating,
      notes: editForm.notes,
    };

    await updateSleepRecord(editForm.id, updateData);
    ElMessage.success("记录更新成功");
    editDialogVisible.value = false;
    await loadSleepRecords();
    await loadSleepStats();
  } catch (error) {
    ElMessage.error(error.message || "更新失败");
  }
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
