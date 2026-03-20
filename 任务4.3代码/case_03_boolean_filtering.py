"""
案例3：布尔索引条件筛选
教材：《无人机遥感数据处理与分析》第四章 任务4.3
演示布尔索引的各种筛选方法：单条件、多条件、isin()、query()
"""

import pandas as pd

# 创建无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006'],
    '区域': ['A', 'A', 'B', 'B', 'C', 'C'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3],
    '地物类型': ['农田', '农田', '林地', '林地', '裸土', '裸土']
}
df = pd.DataFrame(data).set_index('样点ID')

# 单条件筛选
print("单条件筛选：NDVI > 0.7 的样点")
high_ndvi = df[df['NDVI'] > 0.7]
print(high_ndvi)

# 多条件筛选（与）
print("\n多条件筛选：区域为A且NDVI > 0.65")
condition_a = (df['区域'] == 'A') & (df['NDVI'] > 0.65)
result_a = df[condition_a]
print(result_a)

# 多条件筛选（或）
print("\n多条件筛选：区域为B或NDVI > 0.7")
condition_b = (df['区域'] == 'B') | (df['NDVI'] > 0.7)
result_b = df[condition_b]
print(result_b)

# 使用isin方法
print("\n使用isin方法：选择特定地物类型")
selected_types = ['农田', '林地']
result_types = df[df['地物类型'].isin(selected_types)]
print(result_types)

# 使用query方法
print("\n使用query方法：NDVI > 0.7且温度 < 30")
query_result = df.query("NDVI > 0.7 and 温度 < 30")
print(query_result)