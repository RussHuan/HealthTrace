<template>
  <Layout>
    <div class="diet-page">
      <!-- 添加饮食记录 -->
      <el-card class="add-record-card">
        <template #header>
          <div class="card-header">
            <span>添加饮食记录</span>
          </div>
        </template>

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
                <el-button type="primary" @click="addDietRecord">
                  <el-icon><Plus /></el-icon>
                  添加记录
                </el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </el-card>

      <!-- 今日饮食记录 -->
      <el-card class="records-card">
        <template #header>
          <div class="card-header">
            <span>今日饮食记录</span>
            <div class="header-actions">
              <el-tag type="success">总卡路里: {{ totalCalories }} kcal</el-tag>
            </div>
          </div>
        </template>

        <el-table :data="todayRecords" style="width: 100%">
          <el-table-column prop="foodName" label="食物名称" />
          <el-table-column prop="calories" label="卡路里" width="100">
            <template #default="scope">
              {{ scope.row.calories }} kcal
            </template>
          </el-table-column>
          <el-table-column prop="quantity" label="份量" width="100">
            <template #default="scope"> {{ scope.row.quantity }} 份 </template>
          </el-table-column>
          <el-table-column prop="mealType" label="餐次" width="100">
            <template #default="scope">
              <el-tag :type="getMealTypeColor(scope.row.mealType)">
                {{ getMealTypeLabel(scope.row.mealType) }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="time" label="时间" width="120">
            <template #default="scope">
              {{ formatTime(scope.row.time) }}
            </template>
          </el-table-column>
          <el-table-column label="操作" width="120">
            <template #default="scope">
              <el-button
                type="danger"
                size="small"
                @click="deleteRecord(scope.$index)"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>

      <!-- 营养分析 -->
      <el-card class="nutrition-card">
        <template #header>
          <div class="card-header">
            <span>营养分析</span>
          </div>
        </template>

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
      </el-card>
    </div>
  </Layout>
</template>

<script setup>
import { ref, computed } from "vue";
import { ElMessage } from "element-plus";
import Layout from "@/components/Layout.vue";

const dietForm = ref({
  foodName: "",
  calories: 0,
  quantity: 1,
  mealType: "",
  time: null,
});

const todayRecords = ref([
  {
    foodName: "燕麦粥",
    calories: 150,
    quantity: 1,
    mealType: "breakfast",
    time: "08:00",
  },
  {
    foodName: "鸡胸肉",
    calories: 200,
    quantity: 1,
    mealType: "lunch",
    time: "12:30",
  },
]);

const totalCalories = computed(() => {
  return todayRecords.value.reduce((sum, record) => sum + record.calories, 0);
});

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

const formatTime = (time) => {
  return time;
};

const addDietRecord = () => {
  if (!dietForm.value.foodName || !dietForm.value.calories) {
    ElMessage.warning("请填写完整的饮食信息");
    return;
  }

  const newRecord = {
    ...dietForm.value,
    time: dietForm.value.time
      ? `${dietForm.value.time
          .getHours()
          .toString()
          .padStart(2, "0")}:${dietForm.value.time
          .getMinutes()
          .toString()
          .padStart(2, "0")}`
      : new Date().toLocaleTimeString("zh-CN", {
          hour: "2-digit",
          minute: "2-digit",
        }),
  };

  todayRecords.value.push(newRecord);

  // 重置表单
  dietForm.value = {
    foodName: "",
    calories: 0,
    quantity: 1,
    mealType: "",
    time: null,
  };

  ElMessage.success("饮食记录添加成功");
};

const deleteRecord = (index) => {
  todayRecords.value.splice(index, 1);
  ElMessage.success("记录删除成功");
};
</script>

<style scoped>
.diet-page {
  padding: 0;
}

.add-record-card {
  margin-bottom: 20px;
}

.records-card {
  margin-bottom: 20px;
}

.nutrition-card {
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
