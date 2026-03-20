import pandas as pd
import numpy as np

# 创建NumPy数组
np_data = np.array([
    [0.65, 25.3, 65.2],
    [0.72, 28.7, 58.7],
    [0.58, 23.9, 72.3],
    [0.81, 30.1, 55.8],
    [0.69, 26.5, 68.9]
])

df_from_np = pd.DataFrame(np_data, columns=['NDVI', '温度', '湿度'],
                        index=['S001', 'S002', 'S003', 'S004', 'S005'])
print("从NumPy数组创建的DataFrame:")
print(df_from_np)
print(f"\nNumPy数组形状: {np_data.shape}")
print(f"DataFrame形状: {df_from_np.shape}")