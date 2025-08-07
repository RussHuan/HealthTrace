<template>
  <Layout>
    <div class="profile-page">
      <!-- 健康设置卡片组合，与健康数据概览宽度保持一致 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-row :gutter="16">
              <!-- 个人信息 -->
              <a-col :xs="24" :md="8">
                <a-card title="个人信息" style="height: 100%;">
                  <div class="profile-info" style="text-align: center;">
                    <div class="avatar-section" style="margin-bottom: 16px;">
                      <el-avatar :size="100" icon="User" />
                      <h3 style="margin-top: 12px;">{{ authStore.user?.username || '未登录' }}</h3>
                      <p class="user-id" style="color: #888;">用户ID: {{ authStore.user?.id || 'N/A' }}</p>
                    </div>

                    <el-divider style="margin: 16px 0;" />

                    <div class="info-item">
                      <label>账户状态:</label>
                      <el-tag type="success">正常</el-tag>
                    </div>
                  </div>
                </a-card>
              </a-col>

              <!-- 健康目标设置 -->
              <a-col :xs="24" :md="16">
                <a-card title="健康目标设置" style="height: 100%;">
                  <el-form :model="healthGoals" label-width="120px">
                    <el-row :gutter="20">
                      <el-col :span="12">
                        <el-form-item label="每日卡路里目标">
                          <el-input-number v-model="healthGoals.dailyCalories" :min="1000" :max="5000" />
                        </el-form-item>
                      </el-col>
                      <el-col :span="12">
                        <el-form-item label="每日运动时长">
                          <el-input-number v-model="healthGoals.dailyExercise" :min="10" :max="300" />
                        </el-form-item>
                      </el-col>
                    </el-row>

                    <el-row :gutter="20">
                      <el-col :span="12">
                        <el-form-item label="每日睡眠时长">
                          <el-input-number v-model="healthGoals.dailySleep" :min="6" :max="12" :precision="1" />
                        </el-form-item>
                      </el-col>
                    </el-row>

                    <el-row :gutter="20">
                      <el-col :span="12">
                        <el-form-item label="每周运动天数">
                          <el-input-number v-model="healthGoals.weeklyExerciseDays" :min="1" :max="7" />
                        </el-form-item>
                      </el-col>
                      <el-col :span="12">
                        <el-form-item label="体重目标">
                          <el-input-number v-model="healthGoals.targetWeight" :min="30" :max="200" :precision="1" />
                        </el-form-item>
                      </el-col>
                    </el-row>

                    <el-form-item>
                      <el-button type="primary" @click="saveGoals">
                        <el-icon><Check /></el-icon> 保存目标
                      </el-button>
                      <el-button @click="resetGoals">
                        <el-icon><Refresh /></el-icon> 重置
                      </el-button>
                    </el-form-item>
                  </el-form>
                </a-card>
              </a-col>
            </a-row>
          </a-col>
        </a-row>
      </div>


      <!-- 账户设置 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card title="账户设置" style="height: 100%;">
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
            </a-card>
          </a-col>
        </a-row>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router"; // 导入 useRouter

// 导入 Element Plus 图标
import { Check, Refresh, Download, Delete, Warning, User } from "@element-plus/icons-vue";

const authStore = useAuthStore();
const router = useRouter(); // 初始化 router

const healthGoals = ref({
  dailyCalories: 2000,
  dailyExercise: 30,
  dailySleep: 8,
  dailyWater: 2000, // 确保与 resetGoals 中的默认值一致
  weeklyExerciseDays: 5,
  targetWeight: 65,
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

// 修改密码功能
const changePassword = async () => {
  if (!passwordForm.value.currentPassword || !passwordForm.value.newPassword || !passwordForm.value.confirmPassword) {
    ElMessage.warning("请填写完整的密码信息");
    return;
  }

  if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
    ElMessage.error("两次输入的新密码不一致");
    return;
  }

  if (passwordForm.value.newPassword.length < 6) {
    ElMessage.error("新密码长度不能少于6位");
    return;
  }

  try {
    const result = await authStore.changePassword(
      passwordForm.value.currentPassword,
      passwordForm.value.newPassword
    );

    if (result.success) {
      ElMessage.success(result.message || "密码修改成功");
      // 清空表单
      passwordForm.value = {
        currentPassword: "",
        newPassword: "",
        confirmPassword: "",
      };
    } else {
      ElMessage.error(result.message || "密码修改失败");
    }
  } catch (error) {
    console.error("修改密码时发生错误:", error);
    ElMessage.error("修改密码失败，请稍后重试");
  }
};

// 导出数据功能
const exportData = async () => {
  try {
    const result = await authStore.exportUserData();
    if (result.success) {
      // 创建 Blob 对象并下载
      const blob = new Blob([JSON.stringify(result.data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `healthtrace_data_${authStore.user?.username || 'user'}_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url); // 释放 URL 对象
      ElMessage.success(result.message || "数据导出成功");
    } else {
      ElMessage.error(result.message || "数据导出失败");
    }
  } catch (error) {
    console.error("导出数据时发生错误:", error);
    ElMessage.error("数据导出失败，请稍后重试");
  }
};

// 清空数据功能 (目前仅为前端模拟，实际需要后端支持)
const clearData = async () => {
  try {
    await ElMessageBox.confirm(
      "确定要清空所有健康数据吗？此操作不可恢复！此功能目前仅为前端模拟，实际清空需要后端支持。",
      "警告",
      {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }
    );
    // 在实际应用中，这里会调用后端 API 来清空数据
    ElMessage.success("数据已清空 (前端模拟)");
  } catch {
    // 用户取消操作
    ElMessage.info("已取消清空数据");
  }
};

// 删除账户功能
const deleteAccount = async () => {
  try {
    // 第一次确认：要求用户输入密码
    const { value: password } = await ElMessageBox.prompt('请输入您的密码以确认删除账户', '确认删除', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      inputType: 'password',
      inputPlaceholder: '请输入密码',
      inputValidator: (value) => {
        if (!value) return '密码不能为空';
        if (value.length < 6) return '密码长度不能少于6位';
        return true;
      },
      inputErrorMessage: '密码格式不正确',
    });

    // 如果用户输入了密码并点击了确定
    if (password) {
      // 第二次确认：最终确认删除
      await ElMessageBox.confirm(
        "确定要删除账户吗？此操作不可恢复！您的所有数据将被永久删除。",
        "危险操作",
        {
          confirmButtonText: "确定删除",
          cancelButtonText: "取消",
          type: "error",
        }
      );

      // 调用 store 中的删除账户 action
      const result = await authStore.deleteAccount(password);

      if (result.success) {
        ElMessage.success(result.message || "账户已删除");
        // authStore.logout() 已在 store 的 deleteAccount action 中调用
        router.push("/login"); // 删除成功后跳转到登录页
      } else {
        ElMessage.error(result.message || "账户删除失败");
      }
    } else {
      ElMessage.info("已取消删除账户");
    }
  } catch (error) {
    // 捕获 ElMessageBox.prompt 或 ElMessageBox.confirm 的取消操作
    if (error === 'cancel') {
      ElMessage.info("已取消删除账户");
    } else {
      console.error("删除账户时发生错误:", error);
      ElMessage.error("删除账户失败，请稍后重试");
    }
  }
};

onMounted(() => {
  // fetchDietStats(); // 如果需要，可以保留或移除
});
</script>

<style scoped>
/* 样式保持不变 */
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
