import pandas as pd
import numpy as np

# ========== 第一步：创建无人机遥感监测DataFrame ==========
print("第一步：创建无人机遥感监测DataFrame")
print("=" * 50)

data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 
               'S006', 'S007', 'S008', 'S009', 'S010'],
    '区域': ['A', 'A', 'A', 'B', 'B', 
             'B', 'C', 'C', 'C', 'C'],
    '日期': pd.date_range('2026-03-10', periods=10, freq='D'),
    '经度': [116.4074, 116.4085, 116.4096, 116.4107, 116.4118,
             116.4129, 116.4130, 116.4141, 116.4152, 116.4163],
    '纬度': [39.9042, 39.9053, 39.9064, 39.9075, 39.9086,
             39.9097, 39.9108, 39.9119, 39.9120, 39.9131],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 
             0.75, 0.63, 0.88, 0.71, 0.79],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 
             29.3, 24.8, 31.2, 27.8, 29.5],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9, 
             60.5, 70.2, 53.7, 62.4, 57.9],
    '地物类型': ['农田', '农田', '裸土', '农田', '林地', 
                 '裸土', '农田', '林地', '农田', '裸土']
}

# 设置样点ID为索引
df = pd.DataFrame(data).set_index('样点ID')
print("无人机遥感监测数据（样点ID为索引）:")
print(df)
print(f"\n数据形状: {df.shape}")

# ========== 第二步：loc标签索引操作 ==========
print("\n第二步：loc标签索引操作")
print("=" * 50)

# 2.1 选择单个行
print("2.1 选择单个行（样点S003）:")
print(df.loc['S003'])

# 2.2 选择多个行
print("\n2.2 选择多个行（样点S001, S004, S007）:")
print(df.loc[['S001', 'S004', 'S007']])

# 2.3 选择行范围
print("\n2.3 选择行范围（样点S002到S005）:")
print(df.loc['S002':'S005'])

# 2.4 选择行和列
print("\n2.4 选择特定行和列（样点S001-S003的NDVI和温度）:")
print(df.loc['S001':'S003', ['NDVI', '温度']])

# 2.5 选择所有行的特定列
print("\n2.5 选择所有行的地理位置:")
print(df.loc[:, ['经度', '纬度']])

# ========== 第三步：iloc位置索引操作 ==========
print("\n第三步：iloc位置索引操作")
print("=" * 50)

# 3.1 选择单个行
print("3.1 选择单个行（第2行）:")
print(df.iloc[2])

# 3.2 选择多个行
print("\n3.2 选择多个行（第0, 3, 6行）:")
print(df.iloc[[0, 3, 6]])

# 3.3 选择行范围
print("\n3.3 选择行范围（第2到第5行）:")
print(df.iloc[2:5])

# 3.4 选择行和列
print("\n3.4 选择行和列（第1-4行，第2-5列）:")
print(df.iloc[1:5, 2:5])

# ========== 第四步：布尔索引条件筛选 ==========
print("\n第四步：布尔索引条件筛选")
print("=" * 50)

# 4.1 单条件筛选
print("4.1 单条件筛选（NDVI大于0.7）:")
high_ndvi = df[df['NDVI'] > 0.7]
print(high_ndvi[['区域', 'NDVI', '温度']])

# 4.2 多条件筛选（与）
print("\n4.2 多条件筛选（区域为A且NDVI>0.65）:")
condition_a = (df['区域'] == 'A') & (df['NDVI'] > 0.65)
result_a = df[condition_a]
print(result_a[['区域', 'NDVI', '温度']])

# 4.3 多条件筛选（或）
print("\n4.3 多条件筛选（温度高于30或湿度低于60）:")
condition_b = (df['温度'] > 30) | (df['湿度'] < 60)
result_b = df[condition_b]
print(result_b[['区域', '温度', '湿度', 'NDVI']])

# 4.4 使用isin方法
print("\n4.4 使用isin方法（选择特定区域）:")
selected_areas = ['A', 'C']
area_filter = df[df['区域'].isin(selected_areas)]
print(area_filter)

# 4.5 使用query方法
print("\n4.5 使用query方法（NDVI>0.7且温度<30）:")
query_result = df.query("NDVI > 0.7 and 温度 < 30")
print(query_result[['区域', 'NDVI', '温度']])

# ========== 第五步：多级索引操作 ==========
print("\n第五步：多级索引操作")
print("=" * 50)

# 5.1 创建多级索引
df_multi = df.reset_index().set_index(['区域', '样点ID'])
print("多级索引DataFrame:")
print(df_multi)

# 5.2 按顶层索引查询
print("\n区域A的所有样点:")
print(df_multi.loc['A'])

# 5.3 按完整索引查询
print("\n区域B的样点S004:")
print(df_multi.loc[('B', 'S004')])

# 5.4 使用xs方法
print("\n使用xs选择区域C的所有样点:")
print(df_multi.xs('C', level='区域'))