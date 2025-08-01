<template>
  <Layout>
    <div class="dashboard">
      <!-- 统计卡片 -->
      <el-row :gutter="20" class="stats-row">
        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon diet-icon">
                <el-icon><Food /></el-icon>
              </div>
              <div class="stat-info">
                <h3>今日卡路里</h3>
                <p class="stat-value">{{ todayCalories }} kcal</p>
                <p class="stat-target">目标: 2000 kcal</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon exercise-icon">
                <el-icon><Bicycle /></el-icon>
              </div>
              <div class="stat-info">
                <h3>运动时长</h3>
                <p class="stat-value">{{ todayExercise }} 分钟</p>
                <p class="stat-target">目标: 30 分钟</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon sleep-icon">
                <el-icon><Moon /></el-icon>
              </div>
              <div class="stat-info">
                <h3>睡眠时长</h3>
                <p class="stat-value">{{ lastNightSleep }} 小时</p>
                <p class="stat-target">目标: 8 小时</p>
              </div>
            </div>
          </el-card>
        </el-col>

        <el-col :span="6">
          <el-card class="stat-card">
            <div class="stat-content">
              <div class="stat-icon water-icon">
                <el-icon><WaterCup /></el-icon>
              </div>
              <div class="stat-info">
                <h3>饮水量</h3>
                <p class="stat-value">{{ todayWater }} ml</p>
                <p class="stat-target">目标: 2000 ml</p>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <!-- 图表区域 -->
      <el-row :gutter="20" class="charts-row">
        <el-col :span="12">
          <el-card class="chart-card">
            <template #header>
              <div class="card-header">
                <span>本周卡路里摄入</span>
              </div>
            </template>
            <div class="chart-placeholder">
              <el-empty description="图表功能开发中..." />
            </div>
          </el-card>
        </el-col>

        <el-col :span="12">
          <el-card class="chart-card">
            <template #header>
              <div class="card-header">
                <span>运动趋势</span>
              </div>
            </template>
            <div class="chart-placeholder">
              <el-empty description="图表功能开发中..." />
            </div>
          </el-card>
        </el-col>
      </el-row>

      <!-- 快速操作 -->
      <el-row :gutter="20" class="actions-row">
        <el-col :span="24">
          <el-card class="actions-card">
            <template #header>
              <div class="card-header">
                <span>快速操作</span>
              </div>
            </template>
            <div class="quick-actions">
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
          </el-card>
        </el-col>
      </el-row>
    </div>
  </Layout>
</template>

<script setup>
import { ref } from "vue";
import Layout from "@/components/Layout.vue";

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

.stats-row {
  margin-bottom: 20px;
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
}

.diet-icon {
  background: linear-gradient(135deg, #ff6b6b, #ee5a24);
}

.exercise-icon {
  background: linear-gradient(135deg, #4ecdc4, #44a08d);
}

.sleep-icon {
  background: linear-gradient(135deg, #a8edea, #fed6e3);
  color: #333;
}

.water-icon {
  background: linear-gradient(135deg, #74b9ff, #0984e3);
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

.charts-row {
  margin-bottom: 20px;
}

.chart-card {
  height: 300px;
}

.card-header {
  font-weight: bold;
  color: #333;
}

.chart-placeholder {
  height: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.actions-row {
  margin-bottom: 20px;
}

.quick-actions {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.quick-actions .el-button {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 12px 20px;
}
</style>
