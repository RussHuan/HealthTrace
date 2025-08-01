<template>
  <Layout>
    <div class="profile-page">
      <el-row :gutter="20">
        <!-- 个人信息 -->
        <el-col :span="8">
          <el-card class="profile-card">
            <template #header>
              <div class="card-header">
                <span>个人信息</span>
              </div>
            </template>

            <div class="profile-info">
              <div class="avatar-section">
                <el-avatar :size="100" icon="User" />
                <h3>{{ authStore.user?.username }}</h3>
                <p class="user-id">用户ID: {{ authStore.user?.id }}</p>
              </div>

              <el-divider />

              <div class="info-item">
                <label>注册时间:</label>
                <span>{{ registerDate }}</span>
              </div>

              <div class="info-item">
                <label>最后登录:</label>
                <span>{{ lastLoginDate }}</span>
              </div>

              <div class="info-item">
                <label>账户状态:</label>
                <el-tag type="success">正常</el-tag>
              </div>
            </div>
          </el-card>
        </el-col>

        <!-- 健康目标设置 -->
        <el-col :span="16">
          <el-card class="goals-card">
            <template #header>
              <div class="card-header">
                <span>健康目标设置</span>
              </div>
            </template>

            <el-form :model="healthGoals" label-width="120px">
              <el-row :gutter="20">
                <el-col :span="12">
                  <el-form-item label="每日卡路里目标">
                    <el-input-number
                      v-model="healthGoals.dailyCalories"
                      :min="1000"
                      :max="5000"
                      placeholder="卡路里"
                    />
                  </el-form-item>
                </el-col>
                <el-col :span="12">
                  <el-form-item label="每日运动时长">
                    <el-input-number
                      v-model="healthGoals.dailyExercise"
                      :min="10"
                      :max="300"
                      placeholder="分钟"
                    />
                  </el-form-item>
                </el-col>
              </el-row>

              <el-row :gutter="20">
                <el-col :span="12">
                  <el-form-item label="每日睡眠时长">
                    <el-input-number
                      v-model="healthGoals.dailySleep"
                      :min="6"
                      :max="12"
                      :precision="1"
                      placeholder="小时"
                    />
                  </el-form-item>
                </el-col>
                <el-col :span="12">
                  <el-form-item label="每日饮水量">
                    <el-input-number
                      v-model="healthGoals.dailyWater"
                      :min="500"
                      :max="5000"
                      placeholder="毫升"
                    />
                  </el-form-item>
                </el-col>
              </el-row>

              <el-row :gutter="20">
                <el-col :span="12">
                  <el-form-item label="每周运动天数">
                    <el-input-number
                      v-model="healthGoals.weeklyExerciseDays"
                      :min="1"
                      :max="7"
                      placeholder="天"
                    />
                  </el-form-item>
                </el-col>
                <el-col :span="12">
                  <el-form-item label="体重目标">
                    <el-input-number
                      v-model="healthGoals.targetWeight"
                      :min="30"
                      :max="200"
                      :precision="1"
                      placeholder="公斤"
                    />
                  </el-form-item>
                </el-col>
              </el-row>

              <el-form-item>
                <el-button type="primary" @click="saveGoals">
                  <el-icon><Check /></el-icon>
                  保存目标
                </el-button>
                <el-button @click="resetGoals">
                  <el-icon><Refresh /></el-icon>
                  重置
                </el-button>
              </el-form-item>
            </el-form>
          </el-card>
        </el-col>
      </el-row>

      <!-- 健康数据概览 -->
      <el-card class="overview-card">
        <template #header>
          <div class="card-header">
            <span>健康数据概览</span>
          </div>
        </template>

        <el-row :gutter="20">
          <el-col :span="6">
            <div class="overview-item">
              <div class="overview-icon">
                <el-icon><Calendar /></el-icon>
              </div>
              <div class="overview-content">
                <h4>使用天数</h4>
                <p class="overview-value">{{ overview.usageDays }} 天</p>
              </div>
            </div>
          </el-col>

          <el-col :span="6">
            <div class="overview-item">
              <div class="overview-icon">
                <el-icon><Food /></el-icon>
              </div>
              <div class="overview-content">
                <h4>记录饮食</h4>
                <p class="overview-value">{{ overview.dietRecords }} 次</p>
              </div>
            </div>
          </el-col>

          <el-col :span="6">
            <div class="overview-item">
              <div class="overview-icon">
                <el-icon><Bicycle /></el-icon>
              </div>
              <div class="overview-content">
                <h4>记录运动</h4>
                <p class="overview-value">{{ overview.exerciseRecords }} 次</p>
              </div>
            </div>
          </el-col>

          <el-col :span="6">
            <div class="overview-item">
              <div class="overview-icon">
                <el-icon><Moon /></el-icon>
              </div>
              <div class="overview-content">
                <h4>记录睡眠</h4>
                <p class="overview-value">{{ overview.sleepRecords }} 次</p>
              </div>
            </div>
          </el-col>
        </el-row>
      </el-card>

      <!-- 账户设置 -->
      <el-card class="settings-card">
        <template #header>
          <div class="card-header">
            <span>账户设置</span>
          </div>
        </template>

        <el-row :gutter="20">
          <el-col :span="12">
            <h4>修改密码</h4>
            <el-form :model="passwordForm" label-width="100px">
              <el-form-item label="当前密码">
                <el-input
                  v-model="passwordForm.currentPassword"
                  type="password"
                  show-password
                  placeholder="请输入当前密码"
                />
              </el-form-item>
              <el-form-item label="新密码">
                <el-input
                  v-model="passwordForm.newPassword"
                  type="password"
                  show-password
                  placeholder="请输入新密码"
                />
              </el-form-item>
              <el-form-item label="确认密码">
                <el-input
                  v-model="passwordForm.confirmPassword"
                  type="password"
                  show-password
                  placeholder="请再次输入新密码"
                />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="changePassword">
                  修改密码
                </el-button>
              </el-form-item>
            </el-form>
          </el-col>

          <el-col :span="12">
            <h4>数据管理</h4>
            <div class="data-actions">
              <el-button type="warning" @click="exportData">
                <el-icon><Download /></el-icon>
                导出数据
              </el-button>
              <el-button type="danger" @click="clearData">
                <el-icon><Delete /></el-icon>
                清空数据
              </el-button>
            </div>

            <el-divider />

            <h4>账户操作</h4>
            <div class="account-actions">
              <el-button type="danger" @click="deleteAccount">
                <el-icon><Warning /></el-icon>
                删除账户
              </el-button>
            </div>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </Layout>
</template>

<script setup>
import { ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

// 模拟数据
const registerDate = ref("2024-01-15");
const lastLoginDate = ref("2024-01-20 14:30");

const healthGoals = ref({
  dailyCalories: 2000,
  dailyExercise: 30,
  dailySleep: 8,
  dailyWater: 2000,
  weeklyExerciseDays: 5,
  targetWeight: 65,
});

const overview = ref({
  usageDays: 15,
  dietRecords: 45,
  exerciseRecords: 28,
  sleepRecords: 15,
});

const passwordForm = ref({
  currentPassword: "",
  newPassword: "",
  confirmPassword: "",
});

const saveGoals = () => {
  ElMessage.success("健康目标保存成功");
};

const resetGoals = () => {
  healthGoals.value = {
    dailyCalories: 2000,
    dailyExercise: 30,
    dailySleep: 8,
    dailyWater: 2000,
    weeklyExerciseDays: 5,
    targetWeight: 65,
  };
  ElMessage.info("目标已重置为默认值");
};

const changePassword = () => {
  if (!passwordForm.value.currentPassword || !passwordForm.value.newPassword) {
    ElMessage.warning("请填写完整的密码信息");
    return;
  }

  if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
    ElMessage.error("两次输入的新密码不一致");
    return;
  }

  ElMessage.success("密码修改成功");
  passwordForm.value = {
    currentPassword: "",
    newPassword: "",
    confirmPassword: "",
  };
};

const exportData = () => {
  ElMessage.success("数据导出成功");
};

const clearData = async () => {
  try {
    await ElMessageBox.confirm(
      "确定要清空所有健康数据吗？此操作不可恢复！",
      "警告",
      {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }
    );
    ElMessage.success("数据已清空");
  } catch {
    // 用户取消
  }
};

const deleteAccount = async () => {
  try {
    await ElMessageBox.confirm(
      "确定要删除账户吗？此操作不可恢复！",
      "危险操作",
      {
        confirmButtonText: "确定删除",
        cancelButtonText: "取消",
        type: "error",
      }
    );
    ElMessage.success("账户已删除");
    authStore.logout();
  } catch {
    // 用户取消
  }
};
</script>

<style scoped>
.profile-page {
  padding: 0;
}

.profile-card {
  margin-bottom: 20px;
}

.goals-card {
  margin-bottom: 20px;
}

.overview-card {
  margin-bottom: 20px;
}

.settings-card {
  margin-bottom: 20px;
}

.card-header {
  font-weight: bold;
  color: #333;
}

.profile-info {
  text-align: center;
}

.avatar-section {
  margin-bottom: 20px;
}

.avatar-section h3 {
  margin: 10px 0 5px 0;
  color: #333;
}

.user-id {
  color: #666;
  font-size: 14px;
  margin: 0;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}

.info-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
}

.info-item label {
  font-weight: bold;
  color: #666;
}

.overview-item {
  display: flex;
  align-items: center;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 10px;
}

.overview-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  color: white;
  font-size: 20px;
}

.overview-content h4 {
  margin: 0 0 5px 0;
  color: #666;
  font-size: 14px;
  font-weight: normal;
}

.overview-value {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.data-actions,
.account-actions {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

h4 {
  margin: 0 0 15px 0;
  color: #333;
  font-size: 16px;
}
</style>
