<template>
  <a-layout style="min-height: 100vh">
    <!-- 侧边栏 -->
    <a-layout-sider
      v-model:collapsed="collapsed"
      collapsible
      :width="siderWidth"
      :collapsed-width="80"
    >
      <div class="title-bar" :class="{ collapsed: collapsed }">
        <img class="logo" src="../assets/logo.png" alt="logo" />
        <div class="sidebar-header" :class="{ hidden: collapsed }">
          <h2>HealthTrace</h2>
          <p>健迹：让健康有迹可循</p>
        </div>
      </div>

      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="inline"
        @click="onMenuClick"
      >
        <a-menu-item
          v-for="item in menuItems"
          :key="item.key"
          @mouseenter="hoverKey = item.key"
          @mouseleave="hoverKey = null"
          :class="{
            hovered: hoverKey === item.key && !collapsed
          }"
        >
          <component :is="item.icon" />
          <span>{{ item.label }}</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>

    <!-- 主体内容区域 -->
    <a-layout :style="{ marginLeft: collapsed ? '80px' : siderWidth + 'px' }">
      <!-- 头部 -->
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

      <!-- 内容区 -->
      <a-layout-content class="main-content">
        <slot />
      </a-layout-content>

      <!-- 页脚 -->
      <a-layout-footer style="text-align: center">
        HealthTrace ©2025 健迹 — 让健康有迹可循
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
import {ref, computed, watch} from "vue";
import { useRouter, useRoute } from "vue-router";
import { ElMessageBox } from "element-plus";
import { useAuthStore } from "@/stores/auth";
import { ArrowDown } from "@element-plus/icons-vue";

const collapsed = ref(false);
const selectedKeys = ref(["1"]);
const hoverKey = ref<string | null>(null);

const router = useRouter();
const route = useRoute();
const authStore = useAuthStore();

const menuItems = [
  { key: "1", label: "首页", icon: DesktopOutlined },
  { key: "2", label: "睡眠记录", icon: RestOutlined },
  { key: "3", label: "运动记录", icon: ThunderboltOutlined },
  { key: "4", label: "饮食记录", icon: AppleOutlined },
  { key: "5", label: "个人中心", icon: UserOutlined },
];

// *** 修改这里，固定宽度 ***
const siderWidth = computed(() => (collapsed.value ? 80 : 260));

const routeKeyMap: Record<string, string> = {
  "/dashboard": "1",
  "/sleep": "2",
  "/exercise": "3",
  "/diet": "4",
  "/profile": "5",
};

const pageTitle = computed(() => {
  const titleMap: Record<string, string> = {
    "/dashboard": "首页",
    "/diet": "饮食记录",
    "/exercise": "运动记录",
    "/sleep": "睡眠记录",
    "/profile": "个人中心",
  };
  return titleMap[route.path] || "健康追踪";
});

selectedKeys.value = [routeKeyMap[route.path] || "1"];

const onMenuClick = (info: { key: string }) => {
  const keyToRoute: Record<string, string> = {
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
  justify-content: flex-start;
}

.title-bar.collapsed {
  justify-content: center;
}

.logo {
  height: 56px;
  margin-right: 16px;
  transition: all 0.3s;
}

.sidebar-header h2 {
  font-family: "Poppins", sans-serif;
  color: transparent;
  background: linear-gradient(90deg, #ffde59, #38b6ff);
  -webkit-background-clip: text;
  background-clip: text;
  margin: 0 0 6px 0;
  font-size: 24px;
  font-weight: 800;
}

.sidebar-header p {
  font-family: "Noto Sans SC", sans-serif;
  color: #c0c0c0;
  margin: 0;
  font-size: 14px;
}

.sidebar-header {
  opacity: 1;
  transform: translateX(0);
  transition: opacity 0.3s ease, transform 0.3s ease;
  white-space: nowrap;
}

.sidebar-header.hidden {
  opacity: 0;
  transform: translateX(-10px);
  pointer-events: none;
  width: 0;
  overflow: hidden;
}

/* logo 不要动态调整大小 */
.logo {
  height: 56px;
  margin-right: 16px;
  transition: height 0.3s ease;
}
.title-bar.collapsed .logo {
  margin-right: 0;
}

/* 调整菜单整体字号 */
:deep(.ant-menu) {
  font-size: 16px;
}

/* 调整菜单图标大小 */
:deep(.ant-menu .anticon) {
  font-size: 18px;
}

/* 固定侧边栏 */
:deep(.ant-layout-sider) {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  overflow: auto;
  z-index: 10;
  transition: width 0.3s ease;
}

/* 取消菜单项整体放大 */
:deep(.ant-menu-item.hovered) {
  transform: none !important;
}

/* 只放大菜单项内的图标和文字 */
:deep(.ant-menu-item.hovered) .anticon,
:deep(.ant-menu-item.hovered) span {
  transition: transform 0.3s ease;
  transform-origin: left center;
  transform: scale(1.15);
}

/* 内容区随 collapsed 和 siderWidth 动态移动 */
:deep(.ant-layout) {
  transition: margin-left 0.3s ease;
}

/* 头部样式 */
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

/* 内容区样式 */
.main-content {
  background-color: #f9fafb;
  padding: 20px;
  min-height: calc(100vh - 64px - 70px);
}
</style>
