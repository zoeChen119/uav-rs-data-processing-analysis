import pandas as pd

# 创建示例DataFrame
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9]
}
df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 选择单列
print(f"\nNDVI列:")
print(df['NDVI'])

# 选择多列
print(f"\n样点ID和NDVI:")
print(df[['样点ID', 'NDVI']])

# 添加新列
df['NDVI百分比'] = df['NDVI'] * 100
print(f"\n添加NDVI百分比列:")
print(df[['样点ID', 'NDVI', 'NDVI百分比']])

# 删除列
df_drop = df.drop(columns=['NDVI百分比'])
print(f"\n删除NDVI百分比列:")
print(df_drop.columns.tolist())

# 重命名列
df_renamed = df.rename(columns={'NDVI': '归一化植被指数',
                                 '温度': '地表温度'})
print(f"\n重命名后的列名:")
print(df_renamed.columns.tolist())