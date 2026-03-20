"""
任务4.1：Pandas数据结构之Series - 完整实施流程
教材：《无人机遥感数据处理与分析》第四章
演示Series的创建、基本操作、运算与统计的完整流程
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("任务4.1：Pandas数据结构之Series - 完整实施流程")
print("=" * 60)

# ========== 第一步：创建多个遥感监测的 Series ==========
print("\n第一步：创建遥感监测 Series")
print("=" * 50)

# 1.1 从列表创建 NDVI Series
ndvi_data = [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63, 0.88]
sample_points = [f'样点{i}' for i in range(1, 9)]
ndvi = pd.Series(ndvi_data, index=sample_points, name='NDVI指数')
print("1.1 NDVI数据（从列表创建）:")
print(ndvi)
print(f"   数据形状: {ndvi.shape}, 数据类型: {ndvi.dtype}")

# 1.2 从字典创建植被覆盖度 Series
coverage_dict = {'样区A': 85.6, '样区B': 72.3, '样区C': 91.2,
                 '样区D': 68.7, '样区E': 79.4, '样区F': 88.9}
coverage = pd.Series(coverage_dict, name='植被覆盖度(%)')
print("\n1.2 植被覆盖度数据（从字典创建）:")
print(coverage)
print(f"   数据形状: {coverage.shape}, 数据类型: {coverage.dtype}")

# 1.3 创建包含缺失值的温度时间序列
dates = pd.date_range('2026-03-17 08:00', periods=10, freq='H')
temp_data = [25.3, 26.1, np.nan, 27.3, 28.5, np.nan, 29.1, 27.8, 30.2, 28.7]
temperature = pd.Series(temp_data, index=dates, name='温度(℃)')
print("\n1.3 温度时间序列（含缺失值）:")
print(temperature)
print(f"   缺失值数量: {temperature.isna().sum()}")

# ========== 第二步：Series 基本操作 ==========
print("\n第二步：Series 基本操作")
print("=" * 50)

# 2.1 数据访问
print("2.1 数据访问:")
print(f"   样点3的NDVI: {ndvi['样点3']}")
print(f"   NDVI第一个值: {ndvi.iloc[0]}")
print(f"   NDVI前3个值:")
print(ndvi.iloc[:3])

# 2.2 条件筛选
print(f"\n2.2 条件筛选（NDVI>0.7的样点）:")
high_ndvi = ndvi[ndvi > 0.7]
print(high_ndvi)

# 2.3 数据修改
coverage_modified = coverage.copy()
coverage_modified['样区B'] = 75.8
coverage_modified[coverage_modified < 70] = 70
print(f"\n2.3 修改后的植被覆盖度:")
print(coverage_modified)

# 2.4 排序
print(f"\n2.4 按值降序排序:")
print(ndvi.sort_values(ascending=False))

# ========== 第三步：统计描述 ==========
print("\n第三步：统计描述")
print("=" * 50)

# 3.1 NDVI统计
print("3.1 NDVI统计描述:")
print(f"   平均值: {ndvi.mean():.4f}")
print(f"   中位数: {ndvi.median():.4f}")
print(f"   标准差: {ndvi.std():.4f}")
print(f"   最小值: {ndvi.min():.4f}")
print(f"   最大值: {ndvi.max():.4f}")
print(f"   描述性统计:")
print(ndvi.describe())

# 3.2 植被覆盖度统计
print(f"\n3.2 植被覆盖度统计:")
print(coverage.describe())

# ========== 第四步：算术运算与缺失值处理 ==========
print("\n第四步：算术运算与缺失值处理")
print("=" * 50)

# 4.1 算术运算
ndvi_percent = ndvi * 100
print(f"4.1 NDVI转换为百分比（前5个）:")
print(ndvi_percent.head())

# 4.2 Series间运算
# 创建EVI数据
evi = pd.Series([0.45, 0.48, 0.42, 0.50, 0.55, 0.46, 0.49, 0.52],
                index=sample_points, name='EVI指数')
diff = ndvi - evi
print(f"\n4.2 NDVI与EVI的差值:")
print(diff)

# 4.3 缺失值填充
temp_filled = temperature.interpolate(method='linear')
print(f"\n4.3 温度缺失值填充（线性插值）:")
print(temp_filled)
print(f"   填充后缺失值数量: {temp_filled.isna().sum()}")

# ========== 第五步：移动窗口统计 ==========
print("\n第五步：移动窗口统计")
print("=" * 50)

# 5.1 计算移动平均值
rolling_mean = temp_filled.rolling(window=3).mean()
print("5.1 温度3小时移动平均值:")
print(rolling_mean)

# 5.2 计算移动标准差
rolling_std = temp_filled.rolling(window=3).std()
print(f"\n5.2 温度3小时移动标准差:")
print(rolling_std)

print("\n" + "=" * 60)
print("任务4.1 Series完整操作流程示例结束")
print("=" * 60)
