import pandas as pd
import numpy as np

# 创建无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 
               'S006', 'S007', 'S008', 'S009', 'S010'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 
             0.75, 0.63, 0.88, 0.71, 0.79],
    'LST': [28.5, 29.1, 27.3, 30.2, 26.5, 
            31.0, 25.8, 32.5, 27.9, 28.3],
    '温度': [25.3, 26.8, 24.9, 27.5, 26.1, 
             28.0, 25.2, 29.3, 26.7, 27.2]
}
df = pd.DataFrame(data).set_index('样点ID')

# 计算基本统计量
print("NDVI基本统计量:")
print(f"  平均值: {df['NDVI'].mean():.4f}")
print(f"  中位数: {df['NDVI'].median():.4f}")
print(f"  标准差: {df['NDVI'].std():.4f}")
print(f"  最小值: {df['NDVI'].min():.4f}")
print(f"  最大值: {df['NDVI'].max():.4f}")
print(f"  极差: {df['NDVI'].max() - df['NDVI'].min():.4f}")

print("\n温度基本统计量:")
print(f"  平均值: {df['温度'].mean():.2f}℃")
print(f"  中位数: {df['温度'].median():.2f}℃")
print(f"  标准差: {df['温度'].std():.2f}℃")
print(f"  第25百分位: {df['温度'].quantile(0.25):.2f}℃")
print(f"  第75百分位: {df['温度'].quantile(0.75):.2f}℃")

# 批量计算所有数值列的统计量
print("\n所有数值列的基本统计量:")
print(df[['NDVI', 'LST', '温度']].describe())