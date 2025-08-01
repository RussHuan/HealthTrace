#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
睡眠记录模块测试脚本
"""

import requests
import json
from datetime import datetime, timedelta

# API基础URL
BASE_URL = "http://localhost:5000"

def test_sleep_api():
    """测试睡眠记录API"""
    
    print("=== 睡眠记录API测试 ===\n")
    
    # 1. 首先注册一个测试用户
    print("1. 注册测试用户...")
    register_data = {
        "username": "testuser_sleep",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/users/register", json=register_data)
        if response.status_code == 200:
            print("✓ 用户注册成功")
        elif response.status_code == 409:
            print("✓ 用户已存在")
        else:
            print(f"✗ 用户注册失败: {response.text}")
            return
    except Exception as e:
        print(f"✗ 连接失败: {e}")
        return
    
    # 2. 登录获取用户ID
    print("\n2. 用户登录...")
    login_data = {
        "username": "testuser_sleep",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/users/login", json=login_data)
        if response.status_code == 200:
            user_id = response.json().get("data")
            print(f"✓ 登录成功，用户ID: {user_id}")
        else:
            print(f"✗ 登录失败: {response.text}")
            return
    except Exception as e:
        print(f"✗ 登录失败: {e}")
        return
    
    # 3. 添加睡眠记录
    print("\n3. 添加睡眠记录...")
    
    # 创建测试数据
    now = datetime.now()
    sleep_time = (now - timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S")
    wake_time = now.strftime("%Y-%m-%dT%H:%M:%S")
    
    sleep_data = {
        "user_id": user_id,
        "sleep_time": sleep_time,
        "wake_time": wake_time,
        "quality_rating": 8,
        "notes": "测试睡眠记录"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/sleep/records", json=sleep_data)
        if response.status_code == 200:
            record = response.json().get("data")
            record_id = record.get("id")
            print(f"✓ 睡眠记录添加成功，记录ID: {record_id}")
            print(f"  睡眠时长: {record.get('duration_hours')} 小时")
        else:
            print(f"✗ 添加睡眠记录失败: {response.text}")
            return
    except Exception as e:
        print(f"✗ 添加睡眠记录失败: {e}")
        return
    
    # 4. 获取睡眠记录列表
    print("\n4. 获取睡眠记录列表...")
    
    try:
        response = requests.get(f"{BASE_URL}/sleep/records/{user_id}")
        if response.status_code == 200:
            records = response.json().get("data", [])
            print(f"✓ 获取睡眠记录成功，共 {len(records)} 条记录")
            for record in records:
                print(f"  - 记录ID: {record.get('id')}, 时长: {record.get('duration_hours')}小时")
        else:
            print(f"✗ 获取睡眠记录失败: {response.text}")
    except Exception as e:
        print(f"✗ 获取睡眠记录失败: {e}")
    
    # 5. 获取睡眠统计
    print("\n5. 获取睡眠统计...")
    
    try:
        response = requests.get(f"{BASE_URL}/sleep/stats/{user_id}?days=7")
        if response.status_code == 200:
            stats = response.json().get("data", {})
            print(f"✓ 获取睡眠统计成功")
            print(f"  总记录数: {stats.get('total_records', 0)}")
            print(f"  平均时长: {stats.get('average_duration', 0)} 小时")
            print(f"  平均质量: {stats.get('average_quality', 0)}/10")
        else:
            print(f"✗ 获取睡眠统计失败: {response.text}")
    except Exception as e:
        print(f"✗ 获取睡眠统计失败: {e}")
    
    # 6. 更新睡眠记录
    print("\n6. 更新睡眠记录...")
    
    update_data = {
        "quality_rating": 9,
        "notes": "更新后的测试记录"
    }
    
    try:
        response = requests.put(f"{BASE_URL}/sleep/records/{record_id}", json=update_data)
        if response.status_code == 200:
            updated_record = response.json().get("data")
            print(f"✓ 睡眠记录更新成功")
            print(f"  新质量评分: {updated_record.get('quality_rating')}")
            print(f"  新备注: {updated_record.get('notes')}")
        else:
            print(f"✗ 更新睡眠记录失败: {response.text}")
    except Exception as e:
        print(f"✗ 更新睡眠记录失败: {e}")
    
    # 7. 删除睡眠记录
    print("\n7. 删除睡眠记录...")
    
    try:
        response = requests.delete(f"{BASE_URL}/sleep/records/{record_id}")
        if response.status_code == 200:
            print(f"✓ 睡眠记录删除成功")
        else:
            print(f"✗ 删除睡眠记录失败: {response.text}")
    except Exception as e:
        print(f"✗ 删除睡眠记录失败: {e}")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    test_sleep_api() 