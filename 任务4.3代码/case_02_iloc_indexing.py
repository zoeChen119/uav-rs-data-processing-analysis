"""
案例2：使用iloc进行位置索引
教材：《无人机遥感数据处理与分析》第四章 任务4.3
演示iloc索引的基本用法：基于位置的索引操作
"""

import pandas as pd

# 创建无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    '区域': ['A', 'A', 'B', 'B', 'C'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5]
}
df = pd.DataFrame(data)

# 使用iloc选择数据
print("第2行数据（位置索引从0开始）:")
print(df.iloc[1])

print("\n第0行和第3行:")
print(df.iloc[[0, 3]])

print("\n第1到第4行（不包含第4行）:")
print(df.iloc[1:4])

print("\n前2行，前2列:")
print(df.iloc[:2, :2])
