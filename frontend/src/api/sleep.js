// api/sleep.js

const API_BASE_URL = 'http://localhost:5000';

// 添加睡眠记录
export const addSleepRecord = async (sleepData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/sleep/records`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(sleepData),
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.message || '添加睡眠记录失败');
    }
    
    return data;
  } catch (error) {
    throw error;
  }
};

// 获取用户睡眠记录
export const getSleepRecords = async (userId, params = {}) => {
  try {
    const queryParams = new URLSearchParams();
    
    if (params.start_date) queryParams.append('start_date', params.start_date);
    if (params.end_date) queryParams.append('end_date', params.end_date);
    if (params.limit) queryParams.append('limit', params.limit);
    
    const url = `${API_BASE_URL}/sleep/records/${userId}${queryParams.toString() ? '?' + queryParams.toString() : ''}`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.message || '获取睡眠记录失败');
    }
    
    return data;
  } catch (error) {
    throw error;
  }
};

// 更新睡眠记录
export const updateSleepRecord = async (recordId, updateData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/sleep/records/${recordId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updateData),
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.message || '更新睡眠记录失败');
    }
    
    return data;
  } catch (error) {
    throw error;
  }
};

// 删除睡眠记录
export const deleteSleepRecord = async (recordId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/sleep/records/${recordId}`, {
      method: 'DELETE',
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.message || '删除睡眠记录失败');
    }
    
    return data;
  } catch (error) {
    throw error;
  }
};

// 获取睡眠统计信息
export const getSleepStats = async (userId, days = 7) => {
  try {
    const response = await fetch(`${API_BASE_URL}/sleep/stats/${userId}?days=${days}`);
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.message || '获取睡眠统计失败');
    }
    
    return data;
  } catch (error) {
    throw error;
  }
}; 