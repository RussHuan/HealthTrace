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

// 修改密码
export const changePassword = async (userData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/change-password`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });
        const data = await response.json();
        if (!response.ok) {
            // 后端返回的错误信息在 data.msg 中
            throw new Error(data.msg || '修改密码失败');
        }
        return data;
    } catch (error) {
        throw error;
    }
};

// 删除账户
export const deleteAccount = async (userData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/delete-account`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });
        const data = await response.json();
        if (!response.ok) {
            // 后端返回的错误信息在 data.msg 中
            throw new Error(data.msg || '删除账户失败');
        }
        return data;
    } catch (error) {
        throw error;
    }
};

// 导出数据
export const exportData = async (userId) => {
    try {
        // 在实际应用中，用户ID应从认证令牌中获取，而不是作为查询参数
        const response = await fetch(`${API_BASE_URL}/users/export-data?userId=${userId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        const data = await response.json();
        if (!response.ok) {
            // 后端返回的错误信息在 data.msg 中
            throw new Error(data.msg || '数据导出失败');
        }
        return data;
    } catch (error) {
        throw error;
    }
};

// 导出API对象
export const authApi = {
    login,
    register,
    changePassword,
    deleteAccount,
    exportData
};
