<template>
  <Layout>
    <div class="diet-page">
      <!-- 添加饮食记录 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card title="添加饮食记录" style="height: 100%;">
              <el-form :model="dietForm" label-width="100px">
                <el-row :gutter="20">
                  <el-col :span="8">
                    <el-form-item label="食物名称">
                      <el-input
                        v-model="dietForm.foodName"
                        placeholder="请输入食物名称"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item label="卡路里">
                      <el-input-number
                        v-model="dietForm.calories"
                        :min="0"
                        :max="5000"
                        placeholder="卡路里"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item label="份量">
                      <el-input-number
                        v-model="dietForm.quantity"
                        :min="0.1"
                        :max="10"
                        :precision="1"
                        placeholder="份量"
                      />
                    </el-form-item>
                  </el-col>
                </el-row>

                <el-row :gutter="20">
                  <el-col :span="8">
                    <el-form-item label="餐次">
                      <el-select v-model="dietForm.mealType" placeholder="选择餐次">
                        <el-option label="早餐" value="breakfast" />
                        <el-option label="午餐" value="lunch" />
                        <el-option label="晚餐" value="dinner" />
                        <el-option label="加餐" value="snack" />
                      </el-select>
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item label="时间">
                      <el-time-picker
                        v-model="dietForm.time"
                        placeholder="选择时间"
                        format="HH:mm"
                      />
                    </el-form-item>
                  </el-col>
                  <el-col :span="8">
                    <el-form-item>
                      <el-button type="primary" @click="addRecord" :loading="loading">
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

      <!-- 今日饮食记录 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card title="今日饮食记录" style="height: 100%;">
              <div class="header-actions">
                <el-tag type="success">总卡路里: {{ totalCalories }} kcal</el-tag>
                <el-tag type="info">记录数: {{ todayRecords.length }}</el-tag>
              </div>
              <el-table :data="todayRecords" style="width: 100%" v-loading="tableLoading">
                <el-table-column prop="content" label="食物名称" />
                <el-table-column prop="calories" label="卡路里" width="100">
                  <template #default="scope">
                    {{ scope.row.calories }} kcal
                  </template>
                </el-table-column>
                <el-table-column prop="meal_type" label="餐次" width="100">
                  <template #default="scope">
                    <el-tag :type="getMealTypeColor(scope.row.meal_type)">
                      {{ getMealTypeLabel(scope.row.meal_type) }}
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column prop="date" label="日期" width="120">
                  <template #default="scope">
                    {{ formatDate(scope.row.date) }}
                  </template>
                </el-table-column>
                <el-table-column label="操作" width="120">
                  <template #default="scope">
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

      <!-- 营养分析 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex;">
          <a-col :span="24">
            <a-card title="营养分析" style="height: 100%;">
              <el-row :gutter="20">
                <el-col :span="6">
                  <div class="nutrition-item">
                    <div class="nutrition-label">蛋白质</div>
                    <div class="nutrition-value">{{ nutrition.protein }}g</div>
                    <el-progress :percentage="nutrition.proteinPercent" />
                  </div>
                </el-col>
                <el-col :span="6">
                  <div class="nutrition-item">
                    <div class="nutrition-label">碳水化合物</div>
                    <div class="nutrition-value">{{ nutrition.carbs }}g</div>
                    <el-progress :percentage="nutrition.carbsPercent" />
                  </div>
                </el-col>
                <el-col :span="6">
                  <div class="nutrition-item">
                    <div class="nutrition-label">脂肪</div>
                    <div class="nutrition-value">{{ nutrition.fat }}g</div>
                    <el-progress :percentage="nutrition.fatPercent" />
                  </div>
                </el-col>
                <el-col :span="6">
                  <div class="nutrition-item">
                    <div class="nutrition-label">纤维</div>
                    <div class="nutrition-value">{{ nutrition.fiber }}g</div>
                    <el-progress :percentage="nutrition.fiberPercent" />
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
import { ref, computed, onMounted } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import Layout from "@/components/Layout.vue";
import {Plus} from "@element-plus/icons-vue";
import { addDietRecord, getDietRecords, deleteDietRecord, getDietStats } from '@/api/diet';
import { useAuthStore } from "@/stores/auth.js";

const authStore = useAuthStore();

const dietForm = ref({
  foodName: "",
  calories: 0,
  quantity: 1,
  mealType: "",
  time: null,
});

const todayRecords = ref([]);
const loading = ref(false);
const tableLoading = ref(false);

const totalCalories = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.calories, 0);
});

const fetchDietRecords = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  tableLoading.value = true;
  try {
    const response = await getDietRecords(authStore.userId, { limit: 30 });
    todayRecords.value = response.data || [];
  } catch (error) {
    ElMessage.error(error.message || "获取饮食记录失败");
    todayRecords.value = []; // 确保设置为空数组而不是undefined
  } finally {
    tableLoading.value = false;
  }
};

const addRecord = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  if (!dietForm.value.foodName || !dietForm.value.calories || !dietForm.value.mealType) {
    ElMessage.warning("请填写完整的饮食信息");
    return;
  }

  loading.value = true;
  try {
    const newRecord = {
      user_id: authStore.userId,
      meal_type: dietForm.value.mealType,
      content: dietForm.value.foodName,
      calories: dietForm.value.calories,
      date: new Date().toISOString().split('T')[0],
    };
    
    await addDietRecord(newRecord);
    
    // 重置表单
    dietForm.value = {
      foodName: "",
      calories: 0,
      quantity: 1,
      mealType: "",
      time: null,
    };
    
    ElMessage.success('饮食记录添加成功');
    await fetchDietRecords();
  } catch (error) {
    ElMessage.error(error.message || '添加饮食记录失败');
  } finally {
    loading.value = false;
  }
};

const deleteRecord = async (recordId) => {
  try {
    await ElMessageBox.confirm("确定要删除这条饮食记录吗？", "确认删除", {
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      type: "warning",
    });

    await deleteDietRecord(recordId);
    ElMessage.success('记录删除成功');
    await fetchDietRecords();
  } catch (error) {
    if (error !== "cancel") {
      ElMessage.error(error.message || '删除记录失败');
    }
  }
};

const nutrition = computed(() => {
  // 模拟营养数据
  return {
    protein: 45,
    carbs: 120,
    fat: 35,
    fiber: 15,
    proteinPercent: 75,
    carbsPercent: 60,
    fatPercent: 70,
    fiberPercent: 50,
  };
});

const getMealTypeColor = (type) => {
  const colors = {
    breakfast: "success",
    lunch: "warning",
    dinner: "danger",
    snack: "info",
  };
  return colors[type] || "info";
};

const getMealTypeLabel = (type) => {
  const labels = {
    breakfast: "早餐",
    lunch: "午餐",
    dinner: "晚餐",
    snack: "加餐",
  };
  return labels[type] || type;
};

const formatDate = (dateStr) => {
  if (!dateStr) return '-';
  const date = new Date(dateStr);
  return date.toLocaleDateString('zh-CN');
};

onMounted(() => {
  fetchDietRecords();
});
</script>

<style scoped>
.diet-page {
  padding: 0;
}

.header-actions {
  display: flex;
  gap: 10px;
}

.nutrition-item {
  text-align: center;
  padding: 15px;
}

.nutrition-label {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.nutrition-value {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}
</style>
