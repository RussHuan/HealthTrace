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
          <!-- 今日卡路里，手机极窄屏时占满一行 -->
          <a-col :xs="24" :sm="12" :md="6" style="height: 140px;">
            <a-card :bordered="false" style="height: 100%; display: flex; align-items: center; min-width: 0;">
              <div style="display: flex; align-items: center; width: 100%; min-width: 0;">
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
            </a-card>
          </a-col>

          <!-- 运动时长，xs屏隐藏 -->
          <a-col :xs="0" :sm="12" :md="6" style="height: 140px;" class="hide-xs">
            <a-card :bordered="false" style="height: 100%; display: flex; align-items: center; min-width: 0;">
              <div style="display: flex; align-items: center; width: 100%; min-width: 0;">
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
            </a-card>
          </a-col>

          <!-- 睡眠时长，xs和sm屏隐藏 -->
          <a-col :xs="0" :sm="0" :md="6" style="height: 140px;" class="hide-sm-xs">
            <a-card :bordered="false" style="height: 100%; display: flex; align-items: center; min-width: 0;">
              <div style="display: flex; align-items: center; width: 100%; min-width: 0;">
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
            </a-card>
          </a-col>

        </a-row>
      </div>

      <!-- 图表区域 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="12" style="height: 300px;">
            <a-card :loading="chartLoading" title="本周卡路里摄入" style="height: 100%;">
              <template #extra><router-link to="/diet">详情</router-link></template>
              <div v-if="!chartLoading" style="height: 200px; display: flex; align-items: center; justify-content: center;">
                <p>本周总摄入: {{ weeklyCalories }} kcal</p>
              </div>
            </a-card>
          </a-col>

          <a-col :span="12" style="height: 300px;">
            <a-card :loading="chartLoading" title="运动趋势" style="height: 100%;">
              <template #extra><router-link to="/exercise">详情</router-link></template>
              <div v-if="!chartLoading" style="height: 200px; display: flex; align-items: center; justify-content: center;">
                <p>本周运动时长: {{ weeklyExercise }} 分钟</p>
              </div>
            </a-card>
          </a-col>
        </a-row>
      </div>

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
const chartLoading = ref(true);

// 加载统计数据
const loadDashboardData = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  chartLoading.value = true;
  try {
    // 并行加载所有统计数据
    const [dietStats, exerciseStats, sleepStats] = await Promise.all([
      getDietStats(authStore.userId, 1).catch(() => ({ data: { total_calories: 0 } })),
      getExerciseStats(authStore.userId, 1).catch(() => ({ data: { average_duration: 0, total_calories: 0 } })),
      getSleepStats(authStore.userId, 1).catch(() => ({ data: { average_duration: 0 } }))
    ]);

    // 设置今日数据
    todayCalories.value = dietStats.data?.total_calories || 0;
    todayExercise.value = Math.round(exerciseStats.data?.average_duration || 0);
    lastNightSleep.value = sleepStats.data?.average_duration || 0;
    todayWater.value = 1800; // 暂时使用固定值

    // 加载本周数据
    const [weeklyDietStats, weeklyExerciseStats] = await Promise.all([
      getDietStats(authStore.userId, 7).catch(() => ({ data: { total_calories: 0 } })),
      getExerciseStats(authStore.userId, 7).catch(() => ({ data: { average_duration: 0, total_calories: 0 } }))
    ]);

    weeklyCalories.value = weeklyDietStats.data?.total_calories || 0;
    weeklyExercise.value = Math.round(weeklyExerciseStats.data?.average_duration || 0);

  } catch (error) {
    console.error("加载仪表盘数据失败:", error);
    ElMessage.error("加载数据失败");
    // 设置默认值
    todayCalories.value = 0;
    todayExercise.value = 0;
    lastNightSleep.value = 0;
    todayWater.value = 1800;
    weeklyCalories.value = 0;
    weeklyExercise.value = 0;
  } finally {
    chartLoading.value = false;
  }
};

onMounted(() => {
  loadDashboardData();
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
