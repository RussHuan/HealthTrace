<!--<template>-->
<!--  <el-container class="layout-container">-->
<!--    &lt;!&ndash; 侧边栏 &ndash;&gt;-->
<!--    <el-aside width="250px" class="sidebar">-->
<!--      <div class="sidebar-header">-->
<!--        <h2>HealthTrace</h2>-->
<!--        <p>健迹</p>-->
<!--      </div>-->

<!--      <el-menu-->
<!--        :default-active="$route.path"-->
<!--        class="sidebar-menu"-->
<!--        router-->
<!--        background-color="#001529"-->
<!--        text-color="#fff"-->
<!--        active-text-color="#409eff"-->
<!--      >-->
<!--        <el-menu-item index="/dashboard">-->
<!--          <el-icon><DataBoard /></el-icon>-->
<!--          <span>首页</span>-->
<!--        </el-menu-item>-->

<!--        <el-menu-item index="/diet">-->
<!--          <el-icon><Food /></el-icon>-->
<!--          <span>饮食记录</span>-->
<!--        </el-menu-item>-->

<!--        <el-menu-item index="/exercise">-->
<!--          <el-icon><Bicycle /></el-icon>-->
<!--          <span>运动记录</span>-->
<!--        </el-menu-item>-->

<!--        <el-menu-item index="/sleep">-->
<!--          <el-icon><Moon /></el-icon>-->
<!--          <span>睡眠记录</span>-->
<!--        </el-menu-item>-->

<!--        <el-menu-item index="/profile">-->
<!--          <el-icon><User /></el-icon>-->
<!--          <span>个人资料</span>-->
<!--        </el-menu-item>-->
<!--      </el-menu>-->
<!--    </el-aside>-->

<!--    &lt;!&ndash; 主内容区 &ndash;&gt;-->
<!--    <el-container>-->
<!--      &lt;!&ndash; 顶部导航栏 &ndash;&gt;-->
<!--      <el-header class="header">-->
<!--        <div class="header-left">-->
<!--          <h3>{{ pageTitle }}</h3>-->
<!--        </div>-->

<!--        <div class="header-right">-->
<!--          <el-dropdown @command="handleCommand">-->
<!--            <span class="user-dropdown">-->
<!--              <el-avatar :size="32" icon="User" />-->
<!--              <span class="username">{{ authStore.user?.username }}</span>-->
<!--              <el-icon><ArrowDown /></el-icon>-->
<!--            </span>-->
<!--            <template #dropdown>-->
<!--              <el-dropdown-menu>-->
<!--                <el-dropdown-item command="profile">个人资料</el-dropdown-item>-->
<!--                <el-dropdown-item command="logout" divided-->
<!--                  >退出登录</el-dropdown-item-->
<!--                >-->
<!--              </el-dropdown-menu>-->
<!--            </template>-->
<!--          </el-dropdown>-->
<!--        </div>-->
<!--      </el-header>-->

<!--      &lt;!&ndash; 内容区域 &ndash;&gt;-->
<!--      <el-main class="main-content">-->
<!--        <slot />-->
<!--      </el-main>-->
<!--    </el-container>-->
<!--  </el-container>-->
<!--</template>-->

<!--<script setup>-->
<!--import { computed } from "vue";-->
<!--import { useRoute, useRouter } from "vue-router";-->
<!--import { ElMessageBox } from "element-plus";-->
<!--import { useAuthStore } from "@/stores/auth";-->

<!--const route = useRoute();-->
<!--const router = useRouter();-->
<!--const authStore = useAuthStore();-->

<!--const pageTitle = computed(() => {-->
<!--  const titleMap = {-->
<!--    "/dashboard": "首页",-->
<!--    "/diet": "饮食记录",-->
<!--    "/exercise": "运动记录",-->
<!--    "/sleep": "睡眠记录",-->
<!--    "/profile": "个人资料",-->
<!--  };-->
<!--  return titleMap[route.path] || "健康追踪";-->
<!--});-->

<!--const handleCommand = async (command) => {-->
<!--  if (command === "profile") {-->
<!--    router.push("/profile");-->
<!--  } else if (command === "logout") {-->
<!--    try {-->
<!--      await ElMessageBox.confirm("确定要退出登录吗？", "提示", {-->
<!--        confirmButtonText: "确定",-->
<!--        cancelButtonText: "取消",-->
<!--        type: "warning",-->
<!--      });-->
<!--      authStore.logout();-->
<!--      router.push("/login");-->
<!--    } catch {-->
<!--      // 用户取消-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--.layout-container {-->
<!--  height: 100vh;-->
<!--}-->

<!--.sidebar {-->
<!--  background-color: #001529;-->
<!--  color: white;-->
<!--}-->

<!--.sidebar-header {-->
<!--  padding: 20px;-->
<!--  text-align: center;-->
<!--  border-bottom: 1px solid #1f2937;-->
<!--}-->

<!--.sidebar-header h2 {-->
<!--  color: white;-->
<!--  margin: 0 0 5px 0;-->
<!--  font-size: 20px;-->
<!--}-->

<!--.sidebar-header p {-->
<!--  color: #9ca3af;-->
<!--  margin: 0;-->
<!--  font-size: 12px;-->
<!--}-->

<!--.sidebar-menu {-->
<!--  border: none;-->
<!--}-->

<!--.header {-->
<!--  background-color: white;-->
<!--  border-bottom: 1px solid #e5e7eb;-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  justify-content: space-between;-->
<!--  padding: 0 20px;-->
<!--}-->

<!--.header-left h3 {-->
<!--  margin: 0;-->
<!--  color: #374151;-->
<!--  font-size: 18px;-->
<!--}-->

<!--.user-dropdown {-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  cursor: pointer;-->
<!--  padding: 8px 12px;-->
<!--  border-radius: 6px;-->
<!--  transition: background-color 0.2s;-->
<!--}-->

<!--.user-dropdown:hover {-->
<!--  background-color: #f3f4f6;-->
<!--}-->

<!--.username {-->
<!--  margin: 0 8px;-->
<!--  color: #374151;-->
<!--}-->

<!--.main-content {-->
<!--  background-color: #f9fafb;-->
<!--  padding: 20px;-->
<!--}-->
<!--</style>-->

<template>
  <a-layout style="min-height: 100vh">
    <!-- 侧边栏 -->
    <a-layout-sider
      v-model:collapsed="collapsed"
      collapsible
      :width="260"
      :collapsed-width="80"
    >
      <div class="title-bar" :class="{ collapsed: collapsed }">
        <img
          class="logo"
          :class="{ collapsed: collapsed }"
          src="../assets/logo.png"
          alt="logo"
        />
        <div v-if="!collapsed" class="sidebar-header">
          <h2>HealthTrace</h2>
          <p>健迹</p>
        </div>
      </div>

      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="inline"
        @click="onMenuClick"
      >
        <a-menu-item key="1">
          <DesktopOutlined />
          <span>首页</span>
        </a-menu-item>
        <a-menu-item key="2">
          <RestOutlined />
          <span>睡眠记录</span>
        </a-menu-item>
        <a-menu-item key="3">
          <ThunderboltOutlined />
          <span>运动记录</span>
        </a-menu-item>
        <a-menu-item key="4">
          <AppleOutlined />
          <span>饮食记录</span>
        </a-menu-item>
        <a-menu-item key="5">
          <UserOutlined />
          <span>个人中心</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <!-- 主体内容区域 -->
    <a-layout>
      <!-- 头部：使用代码A的顶部导航栏 -->
      <a-layout-header class="header">
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
                <el-dropdown-item command="logout" divided>退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </a-layout-header>

      <!-- 内容区：使用代码A的主内容区 -->
      <a-layout-content class="main-content">
        <slot />
      </a-layout-content>

      <!-- 页脚，可以保留代码B的页脚，也可以删掉 -->
      <a-layout-footer style="text-align: center">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script lang="ts" setup>
import {
  RestOutlined,
  AppleOutlined,
  ThunderboltOutlined,
  UserOutlined,
  DesktopOutlined,
} from "@ant-design/icons-vue";
import { ref, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { ElMessageBox } from "element-plus";
import { useAuthStore } from "@/stores/auth";

const collapsed = ref(false);
const selectedKeys = ref(["1"]);

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

// 根据路由自动同步菜单选中项
const routeKeyMap = {
  "/dashboard": "1",
  "/sleep": "2",
  "/exercise": "3",
  "/diet": "4",
  "/profile": "5",
};

const pageTitle = computed(() => {
  const titleMap = {
    "/dashboard": "首页",
    "/diet": "饮食记录",
    "/exercise": "运动记录",
    "/sleep": "睡眠记录",
    "/profile": "个人资料",
  };
  return titleMap[route.path] || "健康追踪";
});

selectedKeys.value = [routeKeyMap[route.path] || "1"];

const onMenuClick = (info: { key: string }) => {
  // 跳转对应路由
  const keyToRoute = {
    "1": "/dashboard",
    "2": "/sleep",
    "3": "/exercise",
    "4": "/diet",
    "5": "/profile",
  };
  router.push(keyToRoute[info.key]);
  selectedKeys.value = [info.key];
};

const handleCommand = async (command: string) => {
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
/* 侧边栏标题 */
.title-bar {
  display: flex;
  align-items: center;
  padding: 20px;
  color: #ffffff;
  transition: all 0.3s;
}
.title-bar.collapsed {
  justify-content: center;
}
.logo {
  height: 56px;
  margin-right: 16px;
  transition: all 0.3s;
}
.logo.collapsed {
  height: 48px;
  margin: 0;
}
.sidebar-header h2 {
  color: white;
  margin: 0 0 6px 0;
  font-size: 22px;
}
.sidebar-header p {
  color: #c0c0c0;
  margin: 0;
  font-size: 14px;
}

/* 调整菜单整体字号 */
:deep(.ant-menu) {
  font-size: 16px; /* 菜单文字更大 */
}

/* 调整菜单图标大小 */
:deep(.ant-menu .anticon) {
  font-size: 18px;
}

/* 头部样式（代码A的header） */
.header {
  background-color: white;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  height: 64px;
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

/* 内容区样式（代码A的main-content） */
.main-content {
  background-color: #f9fafb;
  padding: 20px;
  min-height: calc(100vh - 64px - 70px); /* 减去 header 和 footer 高度 */
}
</style>
