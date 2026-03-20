"""
案例4：多级索引操作
教材：《无人机遥感数据处理与分析》第四章 任务4.3
演示多级索引的创建与查询操作
"""

import pandas as pd

# 创建无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006'],
    '区域': ['A', 'A', 'B', 'B', 'C', 'C'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3]
}
df = pd.DataFrame(data)

# 设置多级索引
df_multi = df.set_index(['区域', '样点ID'])
print("多级索引DataFrame（区域-样点ID）:")
print(df_multi)

# 按顶层索引查询
print("\n区域A的所有样点:")
print(df_multi.loc['A'])

# 按完整索引查询
print("\n区域B的样点S004:")
print(df_multi.loc[('B', 'S004')])

# 使用xs方法查询
print("\n使用xs选择区域C的所有样点:")
print(df_multi.xs('C', level='区域'))

# 多级索引切片
print("\n区域A和B的所有样点:")
print(df_multi.loc[['A', 'B']])