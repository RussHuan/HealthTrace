// api/diet.js

const API_BASE_URL = 'http://localhost:5000';

// 添加饮食记录
export const addDietRecord = async (dietData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/diet/records`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dietData),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '添加饮食记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 获取用户饮食记录
export const getDietRecords = async (userId, params = {}) => {
    try {
        const queryParams = new URLSearchParams();

        if (params.start_date) queryParams.append('start_date', params.start_date);
        if (params.end_date) queryParams.append('end_date', params.end_date);
        if (params.limit) queryParams.append('limit', params.limit);

        const url = `${API_BASE_URL}/diet/records/${userId}${queryParams.toString() ? '?' + queryParams.toString() : ''}`;

        const response = await fetch(url);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '获取饮食记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 更新饮食记录
export const updateDietRecord = async (recordId, updateData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/diet/records/${recordId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updateData),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '更新饮食记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 删除饮食记录
export const deleteDietRecord = async (recordId) => {
    try {
        const response = await fetch(`${API_BASE_URL}/diet/records/${recordId}`, {
            method: 'DELETE',
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '删除饮食记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 获取饮食统计信息
export const getDietStats = async (userId, days = 7) => {
    try {
        const response = await fetch(`${API_BASE_URL}/diet/stats/${userId}?days=${days}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '获取饮食统计失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};