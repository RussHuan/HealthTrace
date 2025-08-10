<template>
  <Layout>
    <div class="exercise-page">
      <!-- 运动统计 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <!-- 平均运动时长 -->
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
                    平均运动时长
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
                    {{ exerciseStats.average_duration || 0 }} 分钟
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
                    目标: 30 分钟
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>

          <!-- 总消耗卡路里 -->
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
                  <el-icon><HotWater /></el-icon>
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
                    总消耗卡路里
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
                    {{ exerciseStats.total_calories || 0 }} kcal
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
                    目标: 1000 kcal
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
                    {{ exerciseStats.total_records || 0 }} 条
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

          <!-- 最佳运动 -->
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
                    最佳运动
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
                      exerciseStats.best_exercise
                        ? exerciseStats.best_exercise.calories
                        : 0
                    }}
                    kcal
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
                      exerciseStats.best_exercise
                        ? formatDate(exerciseStats.best_exercise.start_time)
                        : "暂无"
                    }}
                  </p>
                </div>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 智能饮食推荐卡片 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card :bordered="false" style="min-height: 220px;">
              <template #title>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span>
                    智能饮食推荐
                    <span style="font-size: 14px; color: #999;">（来源：<a :href="dietApiUrl" target="_blank" style="color:#1890ff;">{{ dietApiUrl }}</a>）</span>
                  </span>
                  <a-button size="small" type="primary" @click="openDietConfig">
                    配置AI参数
                  </a-button>
                </div>
              </template>

              <div style="color: #555; min-height: 120px; white-space: pre-line; font-size: 16px; line-height: 1.5;">
                <p v-if="dietAdvice">{{ dietAdvice }}</p>
                <p v-else style="color: #999;">正在根据运动数据生成饮食推荐...</p>
              </div>

              <p style="margin-top: 8px; font-size: 12px; color: #d9534f;">
                ⚠️ AI 推荐仅供参考，请结合实际情况判断。
              </p>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 智能饮食推荐的AI配置弹窗 -->
      <a-modal
        v-model:visible="dietDialogVisible"
        title="AI接口配置"
        ok-text="保存"
        cancel-text="取消"
        @ok="saveDietConfig"
      >
        <a-form layout="vertical">
          <a-form-item label="LLM API地址">
            <a-input v-model:value="tempDietApiUrl" placeholder="请输入LLM接口地址" allow-clear />
          </a-form-item>
          <a-form-item label="API Key">
            <a-input v-model:value="tempDietApiKey" placeholder="请输入API Key" type="password" allow-clear />
          </a-form-item>
          <a-form-item label="模型名称">
            <a-input v-model:value="tempDietModel" placeholder="例如 gpt-4o-mini" allow-clear />
          </a-form-item>
        </a-form>
      </a-modal>

      <!-- 运动记录列表 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="运动记录列表" style="height: 100%">
              <div class="header-actions">
                <el-date-picker
                  v-model="dateRange"
                  type="daterange"
                  range-separator="至"
                  start-placeholder="开始日期"
                  end-placeholder="结束日期"
                  format="YYYY-MM-DD"
                  value-format="YYYY-MM-DD"
                  @change="loadExerciseRecords"
                  style="margin-right: 10px"
                />
                <el-tag type="success">总时长: {{ totalDuration }} 分钟</el-tag>
                <el-tag type="warning">消耗: {{ totalCalories }} kcal</el-tag>
                <el-tag type="info"
                  >记录数: {{ exerciseRecords.length }}</el-tag
                >
              </div>
              <el-table
                :data="exerciseRecords"
                style="width: 100%"
                v-loading="tableLoading"
              >
                <el-table-column prop="type" label="运动类型" width="120">
                  <template #default="scope">
                    <el-tag :type="getExerciseTypeColor(scope.row.type)">
                      {{ getExerciseTypeLabel(scope.row.type) }}
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column prop="start_time" label="开始时间" width="160">
                  <template #default="scope">
                    {{ formatDateTime(scope.row.start_time) }}
                  </template>
                </el-table-column>
                <el-table-column prop="end_time" label="结束时间" width="160">
                  <template #default="scope">
                    {{ formatDateTime(scope.row.end_time) }}
                  </template>
                </el-table-column>
                <el-table-column
                  prop="duration_mimutes"
                  label="时长"
                  width="100"
                >
                  <template #default="scope">
                    {{ scope.row.duration_mimutes }} 分钟
                  </template>
                </el-table-column>
                <el-table-column prop="calories" label="消耗卡路里" width="120">
                  <template #default="scope">
                    {{ scope.row.calories }} kcal
                  </template>
                </el-table-column>
                <el-table-column prop="notes" label="备注" min-width="200">
                  <template #default="scope">
                    {{ scope.row.notes || "-" }}
                  </template>
                </el-table-column>
                <el-table-column label="操作" width="150">
                  <template #default="scope">
<!--                    <el-button-->
<!--                      type="primary"-->
<!--                      size="small"-->
<!--                      @click="editRecord(scope.row)"-->
<!--                    >-->
<!--                      编辑-->
<!--                    </el-button>-->
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

      <!-- 添加运动记录 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="添加运动记录" style="height: 100%">
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
                    <el-form-item label="开始时间">
                      <el-date-picker
                        v-model="exerciseForm.startTime"
                        type="datetime"
                        placeholder="选择开始时间"
                        format="YYYY-MM-DD HH:mm"
                        value-format="YYYY-MM-DDTHH:mm:ss"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item label="结束时间">
                      <el-date-picker
                        v-model="exerciseForm.endTime"
                        type="datetime"
                        placeholder="选择结束时间"
                        format="YYYY-MM-DD HH:mm"
                        value-format="YYYY-MM-DDTHH:mm:ss"
                      />
                    </el-form-item>
                  </el-col>
                </el-row>

                <el-row :gutter="20">
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
                  <el-col :span="8">
                    <el-form-item label="备注">
                      <el-input
                        v-model="exerciseForm.notes"
                        placeholder="添加备注信息（可选）"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item>
                      <el-button
                        type="primary"
                        @click="addExerciseRecord"
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
    </div>
  </Layout>
  <el-dialog v-model="editDialogVisible" title="编辑运动记录" width="600px">
    <el-form :model="editForm" label-width="100px">
      <el-row :gutter="20">
        <el-col :span="12">
          <el-form-item label="运动类型">
            <el-select v-model="editForm.type" placeholder="选择运动类型">
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
        <el-col :span="12">
          <el-form-item label="卡路里">
            <el-input-number v-model="editForm.calories" :min="0" :max="2000" />
          </el-form-item>
        </el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :span="12">
          <el-form-item label="开始时间">
            <el-date-picker
              v-model="editForm.startTime"
              type="datetime"
              placeholder="开始时间"
              format="YYYY-MM-DD HH:mm"
              value-format="YYYY-MM-DDTHH:mm:ss"
            />
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="结束时间">
            <el-date-picker
              v-model="editForm.endTime"
              type="datetime"
              placeholder="结束时间"
              format="YYYY-MM-DD HH:mm"
              value-format="YYYY-MM-DDTHH:mm:ss"
            />
          </el-form-item>
        </el-col>
      </el-row>

      <el-form-item label="备注">
        <el-input v-model="editForm.notes" type="textarea" rows="2" />
      </el-form-item>
    </el-form>

    <template #footer>
      <el-button @click="editDialogVisible = false">取消</el-button>
      <el-button type="primary" @click="submitEdit">保存</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import {ref, computed, onMounted, watch} from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import { HotWater, Plus, Timer, Calendar, Star } from "@element-plus/icons-vue";
import {
  addExerciseRecord as addExerciseRecordAPI,
  getExerciseRecords,
  updateExerciseRecord,
  deleteExerciseRecord,
  getExerciseStats,
} from "@/api/exercise";
import { useAuthStore } from "@/stores/auth.js";

const authStore = useAuthStore();

const exerciseForm = ref({
  type: "",
  startTime: null,
  endTime: null,
  calories: 0,
  notes: "",
});

const exerciseRecords = ref([]);
const exerciseStats = ref({});
const loading = ref(false);
const tableLoading = ref(false);
const dateRange = ref([]);

const dietDialogVisible = ref(false);

const tempDietApiUrl = ref("");
const tempDietApiKey = ref("");
const tempDietModel = ref("");

const dietAdvice = ref('');
const dietApiKey = ref('');      // 你的API Key
const dietApiUrl = ref('https://api.chatanywhere.tech/v1/chat/completions');  // 接口地址
const dietModel = ref('gpt-4o-mini');  // 模型名

const openDietConfig = () => {
  tempDietApiUrl.value = dietApiUrl.value;
  tempDietApiKey.value = dietApiKey.value;
  tempDietModel.value = dietModel.value;
  dietDialogVisible.value = true;
};

// 计算总时长和总卡路里
const totalDuration = computed(() => {
  return exerciseRecords.value.reduce(
    (sum, record) => sum + (record.duration_mimutes || 0),
    0
  );
});

const totalCalories = computed(() => {
  return exerciseRecords.value.reduce(
    (sum, record) => sum + (record.calories || 0),
    0
  );
});

// 加载运动记录
const loadExerciseRecords = async () => {
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

    const response = await getExerciseRecords(authStore.userId, params);
    exerciseRecords.value = response.data || [];
  } catch (error) {
    ElMessage.error(error.message || "加载运动记录失败");
    exerciseRecords.value = []; // 确保设置为空数组而不是undefined
  } finally {
    tableLoading.value = false;
  }
};

// 加载运动统计
const loadExerciseStats = async () => {
  if (!authStore.userId) return;

  try {
    const response = await getExerciseStats(authStore.userId, 7);
    exerciseStats.value = response.data || {};
  } catch (error) {
    console.error("加载运动统计失败:", error);
    exerciseStats.value = {
      total_records: 0,
      average_duration: 0,
      total_calories: 0,
      best_exercise: null,
      worst_exercise: null,
    };
  }
};

// 添加运动记录
const addExerciseRecord = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  if (
    !exerciseForm.value.type ||
    !exerciseForm.value.startTime ||
    !exerciseForm.value.endTime
  ) {
    ElMessage.warning("请填写完整的运动信息");
    return;
  }

  loading.value = true;
  try {
    const exerciseData = {
      user_id: authStore.userId,
      type: exerciseForm.value.type,
      start_time: exerciseForm.value.startTime,
      end_time: exerciseForm.value.endTime,
      calories: exerciseForm.value.calories,
      notes: exerciseForm.value.notes || "",
    };

    await addExerciseRecordAPI(exerciseData);

    // 重置表单
    exerciseForm.value = {
      type: "",
      startTime: null,
      endTime: null,
      calories: 0,
      notes: "",
    };

    ElMessage.success("运动记录添加成功");

    // 重新加载数据
    await loadExerciseRecords();
    await loadExerciseStats();
  } catch (error) {
    ElMessage.error(error.message || "添加运动记录失败");
  } finally {
    loading.value = false;
  }
};

// 删除运动记录
const deleteRecord = async (recordId) => {
  try {
    await ElMessageBox.confirm("确定要删除这条运动记录吗？", "确认删除", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning",
    });

    await deleteExerciseRecord(recordId);
    ElMessage.success("运动记录删除成功");

    // 重新加载数据
    await loadExerciseRecords();
    await loadExerciseStats();
  } catch (error) {
    if (error !== "cancel") {
      ElMessage.error(error.message || "删除运动记录失败");
    }
  }
};

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

// 监听运动统计变化，自动刷新饮食推荐
watch(
  () => exerciseStats.value,
  async (newStats) => {
    if (newStats && dietApiUrl.value && dietApiKey.value && dietModel.value) {
      await loadDietAdvice(newStats);
    }
  },
  { immediate: true }
);

function createDietPrompt(stats) {
  return `你是饮食专家，请根据以下运动统计数据推荐合理的饮食计划，包含主要营养素摄入建议：
- 总运动时长：${stats.average_duration || 0} 分钟
- 总消耗卡路里：${stats.total_calories || 0} 千卡
- 备注：请给出具体且科学的饮食建议。`;
}

async function loadDietAdvice(stats) {
  if (!dietApiKey.value) {
    dietAdvice.value = '请先配置饮食推荐API Key';
    return;
  }

  dietAdvice.value = '';

  const prompt = createDietPrompt(stats);

  try {
    const fetchPromise = fetch(dietApiUrl.value, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${dietApiKey.value}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: dietModel.value,
        messages: [{ role: "user", content: prompt }],
        max_tokens: 1000,
      }),
    });

    // 设置超时10秒
    const timeoutPromise = new Promise((_, reject) =>
      setTimeout(() => reject(new Error('请求超时')), 10000)
    );

    const response = await Promise.race([fetchPromise, timeoutPromise]);

    if (!response.ok) {
      throw new Error(`接口请求失败，状态码：${response.status}`);
    }

    const data = await response.json();

    if (data.choices?.[0]?.message?.content) {
      dietAdvice.value = data.choices[0].message.content.trim();
    } else {
      dietAdvice.value = '暂无饮食建议';
    }
  } catch (error) {
    console.error("loadDietAdvice 出错:", error);
    dietAdvice.value = '获取饮食建议失败，请检查API配置或稍后重试。';
    ElMessage.error(dietAdvice.value);
  }
}

function saveDietConfig() {
  dietApiUrl.value = tempDietApiUrl.value.trim();
  dietApiKey.value = tempDietApiKey.value.trim();
  dietModel.value = tempDietModel.value.trim();

  localStorage.setItem('dietApiKey', dietApiKey.value);
  localStorage.setItem('dietApiUrl', dietApiUrl.value);
  localStorage.setItem('dietModel', dietModel.value);

  dietDialogVisible.value = false;

  if (exerciseStats.value) {
    loadDietAdvice(exerciseStats.value);
  }
}

onMounted(() => {
  tempDietApiKey.value = localStorage.getItem('dietApiKey') || '';
  dietApiKey.value = tempDietApiKey.value;

  tempDietApiUrl.value = localStorage.getItem('dietApiUrl') || 'https://api.chatanywhere.tech/v1/chat/completions';
  dietApiUrl.value = tempDietApiUrl.value;

  tempDietModel.value = localStorage.getItem('dietModel') || 'gpt-4o-mini';
  dietModel.value = tempDietModel.value;

  loadExerciseRecords();
  loadExerciseStats();
});


</script>

<style scoped>
.exercise-page {
  padding: 0;
}

.header-actions {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 15px;
}

.hide-xs {
  display: none;
}
@media (min-width: 576px) {
  .hide-xs {
    display: block;
  }
}

.hide-sm-xs {
  display: none;
}
@media (min-width: 768px) {
  .hide-sm-xs {
    display: block;
  }
}
</style>
