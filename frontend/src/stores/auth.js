// stores/auth.js

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(null) // Stores { id, username }
    const token = ref(localStorage.getItem('token') || null)
    const userId = ref(localStorage.getItem('userId') || null)

    const isAuthenticated = computed(() => !!token.value)

    // 初始化时尝试从 localStorage 恢复用户信息
    if (token.value && userId.value) {
        const storedUsername = localStorage.getItem('username');
        if (storedUsername) {
            user.value = { id: userId.value, username: storedUsername };
        } else {
            // 如果 username 没有存储，但有 userId 和 token，可以在这里尝试重新获取用户信息
            // 或者在需要 username 的地方进行检查和提示
            user.value = { id: userId.value, username: '未知用户' }; // 临时占位
        }
    }

    const login = async (credentials) => {
        try {
            const response = await authApi.login(credentials)
            if (response.code === 0) {
                user.value = { id: response.data, username: credentials.username } // 存储 username
                userId.value = response.data
                token.value = response.data // 简化版，实际应该使用JWT
                localStorage.setItem('token', token.value)
                localStorage.setItem('userId', userId.value)
                localStorage.setItem('username', credentials.username) // 确保 username 也存储
                return { success: true }
            } else {
                return { success: false, message: response.msg }
            }
        } catch (error) {
            return { success: false, message: '登录失败，请稍后重试' }
        }
    }

    const register = async (userData) => {
        try {
            const response = await authApi.register(userData)
            if (response.code === 0) {
                return { success: true, message: response.msg }
            } else {
                return { success: false, message: response.msg }
            }
        } catch (error) {
            return { success: false, message: '注册失败，请稍后重试' }
        }
    }

    const logout = () => {
        user.value = null
        userId.value = null
        token.value = null
        localStorage.removeItem('token')
        localStorage.removeItem('userId')
        localStorage.removeItem('username') // 清除 username
    }

    // 新增：修改密码
    const changePassword = async (oldPassword, newPassword) => {
        try {
            if (!user.value || !user.value.username) {
                return { success: false, message: '用户未登录或用户信息不完整' };
            }
            const response = await authApi.changePassword({
                username: user.value.username,
                old_password: oldPassword,
                new_password: newPassword
            });
            if (response.code === 0) {
                return { success: true, message: response.msg };
            } else {
                return { success: false, message: response.msg };
            }
        } catch (error) {
            console.error('修改密码API调用失败:', error);
            return { success: false, message: error.message || '修改密码失败，请稍后重试' };
        }
    };

    // 新增：删除账户
    const deleteAccount = async (password) => {
        try {
            if (!user.value || !user.value.username) {
                return { success: false, message: '用户未登录或用户信息不完整' };
            }
            const response = await authApi.deleteAccount({
                username: user.value.username,
                password: password
            });
            if (response.code === 0) {
                logout(); // 成功删除后自动登出
                return { success: true, message: response.msg };
            } else {
                return { success: false, message: response.msg };
            }
        } catch (error) {
            console.error('删除账户API调用失败:', error);
            return { success: false, message: error.message || '删除账户失败，请稍后重试' };
        }
    };

    // 新增：导出数据
    const exportUserData = async () => {
        try {
            if (!userId.value) {
                return { success: false, message: '用户ID未找到，无法导出数据' };
            }
            const response = await authApi.exportData(userId.value);
            if (response.code === 0) {
                return { success: true, data: response.data, message: response.msg };
            } else {
                return { success: false, message: response.msg };
            }
        } catch (error) {
            console.error('导出数据API调用失败:', error);
            return { success: false, message: error.message || '导出数据失败，请稍后重试' };
        }
    };


    return {
        user,
        userId,
        token,
        isAuthenticated,
        login,
        register,
        logout,
        changePassword,
        deleteAccount,
        exportUserData
    }
})
