"""
案例3：创建包含缺失值的Series
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示包含缺失值的Series创建与缺失值检测
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("案例3：创建包含缺失值的Series")
print("=" * 60)

# 创建包含缺失值的温度数据（模拟传感器故障）
temp_data = [25.3, np.nan, 27.8, 28.5, np.nan, 26.9]
time_points = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00']

temp_series = pd.Series(temp_data, index=time_points, name='温度(℃)')

print("包含缺失值的温度数据:")
print(temp_series)
print()

print("缺失值分析:")
print(f"总数据点数: {len(temp_series)}")
print(f"有效数据数量: {temp_series.count()}")
print(f"缺失值数量: {temp_series.isna().sum()}")
print(f"缺失比例: {temp_series.isna().sum() / len(temp_series) * 100:.1f}%")
print()

print("缺失值检测（True表示缺失）:")
print(temp_series.isna())
print()

print("非缺失值检测（True表示有效）:")
print(temp_series.notna())
print()

print("仅提取有效数据:")
valid_data = temp_series.dropna()
print(valid_data)
print(f"有效数据平均值: {valid_data.mean():.2f}℃")
