"""
任务4.1：Pandas数据结构之Series - 创建示例
教材：《无人机遥感数据处理与分析》第四章
作者：[你的姓名]
日期：2026年3月

本文件演示Pandas Series数据结构的创建方法
与教材初稿内容一致
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("任务4.1：Pandas数据结构之Series - 创建方法演示")
print("=" * 60)

# ============================================================================
# 案例1：从列表创建Series
# ============================================================================
print("\n案例1：从列表创建Series")
print("-" * 40)

# 创建无人机采集的植被指数数据
ndvi_data = [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63]
sample_points = ['样点1', '样点2', '样点3', '样点4', '样点5', '样点6', '样点7']

# 从列表创建 Series，指定自定义索引和名称
ndvi_series = pd.Series(ndvi_data, index=sample_points, name='NDVI指数')
print("无人机采集的NDVI植被指数数据:")
print(ndvi_series)
print(f"\n数据形状: {ndvi_series.shape}")
print(f"数据类型: {ndvi_series.dtype}")
print(f"平均值: {ndvi_series.mean():.3f}")
print(f"最大值: {ndvi_series.max():.3f} (样点: {ndvi_series.idxmax()})")

# ============================================================================
# 案例2：从字典创建Series
# ============================================================================
print("\n\n案例2：从字典创建Series")
print("-" * 40)

# 从字典创建 Series（城市人口数据示例）
city_data = {
    '北京': 2154.2,
    '上海': 2428.1,
    '广州': 1867.7,
    '深圳': 1768.2,
    '成都': 2093.8
}
city_series = pd.Series(city_data, name='城市人口(万人)')
print("从字典创建的 Series:")
print(city_series)
print(f"\n索引: {city_series.index.tolist()}")
print(f"值: {city_series.values}")

# ============================================================================
# 案例3：创建包含缺失值的Series
# ============================================================================
print("\n\n案例3：创建包含缺失值的Series")
print("-" * 40)

# 创建包含缺失值的温度数据（模拟传感器故障）
temp_data = [25.3, np.nan, 27.8, 28.5, np.nan, 26.9]
time_points = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00']

temp_series = pd.Series(temp_data, index=time_points, name='温度(℃)')
print("包含缺失值的温度数据:")
print(temp_series)
print(f"\n有效数据数量: {temp_series.count()}")
print(f"缺失值数量: {temp_series.isna().sum()}")

# ============================================================================
# 案例4：Series的基本操作
# ============================================================================
print("\n\n案例4：Series的基本操作")
print("-" * 40)

# 创建无人机植被覆盖度数据
coverage_data = {
    '样区A': 85.6,
    '样区B': 72.3,
    '样区C': 91.2,
    '样区D': 68.7,
    '样区E': 79.4
}
coverage = pd.Series(coverage_data, name='植被覆盖度(%)')
print("原始植被覆盖度数据:")
print(coverage)

# 数据访问
print(f"\n样区A的覆盖度: {coverage['样区A']}%")
print(f"第一个元素: {coverage.iloc[0]}%")
print(f"前3个样区:\n{coverage.iloc[:3]}")

# 数据修改
coverage_modified = coverage.copy()
coverage_modified['样区B'] = 75.8
coverage_modified[coverage_modified < 70] = 70
print(f"\n修改后的数据（修正样区B，将低于70%的设为70%）:")
print(coverage_modified)

# 排序
print(f"\n按值升序排序:\n{coverage.sort_values()}")
print(f"\n按索引排序:\n{coverage.sort_index()}")

# 统计分析
print(f"\n平均值: {coverage.mean():.2f}%")
print(f"中位数: {coverage.median():.2f}%")
print(f"标准差: {coverage.std():.2f}%")
print(f"\n描述性统计:")
print(coverage.describe())

# ============================================================================
# 案例5：Series的运算与统计
# ============================================================================
print("\n\n案例5：Series的运算与统计")
print("-" * 40)

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

# ============================================================================
# 任务实施代码
# ============================================================================
print("\n\n" + "=" * 60)
print("任务实施：完整操作流程")
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

# 1.2 从字典创建植被覆盖度 Series
coverage_dict = {'样区A': 85.6, '样区B': 72.3, '样区C': 91.2,
                 '样区D': 68.7, '样区E': 79.4, '样区F': 88.9}
coverage = pd.Series(coverage_dict, name='植被覆盖度(%)')
print("\n1.2 植被覆盖度数据（从字典创建）:")
print(coverage)

# 1.3 创建包含缺失值的温度时间序列
dates = pd.date_range('2026-03-17 08:00', periods=10, freq='H')
temp_data = [25.3, 26.1, np.nan, 27.3, 28.5, np.nan, 29.1, 27.8, 30.2, 28.7]
temperature = pd.Series(temp_data, index=dates, name='温度(℃)')
print("\n1.3 温度时间序列（含缺失值）:")
print(temperature)
print(f"   缺失值数量: {temperature.isna().sum()}")

# ========== 第二步：Series 基本操作 ==========
print("\n\n第二步：Series 基本操作")
print("=" * 50)

# 2.1 数据访问
print("2.1 数据访问:")
print(f"   样点3的NDVI: {ndvi['样点3']}")
print(f"   NDVI第一个值: {ndvi.iloc[0]}")
print(f"   NDVI前3个值:\n{ndvi.iloc[:3]}")

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
print(f"\n2.4 按值降序排序:\n{ndvi.sort_values(ascending=False)}")

# ========== 第三步：统计描述 ==========
print("\n\n第三步：统计描述")
print("=" * 50)

# 3.1 NDVI统计
print("3.1 NDVI统计描述:")
print(f"   平均值: {ndvi.mean():.4f}")
print(f"   中位数: {ndvi.median():.4f}")
print(f"   标准差: {ndvi.std():.4f}")
print(f"   最小值: {ndvi.min():.4f}")
print(f"   最大值: {ndvi.max():.4f}")
print(f"   描述性统计:\n{ndvi.describe()}")

# 3.2 植被覆盖度统计
print(f"\n3.2 植被覆盖度统计:\n{coverage.describe()}")

# ========== 第四步：算术运算与缺失值处理 ==========
print("\n\n第四步：算术运算与缺失值处理")
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
print("\n\n第五步：移动窗口统计")
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
print("任务4.1 Series创建示例结束")
print("=" * 60)
