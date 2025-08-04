// api/exercise.js

const API_BASE_URL = 'http://localhost:5000';

// 添加运动记录
export const addExerciseRecord = async (exerciseData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/exercise/records`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(exerciseData),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '添加运动记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 获取用户运动记录
export const getExerciseRecords = async (userId, params = {}) => {
    try {
        const queryParams = new URLSearchParams();

        if (params.start_date) queryParams.append('start_date', params.start_date);
        if (params.end_date) queryParams.append('end_date', params.end_date);
        if (params.limit) queryParams.append('limit', params.limit);

        const url = `${API_BASE_URL}/exercise/records/${userId}${queryParams.toString() ? '?' + queryParams.toString() : ''}`;

        const response = await fetch(url);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '获取运动记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 更新运动记录
export const updateExerciseRecord = async (recordId, updateData) => {
    try {
        const response = await fetch(`${API_BASE_URL}/exercise/records/${recordId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updateData),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '更新运动记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 删除运动记录
export const deleteExerciseRecord = async (recordId) => {
    try {
        const response = await fetch(`${API_BASE_URL}/exercise/records/${recordId}`, {
            method: 'DELETE',
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '删除运动记录失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
};

// 获取运动统计信息
export const getExerciseStats = async (userId, days = 7) => {
    try {
        const response = await fetch(`${API_BASE_URL}/exercise/stats/${userId}?days=${days}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '获取运动统计失败');
        }

        return data;
    } catch (error) {
        throw error;
    }
}; 