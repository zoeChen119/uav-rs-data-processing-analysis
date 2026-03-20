import pandas as pd

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