<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
// 根组件
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', 'Noto Sans SC', 'Helvetica Neue', Helvetica,
    'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
  background-color: #f5f5f5;
  font-weight: 600; /* 可选：默认加粗一点，让整体更有力 */
}

#app {
  min-height: 100vh;
}

</style>
