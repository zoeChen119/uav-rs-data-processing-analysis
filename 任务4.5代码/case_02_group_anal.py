import pandas as pd

# 创建无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 
               'S006', 'S007', 'S008', 'S009', 'S010'],
    '区域': ['A', 'A', 'A', 'B', 'B', 
             'B', 'C', 'C', 'C', 'C'],
    '地物类型': ['农田', '农田', '裸土', '农田', '林地', 
                 '裸土', '农田', '林地', '农田', '裸土'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 
             0.75, 0.63, 0.88, 0.71, 0.79],
    'LST': [28.5, 29.1, 27.3, 30.2, 26.5, 
            31.0, 25.8, 32.5, 27.9, 28.3],
    '温度': [25.3, 26.8, 24.9, 27.5, 26.1, 
             28.0, 25.2, 29.3, 26.7, 27.2]
}
df = pd.DataFrame(data).set_index('样点ID')

# 按区域分组统计
print("按区域分组统计（NDVI和温度）:")
grouped_area = df.groupby('区域')[['NDVI', '温度']].mean()
print(grouped_area)

# 按地物类型分组统计
print("\n按地物类型分组统计（NDVI和LST）:")
grouped_type = df.groupby('地物类型')[['NDVI', 'LST']].agg(['mean', 'std'])
print(grouped_type)

# 按区域和地物类型多级分组统计
print("\n按区域和地物类型分组统计:")
grouped_multi = df.groupby(['区域', '地物类型'])[['NDVI', '温度']].mean()
print(grouped_multi)

# 按区域统计样点数量
print("\n各区域样点数量:")
count_by_area = df.groupby('区域').size()
print(count_by_area)