import pandas as pd

# 创建示例DataFrame
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5]
}
df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 选择行（按位置）
print(f"\n前3行数据:")
print(df.iloc[:3])

# 选择行（按条件）
print(f"\nNDVI>0.7的样点:")
print(df[df['NDVI'] > 0.7])

# 修改单个值
df_modified = df.copy()
df_modified.loc[0, 'NDVI'] = 0.68
print(f"\n修改S001的NDVI值为0.68:")
print(df_modified[['样点ID', 'NDVI']].head())

# 批量修改（温度单位转换）
df_modified['温度_华氏度'] = df_modified['温度'] * 9/5 + 32
print(f"\n添加华氏温度列:")
print(df_modified[['样点ID', '温度', '温度_华氏度']].head())

# 条件修改（修正异常湿度）
df_modified['湿度修正'] = df_modified['温度']  # 模拟湿度列
df_modified.loc[df_modified['湿度修正'] < 50, '湿度修正'] = 50
print(f"\n修正后的湿度数据（将低于50的设为50）:")
print(df_modified[['样点ID', '温度', '湿度修正']])