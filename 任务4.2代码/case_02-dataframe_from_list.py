import pandas as pd

# 创建数据列表（每个子列表代表一行）
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

# 指定自定义索引
df_with_index = pd.DataFrame(data_list, columns=columns,
                            index=['A', 'B', 'C', 'D', 'E'])
print(f"\n指定自定义索引的DataFrame:")
print(df_with_index)