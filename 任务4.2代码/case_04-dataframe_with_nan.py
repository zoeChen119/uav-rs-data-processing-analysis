import pandas as pd
import numpy as np

# 创建包含缺失值的数据
data_with_nan = {
    '样点编号': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'NDVI': [0.65, np.nan, 0.58, 0.81, np.nan],
    '温度': [25.3, 28.7, np.nan, 30.1, 26.5],
    '湿度': [65.2, 58.7, 72.3, np.nan, 68.9]
}

df_with_nan = pd.DataFrame(data_with_nan)
print("包含缺失值的DataFrame:")
print(df_with_nan)
print(f"\n各列缺失值数量:")
print(df_with_nan.isna().sum())
print(f"\n总缺失值数量: {df_with_nan.isna().sum().sum()}")