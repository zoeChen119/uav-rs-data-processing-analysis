import pandas as pd
import numpy as np

# 创建含异常值的无人机样点数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 
               'S006', 'S007', 'S008', 'S009', 'S010'],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 
             0.75, 0.63, 0.88, 0.71, 0.79],
    'LST': [28.5, 29.1, 27.3, 30.2, 26.5, 
            31.0, 25.8, 45.0, 27.9, 28.3],
    '温度': [25.3, 26.8, 24.9, 27.5, 26.1, 
             28.0, 25.2, 29.3, 26.7, 27.2]
}
df = pd.DataFrame(data).set_index('样点ID')

# 模拟：在S008的LST数据中加入异常值
df.loc['S008', 'LST'] = 45.0

# 数据质量评估
print("数据质量评估:")
print("-" * 40)

# 缺失值检测
print("1. 缺失值检测:")
print(df.isnull().sum())

# 重复值检测
print("\n2. 重复值检测:")
print(f"  重复行数: {df.duplicated().sum()}")

# 数据类型检查
print("\n3. 数据类型检查:")
print(df.dtypes)

# 异常值检测（基于IQR方法）
print("\n4. 异常值检测（IQR方法）:")
Q1 = df['LST'].quantile(0.25)
Q3 = df['LST'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"  LST Q1: {Q1:.2f}℃")
print(f"  LST Q3: {Q3:.2f}℃")
print(f"  LST IQR: {IQR:.2f}℃")
print(f"  LST 正常范围: [{lower_bound:.2f}, {upper_bound:.2f}]")

# 识别异常值
outliers = df[(df['LST'] < lower_bound) | (df['LST'] > upper_bound)]
print(f"  异常值数量: {len(outliers)}")
print("  异常值样点:")
print(outliers[['NDVI', 'LST', '温度']])

# 异常值处理（替换为中位数）
df_clean = df.copy()
lst_median = df_clean['LST'].median()
df_clean.loc[outliers.index, 'LST'] = lst_median

print(f"\n5. 异常值处理:")
print(f"  LST中位数: {lst_median:.2f}℃")
print(f"  替换后的LST值:")
print(df_clean.loc[outliers.index, ['NDVI', 'LST', '温度']])