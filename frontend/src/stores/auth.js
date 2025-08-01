import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(null)
    const token = ref(localStorage.getItem('token') || null)

    const isAuthenticated = computed(() => !!token.value)

    const login = async (credentials) => {
        try {
            const response = await authApi.login(credentials)
            if (response.code === 0) {
                user.value = { id: response.data, username: credentials.username }
                token.value = response.data // 简化版，实际应该使用JWT
                localStorage.setItem('token', token.value)
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
        token.value = null
        localStorage.removeItem('token')
    }

    return {
        user,
        token,
        isAuthenticated,
        login,
        register,
        logout
    }
}) 