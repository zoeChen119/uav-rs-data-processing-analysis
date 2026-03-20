"""
案例5：Series的运算与统计
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示Series的算术运算、缺失值处理和移动窗口统计
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("案例5：Series的运算与统计")
print("=" * 60)

# 创建无人机连续监测的NDVI数据（含缺失值）
dates = pd.date_range('2026-03-17', periods=10, freq='D')
ndvi_data = [0.65, 0.68, np.nan, 0.72, 0.75, 0.70, 0.78, np.nan, 0.82, 0.79]
ndvi = pd.Series(ndvi_data, index=dates, name='NDVI指数')

print("原始NDVI监测数据（含缺失值）:")
print(ndvi)
print(f"\n缺失值数量: {ndvi.isna().sum()}")
print(f"缺失值位置: {ndvi[ndvi.isna()].index.tolist()}")
print()

# ========== 算术运算 ==========
print("1. 算术运算:")
print("-" * 40)

# 转换为百分比
ndvi_percent = ndvi * 100
print("转换为百分比（前5个）:")
print(ndvi_percent.head())
print()

# 加上一个常数（数据标准化）
ndvi_normalized = (ndvi - ndvi.mean()) / ndvi.std()
print("标准化处理（均值=0，标准差=1）:")
print(ndvi_normalized)
print()

# ========== 统计分析 ==========
print("2. 统计分析（仅使用有效数据）:")
print("-" * 40)

valid_ndvi = ndvi.dropna()
print(f"有效数据数量: {len(valid_ndvi)}")
print(f"平均值: {valid_ndvi.mean():.4f}")
print(f"标准差: {valid_ndvi.std():.4f}")
print(f"最小值: {valid_ndvi.min():.4f}")
print(f"最大值: {valid_ndvi.max():.4f}")
print(f"中位数: {valid_ndvi.median():.4f}")
print()

# ========== 缺失值处理 ==========
print("3. 缺失值处理:")
print("-" * 40)

# 线性插值
ndvi_filled_linear = ndvi.interpolate(method='linear')
print("线性插值填充后的数据:")
print(ndvi_filled_linear)
print(f"填充后缺失值数量: {ndvi_filled_linear.isna().sum()}")
print()

# 前向填充
ndvi_filled_ffill = ndvi.fillna(method='ffill')
print("前向填充（用前一个值填充）:")
print(ndvi_filled_ffill)
print()

# 后向填充
ndvi_filled_bfill = ndvi.fillna(method='bfill')
print("后向填充（用后一个值填充）:")
print(ndvi_filled_bfill)
print()

# 固定值填充
ndvi_filled_fixed = ndvi.fillna(0.7)
print("固定值填充（填充为0.7）:")
print(ndvi_filled_fixed)
print()

# ========== 移动窗口统计 ==========
print("4. 移动窗口统计（使用线性插值后的数据）:")
print("-" * 40)

# 3天移动平均值
rolling_mean_3 = ndvi_filled_linear.rolling(window=3).mean()
print("3天移动平均值:")
print(rolling_mean_3)
print()

# 5天移动平均值
rolling_mean_5 = ndvi_filled_linear.rolling(window=5).mean()
print("5天移动平均值:")
print(rolling_mean_5)
print()

# 3天移动标准差
rolling_std_3 = ndvi_filled_linear.rolling(window=3).std()
print("3天移动标准差:")
print(rolling_std_3)
print()

# 累积统计
print("累积统计:")
print(f"累积和:")
print(ndvi_filled_linear.cumsum())
print()
print(f"累积最大值:")
print(ndvi_filled_linear.cummax())
