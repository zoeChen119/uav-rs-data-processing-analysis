import pandas as pd

# 创建示例DataFrame（包含区域、样点等信息）
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'],
    '区域': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63, 0.88],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3, 24.8, 31.2],
    '植被覆盖度': [85.6, 92.3, 78.4, 94.1, 89.2, 91.7, 83.5, 96.8]
}
df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 按单列排序
print(f"\n按NDVI降序排序:")
print(df.sort_values('NDVI', ascending=False)[['样点ID', '区域', 'NDVI']])

# 按多列排序
print(f"\n按区域升序、NDVI降序排序:")
print(df.sort_values(['区域', 'NDVI'],
                     ascending=[True, False])[['样点ID', '区域', 'NDVI']])

# 分组统计
print(f"\n各区域样点数量:")
print(df.groupby('区域').size())

print(f"\n各区域NDVI平均值:")
print(df.groupby('区域')['NDVI'].mean())

print(f"\n各区域温度和湿度的统计描述:")
area_stats = df.groupby('区域')[['温度', '植被覆盖度']].agg(['mean', 'std', 'min', 'max'])
print(area_stats)

# 数据透视表
pivot_table = pd.pivot_table(df, values='NDVI', index='区域',
                            columns='植被覆盖度等级',
                            aggfunc='mean', fill_value=0)
print(f"\n各区域不同覆盖度等级的平均NDVI:")
print(pivot_table)