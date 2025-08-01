<template>
  <el-container class="layout-container">
    <!-- 侧边栏 -->
    <el-aside width="250px" class="sidebar">
      <div class="sidebar-header">
        <h2>HealthTrace</h2>
        <p>健康追踪系统</p>
      </div>

      <el-menu
        :default-active="$route.path"
        class="sidebar-menu"
        router
        background-color="#001529"
        text-color="#fff"
        active-text-color="#409eff"
      >
        <el-menu-item index="/dashboard">
          <el-icon><DataBoard /></el-icon>
          <span>仪表盘</span>
        </el-menu-item>

        <el-menu-item index="/diet">
          <el-icon><Food /></el-icon>
          <span>饮食记录</span>
        </el-menu-item>

        <el-menu-item index="/exercise">
          <el-icon><Bicycle /></el-icon>
          <span>运动记录</span>
        </el-menu-item>

        <el-menu-item index="/sleep">
          <el-icon><Moon /></el-icon>
          <span>睡眠记录</span>
        </el-menu-item>

        <el-menu-item index="/profile">
          <el-icon><User /></el-icon>
          <span>个人资料</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <!-- 主内容区 -->
    <el-container>
      <!-- 顶部导航栏 -->
      <el-header class="header">
        <div class="header-left">
          <h3>{{ pageTitle }}</h3>
        </div>

        <div class="header-right">
          <el-dropdown @command="handleCommand">
            <span class="user-dropdown">
              <el-avatar :size="32" icon="User" />
              <span class="username">{{ authStore.user?.username }}</span>
              <el-icon><ArrowDown /></el-icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item command="profile">个人资料</el-dropdown-item>
                <el-dropdown-item command="logout" divided
                  >退出登录</el-dropdown-item
                >
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 内容区域 -->
      <el-main class="main-content">
        <slot />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { ElMessageBox } from "element-plus";
import { useAuthStore } from "@/stores/auth";

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();

const pageTitle = computed(() => {
  const titleMap = {
    "/dashboard": "仪表盘",
    "/diet": "饮食记录",
    "/exercise": "运动记录",
    "/sleep": "睡眠记录",
    "/profile": "个人资料",
  };
  return titleMap[route.path] || "健康追踪";
});

const handleCommand = async (command) => {
  if (command === "profile") {
    router.push("/profile");
  } else if (command === "logout") {
    try {
      await ElMessageBox.confirm("确定要退出登录吗？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      });
      authStore.logout();
      router.push("/login");
    } catch {
      // 用户取消
    }
  }
};
</script>

<style scoped>
.layout-container {
  height: 100vh;
}

.sidebar {
  background-color: #001529;
  color: white;
}

.sidebar-header {
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #1f2937;
}

.sidebar-header h2 {
  color: white;
  margin: 0 0 5px 0;
  font-size: 20px;
}

.sidebar-header p {
  color: #9ca3af;
  margin: 0;
  font-size: 12px;
}

.sidebar-menu {
  border: none;
}

.header {
  background-color: white;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}

.header-left h3 {
  margin: 0;
  color: #374151;
  font-size: 18px;
}

.user-dropdown {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 6px;
  transition: background-color 0.2s;
}

.user-dropdown:hover {
  background-color: #f3f4f6;
}

.username {
  margin: 0 8px;
  color: #374151;
}

.main-content {
  background-color: #f9fafb;
  padding: 20px;
}
</style>
