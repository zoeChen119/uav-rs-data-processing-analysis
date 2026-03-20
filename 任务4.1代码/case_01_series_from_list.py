"""
案例1：从列表创建Series
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示从列表创建Series的基本方法
"""

import pandas as pd

print("=" * 60)
print("案例1：从列表创建Series")
print("=" * 60)

# 创建无人机采集的植被指数数据
ndvi_data = [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63]
sample_points = ['样点1', '样点2', '样点3', '样点4', '样点5', '样点6', '样点7']

# 从列表创建 Series，指定自定义索引和名称
ndvi_series = pd.Series(ndvi_data, index=sample_points, name='NDVI指数')

print("无人机采集的NDVI植被指数数据:")
print(ndvi_series)
print()

print("Series属性信息:")
print(f"数据形状: {ndvi_series.shape}")
print(f"数据类型: {ndvi_series.dtype}")
print(f"数据名称: {ndvi_series.name}")
print()

print("统计信息:")
print(f"平均值: {ndvi_series.mean():.3f}")
print(f"最大值: {ndvi_series.max():.3f} (样点: {ndvi_series.idxmax()})")
print(f"最小值: {ndvi_series.min():.3f} (样点: {ndvi_series.idxmin()})")
print()

print("索引和值:")
print(f"索引: {ndvi_series.index.tolist()}")
print(f"值: {ndvi_series.values.tolist()}")
