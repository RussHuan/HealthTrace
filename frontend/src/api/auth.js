// api/auth.js

const API_BASE_URL = 'http://localhost:5000';

// 用户登录
export const login = async (credentials) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '登录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 用户注册
export const register = async (userData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '注册失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 导出API对象
export const authApi = {
    login,
    register
}; 