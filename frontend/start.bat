@echo off
echo 正在启动 HealthTrace 前端应用...
echo.

echo 检查 Node.js 是否安装...
node --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到 Node.js，请先安装 Node.js
    pause
    exit /b 1
)

echo 检查 npm 是否可用...
npm --version >nul 2>&1
if errorlevel 1 (
    echo 错误: npm 不可用
    pause
    exit /b 1
)

echo 安装依赖包...
npm install
if errorlevel 1 (
    echo 错误: 依赖安装失败
    pause
    exit /b 1
)

echo.
echo 启动开发服务器...
echo 前端应用将在 http://localhost:3000 启动
echo 请确保后端服务器在 http://localhost:5000 运行
echo.
echo 按 Ctrl+C 停止服务器
echo.

npm run dev

pause 