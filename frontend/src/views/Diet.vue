<template>
  <Layout>
    <div class="diet-page">
      <!-- 今日饮食记录 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="今日饮食记录" style="height: 100%">
              <div class="header-actions">
                <el-tag type="success">总卡路里: {{ totalCalories }} kcal</el-tag>
                <el-tag type="info">记录数: {{ todayRecords.length }}</el-tag>
              </div>
              <el-table :data="todayRecords" style="width: 100%" v-loading="tableLoading">
                <el-table-column prop="content" label="食物名称" />
                <el-table-column prop="calories" label="卡路里" width="100">
                  <template #default="scope">{{ scope.row.calories }} kcal</template>
                </el-table-column>
                <el-table-column prop="meal_type" label="餐次" width="100">
                  <template #default="scope">
                    <el-tag :type="getMealTypeColor(scope.row.meal_type)">
                      {{ getMealTypeLabel(scope.row.meal_type) }}
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column prop="date" label="日期" width="120">
                  <template #default="scope">{{ formatDate(scope.row.date) }}</template>
                </el-table-column>
                <el-table-column label="操作" width="160">
                  <template #default="scope">
                    <el-button type="primary" size="small" @click="openEditDialog(scope.row)">
                      编辑
                    </el-button>
                    <el-button type="danger" size="small" @click="deleteRecord(scope.row.id)">
                      删除
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </a-card>
          </a-col>
        </a-row>
      </div>

      <!-- 添加饮食记录 -->
      <div style="background-color: transparent; padding: 20px">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="添加饮食记录" style="height: 100%">
              <el-form :model="dietForm" label-width="100px">
                <el-row :gutter="20">
                  <el-col :span="8">
                    <el-form-item label="食物名称">
                      <el-input
                        v-model="dietForm.foodName"
                        placeholder="请输入食物名称"
                        @input="autoMatchCalories"
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

      <!-- 常见食物卡路里参考 -->
      <div style="background-color: transparent; padding: 20px;">
        <a-row :gutter="16" style="display: flex">
          <a-col :span="24">
            <a-card title="常见食物卡路里参考" class="common-foods-card">
              <a-row :gutter="16">
                <a-col
                  v-for="food in commonFoods"
                  :key="food.name"
                  :span="6"
                  class="food-item"
                >
                  <div class="food-tag-wrapper" style="display: flex; align-items: center; gap: 6px;">
                    <span class="food-name-label" style="flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                      {{ food.name }}
                    </span>
                    <el-tag
                      :type="getTagType(food.calories)"
                      effect="light"
                      style="padding: 0 6px; font-size: 12px; line-height: 18px; min-width: 50px; text-align: center;"
                    >
                      {{ food.calories }} kcal
                    </el-tag>
                  </div>
                </a-col>
              </a-row>
            </a-card>
          </a-col>
        </a-row>
      </div>
    </div>
  </Layout>

  <el-dialog v-model="editDialogVisible" title="编辑饮食记录" width="500px">
    <el-form :model="editForm" label-width="100px">
      <el-form-item label="食物名称">
        <el-input v-model="editForm.foodName" />
      </el-form-item>
      <el-form-item label="卡路里">
        <el-input-number v-model="editForm.calories" :min="0" />
      </el-form-item>
      <el-form-item label="餐次">
        <el-select v-model="editForm.mealType" placeholder="选择餐次">
          <el-option label="早餐" value="breakfast" />
          <el-option label="午餐" value="lunch" />
          <el-option label="晚餐" value="dinner" />
          <el-option label="加餐" value="snack" />
        </el-select>
      </el-form-item>
      <el-form-item label="日期">
        <el-date-picker v-model="editForm.date" type="date" format="YYYY-MM-DD" />
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
import { ElMessage } from "element-plus";
import Layout from "@/components/Layout.vue";
import { Plus } from "@element-plus/icons-vue";
import {
  addDietRecord,
  getDietRecords,
  deleteDietRecord,
  updateDietRecord,
} from "@/api/diet";
import { useAuthStore } from "@/stores/auth.js";

const commonFoods = [
  { name: "苹果(100g)", calories: 52 },
  { name: "香蕉(100g)", calories: 89 },
  { name: "米饭(100g)", calories: 130 },
  { name: "鸡蛋(100g)", calories: 155 },       // 约2个大鸡蛋
  { name: "牛肉(100g, 瘦肉)", calories: 250 },
  { name: "面包片(30g)", calories: 70 },
  { name: "牛奶(100ml, 全脂)", calories: 64 },
  { name: "橙子(100g)", calories: 47 },
  { name: "鸡胸肉(100g)", calories: 165 },
  { name: "猪肉(100g, 瘦肉)", calories: 242 },
  { name: "三文鱼(100g)", calories: 208 },
  { name: "黄油(10g)", calories: 72 },
  { name: "土豆(100g, 煮熟)", calories: 77 },
  { name: "胡萝卜(100g)", calories: 41 },
  { name: "西红柿(100g)", calories: 18 },
  { name: "黄瓜(100g)", calories: 16 },
  { name: "葡萄(100g)", calories: 69 },
  { name: "酸奶(100g, 原味)", calories: 59 },
  { name: "豆腐(100g)", calories: 76 },
  { name: "花生(100g)", calories: 567 },
  { name: "玉米(100g, 煮熟)", calories: 96 },
  { name: "意大利面(100g, 煮熟)", calories: 131 },
  { name: "蜂蜜(20g)", calories: 61 },
  { name: "巧克力(100g, 黑巧克力)", calories: 546 },
];

const getTagType = (calories) => {
  if (calories < 80) return 'success';    // 绿色
  if (calories <= 200) return 'warning';  // 黄色
  return 'danger';                        // 红色
};

const editDialogVisible = ref(false);
const editForm = ref({
  id: null,
  foodName: "",
  calories: 0,
  mealType: "",
  date: "",
});

const openEditDialog = (record) => {
  editForm.value = {
    id: record.id,
    foodName: record.content,
    calories: record.calories,
    mealType: record.meal_type,
    date: record.date,
  };
  editDialogVisible.value = true;
};

const submitEdit = async () => {
  try {
    const updateData = {
      content: editForm.value.foodName,
      calories: editForm.value.calories,
      meal_type: editForm.value.mealType,
      date: editForm.value.date,
    };

    await updateDietRecord(editForm.value.id, updateData);
    ElMessage.success("记录更新成功");
    editDialogVisible.value = false;
    await fetchDietRecords();
  } catch (error) {
    ElMessage.error(error.message || "更新记录失败");
  }
};

const authStore = useAuthStore();

const dietForm = ref({
  foodName: "",
  calories: 0,    // 实际卡路里 = quantity * unitCalories
  quantity: 1,
  unitCalories: 0,  // 单位卡路里，自动匹配的值
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
    todayRecords.value = [];
  } finally {
    tableLoading.value = false;
  }
};

// 自动匹配卡路里，更新 unitCalories 和 calories
const autoMatchCalories = (val) => {
  if (!val) {
    dietForm.value.unitCalories = 0;
    dietForm.value.calories = 0;
    return;
  }
  const matchedFood = commonFoods.find(food => food.name.includes(val));
  if (matchedFood) {
    dietForm.value.unitCalories = matchedFood.calories;
    dietForm.value.calories = matchedFood.calories * dietForm.value.quantity;
  } else {
    dietForm.value.unitCalories = 0;
    dietForm.value.calories = 0;
  }
};

// 监听份量变化，更新实际卡路里
watch(() => dietForm.value.quantity, (newQty) => {
  dietForm.value.calories = dietForm.value.unitCalories * newQty;
});

const addRecord = async () => {
  if (!authStore.userId) {
    ElMessage.error("请先登录");
    return;
  }

  if (
    !dietForm.value.foodName ||
    !dietForm.value.calories ||
    !dietForm.value.mealType
  ) {
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
      date: new Date().toISOString().split("T")[0],
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

    ElMessage.success("饮食记录添加成功");
    await fetchDietRecords();
  } catch (error) {
    ElMessage.error(error.message || "添加饮食记录失败");
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
    ElMessage.success("记录删除成功");
    await fetchDietRecords();
  } catch (error) {
    if (error !== "cancel") {
      ElMessage.error(error.message || "删除记录失败");
    }
  }
};

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
  if (!dateStr) return "-";
  const date = new Date(dateStr);
  return date.toLocaleDateString("zh-CN");
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

.common-foods-card {
  margin-top: 20px;
}

.food-item {
  padding: 10px 0;
  text-align: center;
}

.food-name {
  font-weight: 600;
  margin-bottom: 6px;
  font-size: 14px;
}
</style>
