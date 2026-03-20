"""
任务4.2：Pandas数据结构之DataFrame - 创建示例
教材：《无人机遥感数据处理与分析》第四章
作者：[你的姓名]
日期：2026年3月

本文件演示Pandas DataFrame数据结构的创建方法
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("任务4.2：Pandas数据结构之DataFrame - 创建方法演示")
print("=" * 60)

# ============================================================================
# 1. 从字典创建DataFrame
# ============================================================================
print("\n1. 从字典创建DataFrame")
print("-" * 40)

# 创建无人机遥感监测数据字典
remote_data_dict = {
    '样点编号': ['S001', 'S002', 'S003', 'S004', 'S005'],
    '经度': [116.4074, 116.4085, 116.4096, 116.4107, 116.4118],
    '纬度': [39.9042, 39.9053, 39.9064, 39.9075, 39.9086],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9]
}

df_from_dict = pd.DataFrame(remote_data_dict)
print("从字典创建的DataFrame（无人机遥感数据）:")
print(df_from_dict)
print(f"\nDataFrame形状: {df_from_dict.shape}")
print(f"列名: {df_from_dict.columns.tolist()}")
print(f"索引: {df_from_dict.index.tolist()}")

# ============================================================================
# 2. 从列表创建DataFrame
# ============================================================================
print("\n\n2. 从列表创建DataFrame")
print("-" * 40)

# 创建数据列表
data_list = [
    ['S001', 116.4074, 39.9042, 0.65, 25.3, 65.2],
    ['S002', 116.4085, 39.9053, 0.72, 28.7, 58.7],
    ['S003', 116.4096, 39.9064, 0.58, 23.9, 72.3],
    ['S004', 116.4107, 39.9075, 0.81, 30.1, 55.8],
    ['S005', 116.4118, 39.9086, 0.69, 26.5, 68.9]
]

columns = ['样点编号', '经度', '纬度', 'NDVI', '温度', '湿度']
df_from_list = pd.DataFrame(data_list, columns=columns)
print("从列表创建的DataFrame:")
print(df_from_list)

# 指定索引
df_with_index = pd.DataFrame(data_list, columns=columns, index=['A', 'B', 'C', 'D', 'E'])
print("\n指定自定义索引的DataFrame:")
print(df_with_index)

# ============================================================================
# 3. 从NumPy数组创建DataFrame
# ============================================================================
print("\n\n3. 从NumPy数组创建DataFrame")
print("-" * 40)

# 创建NumPy数组
np_data = np.array([
    [0.65, 25.3, 65.2],
    [0.72, 28.7, 58.7],
    [0.58, 23.9, 72.3],
    [0.81, 30.1, 55.8],
    [0.69, 26.5, 68.9]
])

df_from_np = pd.DataFrame(np_data, columns=['NDVI', '温度', '湿度'], index=['S001', 'S002', 'S003', 'S004', 'S005'])
print("从NumPy数组创建的DataFrame:")
print(df_from_np)
print(f"\nNumPy数组形状: {np_data.shape}")
print(f"DataFrame形状: {df_from_np.shape}")

# ============================================================================
# 4. 从Series创建DataFrame
# ============================================================================
print("\n\n4. 从Series创建DataFrame")
print("-" * 40)

# 创建多个Series
ndvi_series = pd.Series([0.65, 0.72, 0.58, 0.81, 0.69], name='NDVI', index=['S001', 'S002', 'S003', 'S004', 'S005'])
temp_series = pd.Series([25.3, 28.7, 23.9, 30.1, 26.5], name='温度', index=['S001', 'S002', 'S003', 'S004', 'S005'])
humidity_series = pd.Series([65.2, 58.7, 72.3, 55.8, 68.9], name='湿度', index=['S001', 'S002', 'S003', 'S004', 'S005'])

# 从Series字典创建DataFrame
df_from_series = pd.DataFrame({'NDVI': ndvi_series, '温度': temp_series, '湿度': humidity_series})
print("从Series创建的DataFrame:")
print(df_from_series)

# ============================================================================
# 5. 创建包含缺失值的DataFrame
# ============================================================================
print("\n\n5. 创建包含缺失值的DataFrame")
print("-" * 40)

# 创建包含缺失值的数据
data_with_nan = {
    '样点编号': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'NDVI': [0.65, np.nan, 0.58, 0.81, np.nan],
    '温度': [25.3, 28.7, np.nan, 30.1, 26.5],
    '湿度': [65.2, 58.7, 72.3, np.nan, 68.9]
}

df_with_nan = pd.DataFrame(data_with_nan)
print("包含缺失值的DataFrame:")
print(df_with_nan)
print(f"\n各列缺失值数量:")
print(df_with_nan.isna().sum())
print(f"\n总缺失值数量: {df_with_nan.isna().sum().sum()}")

# ============================================================================
# 6. 创建时间序列DataFrame
# ============================================================================
print("\n\n6. 创建时间序列DataFrame")
print("-" * 40)

# 创建时间索引
dates = pd.date_range('2026-03-01', periods=5, freq='D')

# 创建时间序列数据
time_series_data = {
    'NDVI': [0.65, 0.68, 0.72, 0.70, 0.75],
    '温度': [25.3, 26.1, 27.3, 26.9, 28.5],
    '湿度': [65.2, 63.8, 61.3, 64.2, 59.7]
}

df_time_series = pd.DataFrame(time_series_data, index=dates)
print("时间序列DataFrame（无人机连续监测数据）:")
print(df_time_series)
print(f"\n索引类型: {type(df_time_series.index)}")
print(f"时间范围: {df_time_series.index[0]} 到 {df_time_series.index[-1]}")

# ============================================================================
# 7. 创建多级索引DataFrame
# ============================================================================
print("\n\n7. 创建多级索引DataFrame")
print("-" * 40)

# 创建多级索引
arrays = [
    ['区域A', '区域A', '区域A', '区域B', '区域B', '区域B'],
    ['样点1', '样点2', '样点3', '样点1', '样点2', '样点3']
]

index = pd.MultiIndex.from_arrays(arrays, names=['区域', '样点'])

# 创建数据
multi_index_data = {
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9, 60.5]
}

df_multi_index = pd.DataFrame(multi_index_data, index=index)
print("多级索引DataFrame（按区域和样点组织）:")
print(df_multi_index)
print(f"\n索引级别: {df_multi_index.index.names}")
print(f"索引值:")
print(df_multi_index.index.tolist())

# ============================================================================
# 8. 无人机遥感数据综合示例
# ============================================================================
print("\n\n8. 无人机遥感数据综合示例")
print("-" * 40)

print("8.1 创建完整的无人机遥感监测数据集:")

# 模拟更复杂的无人机遥感数据
complete_remote_data = {
    '飞行时间': pd.date_range('2026-03-17 08:00', periods=8, freq='H'),
    '飞行高度': [125.6, 130.2, 128.7, 135.3, 132.8, 140.1, 138.5, 142.3],
    '飞行速度': [12.5, 13.2, 12.8, 14.1, 13.7, 15.2, 14.8, 15.6],
    'NDVI': [0.65, 0.68, 0.72, 0.70, 0.75, 0.78, 0.81, 0.79],
    '地表温度': [25.3, 26.1, 27.3, 26.9, 28.5, 29.1, 30.2, 29.7],
    '土壤湿度': [65.2, 63.8, 61.3, 64.2, 59.7, 58.9, 57.3, 58.5],
    '植被覆盖度': [85.6, 87.2, 89.5, 86.8, 91.2, 92.7, 94.1, 93.3]
}

df_complete = pd.DataFrame(complete_remote_data)
print("完整的无人机遥感监测DataFrame:")
print(df_complete)
print(f"\n数据形状: {df_complete.shape}")
print(f"列数据类型:")
print(df_complete.dtypes)

# ============================================================================
# 9. DataFrame属性查看方法
# ============================================================================
print("\n\n9. DataFrame属性查看方法")
print("-" * 40)

print("9.1 基本信息查看:")
print(f"形状: {df_complete.shape}")
print(f"列名: {df_complete.columns.tolist()}")
print(f"索引: {df_complete.index.tolist()}")
print(f"数据类型:\n{df_complete.dtypes}")

print("\n9.2 数据概览:")
print("前3行数据:")
print(df_complete.head(3))

print("\n后3行数据:")
print(df_complete.tail(3))

print("\n9.3 数据信息:")
print(df_complete.info())

print("\n9.4 描述性统计:")
print(df_complete.describe())

# ============================================================================
# 10. 总结与练习
# ============================================================================
print("\n\n10. 总结与练习")
print("-" * 40)

print("""
本章学习了DataFrame的多种创建方法：

1. 从字典创建：最常用的方法，字典键成为列名
2. 从列表创建：需要指定列名
3. 从NumPy数组创建：高效处理数值数据
4. 从Series创建：多个Series组合成DataFrame
5. 创建包含缺失值的DataFrame：使用np.nan
6. 创建时间序列DataFrame：使用时间索引
7. 创建多级索引DataFrame：复杂数据组织

DataFrame属性查看方法：
1. shape：数据形状
2. columns：列名
3. index：索引
4. dtypes：数据类型
5. head()/tail()：查看首尾数据
6. info()：数据信息
7. describe()：描述性统计

练习建议：
1. 创建一个包含无人机飞行参数的DataFrame
2. 创建一个包含时间序列的遥感监测DataFrame
3. 练习使用各种属性查看方法
""")

# 练习示例
print("\n练习示例：创建无人机飞行数据DataFrame")
print("=" * 40)

# 练习：创建无人机飞行数据
flight_data = {
    '航点': [f'WP{i+1:03d}' for i in range(10)],
    '经度': [116.4 + i*0.001 for i in range(10)],
    '纬度': [39.9 + i*0.001 for i in range(10)],
    '高度': [100 + i*5 for i in range(10)],
    '速度': [10 + i*0.5 for i in range(10)],
    '拍摄状态': ['成功', '成功', '失败', '成功', '成功', '成功', '失败', '成功', '成功', '成功']
}

df_flight = pd.DataFrame(flight_data)
print("无人机飞行数据DataFrame:")
print(df_flight)

print("\n数据统计信息:")
print(f"总航点数: {len(df_flight)}")
print(f"成功拍摄数: {(df_flight['拍摄状态'] == '成功').sum()}")
print(f"平均飞行高度: {df_flight['高度'].mean():.1f}m")
print(f"平均飞行速度: {df_flight['速度'].mean():.1f}m/s")

print("\n" + "=" * 60)
print("任务4.2 DataFrame创建示例结束")
print("=" * 60)