<template>
  <Layout>
    <div class="dashboard">
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
                    运动时长
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
                    睡眠时长
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

          <!-- 饮水量，xs和sm屏隐藏 -->
          <a-col :xs="0" :sm="0" :md="6" style="height: 140px;" class="hide-sm-xs">
            <a-card :bordered="false" style="height: 100%; display: flex; align-items: center; min-width: 0;">
              <div style="display: flex; align-items: center; width: 100%; min-width: 0;">
                <div style="font-size: 32px; color: #1890ff; margin-right: 12px; flex-shrink: 0;">
                  <el-icon><IceDrink /></el-icon>
                </div>
                <div style="display: flex; flex-direction: column; overflow: hidden; min-width: 0;">
                  <h3 style="margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    饮水量
                  </h3>
                  <p style="margin: 0; font-weight: bold; font-size: 26px; line-height: 1.4;
                            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                    {{ todayWater }} ml
                  </p>
                  <p style="margin: 0; color: #888; font-size: 14px; white-space: nowrap;
                            overflow: hidden; text-overflow: ellipsis;">
                    目标: 2000 ml
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
            <a-card :loading="true" title="本周卡路里摄入" style="height: 100%;">
              <template #extra><router-link to="/diet">详情</router-link></template>
              <p>card content</p>
              <p>card content</p>
              <p>card content</p>
            </a-card>
          </a-col>

          <a-col :span="12" style="height: 300px;">
            <a-card :loading="true" title="运动趋势" style="height: 100%;">
              <template #extra><router-link to="exercise">详情</router-link></template>
              <p>card content</p>
              <p>card content</p>
              <p>card content</p>
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
import { ref } from "vue";
import Layout from "@/components/Layout.vue";
import {Food, Bicycle, Moon, IceDrink, Plus} from "@element-plus/icons-vue";

// 模拟数据
const todayCalories = ref(1450);
const todayExercise = ref(25);
const lastNightSleep = ref(7.5);
const todayWater = ref(1800);
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

/* 你已有样式保持不变 */
</style>
