"""
案例5：Series的运算与统计
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示Series的算术运算、缺失值处理和移动窗口统计
"""

import pandas as pd
import numpy as np

# 创建无人机连续监测的NDVI数据（含缺失值）
dates = pd.date_range('2026-03-17', periods=10, freq='D')
ndvi_data = [0.65, 0.68, np.nan, 0.72, 0.75, 0.70, 0.78, np.nan, 0.82, 0.79]
ndvi = pd.Series(ndvi_data, index=dates, name='NDVI指数')
print("原始NDVI监测数据（含缺失值）:")
print(ndvi)
print(f"\n缺失值数量: {ndvi.isna().sum()}")

# 算术运算：转换为百分比
ndvi_percent = ndvi * 100
print(f"\n转换为百分比（前5个）:")
print(ndvi_percent.head())

# 统计分析
print(f"\n有效数据统计:")
valid_ndvi = ndvi.dropna()
print(f"平均值: {valid_ndvi.mean():.4f}")
print(f"标准差: {valid_ndvi.std():.4f}")
print(f"最小值: {valid_ndvi.min():.4f}")
print(f"最大值: {valid_ndvi.max():.4f}")

# 缺失值填充
ndvi_filled = ndvi.interpolate(method='linear')
print(f"\n线性插值填充后的数据:")
print(ndvi_filled)
print(f"填充后缺失值数量: {ndvi_filled.isna().sum()}")

# 移动窗口统计（3天移动平均）
rolling_mean = ndvi_filled.rolling(window=3).mean()
print(f"\n3天移动平均值:")
print(rolling_mean)