<template>
  <Layout>
    <div class="dashboard">
      <div style="padding: 20px;">
        <a-row :gutter="16">
          <a-col :span="24">
            <a-carousel autoplay effect="fade">
              <div>
                <img src="/images/banner1.jpg" alt="banner1" class="carousel-img">
              </div>
              <div>
                <img src="/images/banner2.jpg" alt="banner1" class="carousel-img">
              </div>
              <div>
                <img src="/images/banner3.jpg" alt="banner1" class="carousel-img">
              </div>
              <div class="developer-slide">
                <h3>关注我们：</h3>
                <div class="dev-links">
                  <a href="https://github.com/buuyii" target="_blank">
                    <GithubOutlined /> buuyii
                  </a>
                  <a href="https://github.com/Wh04m1777" target="_blank">
                    <GithubOutlined /> Wh04m1777
                  </a>
                  <a href="https://github.com/BaconToast-pro" target="_blank">
                    <GithubOutlined /> BaconToast-pro
                  </a>
                </div>
              </div>
            </a-carousel>
          </a-col>
        </a-row>
      </div>

      <!-- 统计卡片 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <!-- 今日卡路里 -->
          <a-col :span="8" style="height: 140px;">
            <a-card
              :bordered="false"
              style="height: 100%"
              :bodyStyle="{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                justifyContent: 'flex-start',
                minWidth: 0,
                height: '100%',
                padding: '0 12px',
                gap: '8px'
              }"
            >
              <!-- 左侧内容 -->
              <div style="display: flex; align-items: center; flex: 1; min-width: 0;">
                <div style="font-size: 32px; color: #1890ff; margin-right: 12px; flex-shrink: 0;">
                  <el-icon><Food /></el-icon>
                </div>
                <div style="display: flex; flex-direction: column; overflow: hidden; min-width: 0;">
                  <h3 style="margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    今日卡路里
                  </h3>
                  <p style="margin: 0; font-weight: bold; font-size: 26px; line-height: 1.4;
                            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    {{ todayCalories }} kcal
                  </p>
                  <p style="margin: 0; color: #888; font-size: 14px; white-space: nowrap;
                            overflow: hidden; text-overflow: ellipsis;">
                    目标: 2000 kcal
                  </p>
                </div>
              </div>

              <!-- 右侧圆环 -->
              <a-progress
                type="circle"
                :percent="Math.min((todayCalories / 2000) * 100, 100)"
                :width="60"
                :strokeWidth="8"
                strokeColor="#1890ff"
                style="flex-shrink: 0; margin-left: 12px;"
              />
            </a-card>
          </a-col>

          <!-- 今日运动时长 -->
          <a-col :span="8" style="height: 140px;">
            <a-card
              :bordered="false"
              style="height: 100%"
              :bodyStyle="{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                justifyContent: 'flex-start',
                minWidth: 0,
                height: '100%',
                padding: '0 12px',
                gap: '8px'
              }"
            >
              <!-- 左侧内容 -->
              <div style="display: flex; align-items: center; flex: 1; min-width: 0;">
                <div style="font-size: 32px; color: #1890ff; margin-right: 12px; flex-shrink: 0;">
                  <el-icon><Bicycle /></el-icon>
                </div>
                <div style="display: flex; flex-direction: column; overflow: hidden; min-width: 0;">
                  <h3 style="margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    今日运动时长
                  </h3>
                  <p style="margin: 0; font-weight: bold; font-size: 26px; line-height: 1.4;
                            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    {{ todayExercise }} 分钟
                  </p>
                  <p style="margin: 0; color: #888; font-size: 14px; white-space: nowrap;
                            overflow: hidden; text-overflow: ellipsis;">
                    目标: 30 分钟
                  </p>
                </div>
              </div>

              <!-- 右侧圆环 -->
              <a-progress
                type="circle"
                :percent="Math.min((todayExercise / 30) * 100, 100)"
                :width="60"
                :strokeWidth="8"
                strokeColor="#1890ff"
                style="flex-shrink: 0; margin-left: 12px;"
              />
            </a-card>
          </a-col>

          <!-- 今日睡眠时长 -->
          <a-col :span="8" style="height: 140px;">
            <a-card
              :bordered="false"
              style="height: 100%"
              :bodyStyle="{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                justifyContent: 'flex-start',
                minWidth: 0,
                height: '100%',
                padding: '0 12px',
                gap: '8px'
              }"
            >
              <!-- 左侧内容 -->
              <div style="display: flex; align-items: center; flex: 1; min-width: 0;">
                <div style="font-size: 32px; color: #1890ff; margin-right: 12px; flex-shrink: 0;">
                  <el-icon><Moon /></el-icon>
                </div>
                <div style="display: flex; flex-direction: column; overflow: hidden; min-width: 0;">
                  <h3 style="margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    今日睡眠时长
                  </h3>
                  <p style="margin: 0; font-weight: bold; font-size: 26px; line-height: 1.4;
                            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    {{ lastNightSleep }} 小时
                  </p>
                  <p style="margin: 0; color: #888; font-size: 14px; white-space: nowrap;
                            overflow: hidden; text-overflow: ellipsis;">
                    目标: 8 小时
                  </p>
                </div>
              </div>

              <!-- 右侧圆环 -->
              <a-progress
                type="circle"
                :percent="Math.min((lastNightSleep / 8) * 100, 100)"
                :width="60"
                :strokeWidth="8"
                strokeColor="#1890ff"
                style="flex-shrink: 0; margin-left: 12px;"
              />
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 健康周报 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card :bordered="false" style="height: 100%; padding: 20px;">
              <template #title>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span>健康周报</span>
                  <a-button size="small" type="primary" @click="dialogVisible = true">
                    配置AI参数
                  </a-button>
                </div>
              </template>

              <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 24px;">
                <div style="flex: 1; min-width: 180px; text-align: center;">
                  <h3>本周总摄入</h3>
                  <p style="font-size: 24px; font-weight: bold;">{{ weeklyCalories }} kcal</p>
                </div>
                <div style="flex: 1; min-width: 180px; text-align: center;">
                  <h3>本周运动时长</h3>
                  <p style="font-size: 24px; font-weight: bold;">{{ weeklyExercise }} 分钟</p>
                </div>
                <div style="flex: 1; min-width: 180px; text-align: center;">
                  <h3>本周平均睡眠</h3>
                  <p style="font-size: 24px; font-weight: bold;">{{ weeklySleep }} 小时</p>
                </div>
              </div>

              <div style="margin-top: 24px; color: #555;">
                <h4 style="display: flex; align-items: center; gap: 8px;">
                  健康建议
                  <span style="font-size: 14px; color: #999;">（来源：<a :href="apiUrl" target="_blank" style="color:#1890ff;">{{ apiUrl }}</a>）</span>
                </h4>
                <p v-if="llmAdvice" style="font-size: 16px; line-height: 1.5;">{{ llmAdvice }}</p>
                <p v-else style="font-size: 16px; color: #999;">正在加载建议...</p>
                <p style="margin-top: 8px; font-size: 12px; color: #d9534f;">
                  ⚠️ AI 提供的信息仅供参考，请结合实际情况甄别判断。
                </p>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 配置弹窗保持不变 -->
      <a-modal
        v-model:visible="dialogVisible"
        title="AI接口配置"
        ok-text="保存"
        cancel-text="取消"
        @ok="saveConfig"
      >
        <a-form layout="vertical">
          <a-form-item label="LLM API地址">
            <a-input
              v-model:value="tempApiUrl"
              placeholder="请输入LLM接口地址"
              allow-clear
            />
          </a-form-item>

          <a-form-item label="API Key">
            <a-input
              v-model:value="tempApiKey"
              placeholder="请输入API Key"
              type="password"
              allow-clear
            />
          </a-form-item>

          <a-form-item label="模型名称">
            <a-input
              v-model:value="tempModel"
              placeholder="例如 gpt-4o-mini"
              allow-clear
            />
          </a-form-item>
        </a-form>
      </a-modal>


      <!-- 快速操作 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card title="快速操作" style="height: 100%;">
              <div class="quick-actions" style="margin-top: 12px;">
                <el-button type="primary" @click="$router.push('/diet')">
                  <el-icon><Plus /></el-icon>
                  记录饮食
                </el-button>
                <el-button type="success" @click="$router.push('/exercise')">
                  <el-icon><Bicycle /></el-icon>
                  记录运动
                </el-button>
                <el-button type="info" @click="$router.push('/sleep')">
                  <el-icon><Moon /></el-icon>
                  记录睡眠
                </el-button>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { ElMessage } from "element-plus";
import Layout from "@/components/Layout.vue";
import {Food, Bicycle, Moon, IceDrink, Plus} from "@element-plus/icons-vue";
import { GithubOutlined } from '@ant-design/icons-vue';
import { useAuthStore } from "@/stores/auth.js";
import { getDietStats } from "@/api/diet.js";
import { getExerciseStats } from "@/api/exercise.js";
import { getSleepStats } from "@/api/sleep.js";

const authStore = useAuthStore();

// 统计数据
const todayCalories = ref(0);
const todayExercise = ref(0);
const lastNightSleep = ref(0);
const todayWater = ref(0);
const weeklyCalories = ref(0);
const weeklyExercise = ref(0);
const weeklySleep = ref(0);  // 新增响应式变量
const chartLoading = ref(true);
const llmAdvice = ref('');
const dialogVisible = ref(false);
const tempApiKey = ref('');         // 临时存储输入的API Key
const apiKey = ref(''); // 默认值或本地存储读取
const tempModel = ref('gpt-4o-mini');
const model = ref('gpt-4o-mini');
const tempApiUrl = ref('https://api.chatanywhere.tech/v1/chat/completions'); // 配置弹窗输入
const apiUrl = ref('https://api.chatanywhere.tech/v1/chat/completions');     // 默认值

function createPrompt(calories, exercise, sleep) {
  return `你是一名健康顾问。请根据以下每周数据生成简短的健康建议：
- 每周摄入热量：${calories} kcal
- 每周运动时长：${exercise} 分钟
- 每周平均睡眠时长：${sleep} 小时
请给出具体且易懂的建议。`;
}

function saveConfig() {
  if (tempApiKey.value.trim()) {
    apiKey.value = tempApiKey.value.trim();
    localStorage.setItem('apiKey', apiKey.value);
  }
  if (tempModel.value.trim()) {
    model.value = tempModel.value.trim();
    localStorage.setItem('model', model.value);
  }
  if (tempApiUrl.value.trim()) {
    apiUrl.value = tempApiUrl.value.trim();
    localStorage.setItem('apiUrl', apiUrl.value);
  }
  dialogVisible.value = false;

  // 配置变更后重新拉取建议
  loadLlmAdvice();
}

async function fetchAdvice(calories, exercise, sleep) {
  const prompt = createPrompt(calories, exercise, sleep);

  try {
    const fetchPromise = fetch(apiUrl.value, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey.value}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: model.value,
        messages: [{ role: "user", content: prompt }],
        max_tokens: 500
      })
    });

    const timeoutPromise = new Promise((_, reject) =>
      setTimeout(() => reject(new Error('请求超时')), 10000)
    );

    const response = await Promise.race([fetchPromise, timeoutPromise]);

    if (!response.ok) {
      throw new Error(`API请求失败，状态码：${response.status}`);
    }

    const data = await response.json();

    if (data.choices?.[0]?.message?.content) {
      llmAdvice.value = data.choices[0].message.content;
    } else {
      llmAdvice.value = '暂无建议';
    }
  } catch (error) {
    console.error("fetchAdvice 出错:", error);
    llmAdvice.value = '无法加载建议，请稍后重试。';
  }
}


// 加载统计数据
const loadDashboardData = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  chartLoading.value = true;
  try {
    // 并行加载今日统计数据
    const [dietStats, exerciseStats, sleepStats] = await Promise.all([
      getDietStats(authStore.userId, 1).catch(() => ({ data: { total_calories: 0 } })),
      getExerciseStats(authStore.userId, 1).catch(() => ({ data: { average_duration: 0, total_calories: 0 } })),
      getSleepStats(authStore.userId, 1).catch(() => ({ data: { average_duration: 0 } }))
    ]);

    todayCalories.value = dietStats.data?.total_calories || 0;
    todayExercise.value = Math.round(exerciseStats.data?.average_duration || 0);
    lastNightSleep.value = sleepStats.data?.average_duration || 0;
    todayWater.value = 1800;

    // 并行加载本周统计数据
    const [weeklyDietStats, weeklyExerciseStats, weeklySleepStats] = await Promise.all([
      getDietStats(authStore.userId, 7).catch(() => ({ data: { total_calories: 0 } })),
      getExerciseStats(authStore.userId, 7).catch(() => ({ data: { average_duration: 0, total_calories: 0 } })),
      getSleepStats(authStore.userId, 7).catch(() => ({ data: { average_duration: 0 } }))
    ]);

    weeklyCalories.value = weeklyDietStats.data?.total_calories || 0;
    weeklyExercise.value = Math.round(weeklyExerciseStats.data?.average_duration || 0);
    weeklySleep.value = weeklySleepStats.data?.average_duration || 0;
    await loadLlmAdvice();
  } catch (error) {
    console.error("加载仪表盘数据失败:", error);
    ElMessage.error("加载数据失败");
    todayCalories.value = 0;
    todayExercise.value = 0;
    lastNightSleep.value = 0;
    todayWater.value = 1800;
    weeklyCalories.value = 0;
    weeklyExercise.value = 0;
    weeklySleep.value = 0;
  } finally {
    chartLoading.value = false;
  }
};

// 独立加载 LLM 建议
const loadLlmAdvice = async () => {
  try {
    // 这里根据你的实现调用 fetchAdvice，传入最新的周统计数据
    await fetchAdvice(weeklyCalories.value, weeklyExercise.value, weeklySleep.value);
  } catch (error) {
    console.error("加载健康建议失败:", error);
    llmAdvice.value = '无法加载建议，请稍后重试。';
  }
};

onMounted(() => {
  const savedKey = localStorage.getItem('apiKey');
  if (savedKey) apiKey.value = savedKey;

  const savedModel = localStorage.getItem('model');
  if (savedModel) model.value = savedModel;

  // 初始化临时输入框
  tempApiKey.value = apiKey.value;
  tempModel.value = model.value;

  loadDashboardData();  // 这里改成加载数据
});

</script>

<style scoped>
.dashboard {
  padding: 0;
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

:deep(.slick-slide) {
  text-align: center;
  background: #364d79;
  overflow: hidden;
}
:deep(.slick-slide h3) {
  color: #fff;
}

.dashboard {
  padding: 0;
}

.carousel-img {
  width: 100%;
  height: 200px; /* 可调 */
  object-fit: cover; /* 保证图片不变形 */
  display: block;
}

.developer-slide {
  background: #364d79;
  min-height: 200px;
  color: #fff;
  text-align: center;
  padding: 40px 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.developer-slide h3 {
  font-size: 22px;
  margin-bottom: 12px;
}

.dev-links {
  margin-top: 12px;
}

.dev-links a {
  display: inline-block;
  margin: 0 12px;
  font-size: 18px;
  color: #fff;
  text-decoration: underline;
}

.dev-links a:hover {
  color: #91d5ff;
}

</style>
