import pandas as pd
import numpy as np

# ========== 基础数据（沿用任务4.5）==========
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
             28.0, 25.2, 29.3, 26.7, 27.2],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9,
             60.5, 70.2, 53.7, 62.4, 57.9]
}

df = pd.DataFrame(data).set_index('样点ID')

# ========== （1）湿度变异系数 ==========
print("（1）湿度变异系数")
print("=" * 50)

humidity_mean = df['湿度'].mean()
humidity_std = df['湿度'].std()
cv = humidity_std / humidity_mean

print(f"湿度平均值: {humidity_mean:.4f}")
print(f"湿度标准差: {humidity_std:.4f}")
print(f"湿度变异系数(CV): {cv:.4f} ({cv*100:.2f}%)")
if cv < 0.1:
    print("离散程度评估: 变异系数较小，湿度数据离散程度低，分布较均匀")
elif cv < 0.3:
    print("离散程度评估: 变异系数中等，湿度数据存在一定离散程度")
else:
    print("离散程度评估: 变异系数较大，湿度数据离散程度高，分布不均匀")

# ========== （2）NDVI最高和最低样点 ==========
print("\n（2）NDVI最高和最低样点")
print("=" * 50)

ndvi_max_idx = df['NDVI'].idxmax()
ndvi_min_idx = df['NDVI'].idxmin()

print(f"NDVI最高样点 ({ndvi_max_idx}):")
print(df.loc[ndvi_max_idx])

print(f"\nNDVI最低样点 ({ndvi_min_idx}):")
print(df.loc[ndvi_min_idx])

# ========== （3）多级分组统计 ==========
print("\n（3）按区域和地物类型多级分组统计")
print("=" * 50)

multi_grouped = df.groupby(['区域', '地物类型'])[['NDVI', '温度']].agg(['mean', 'max'])
print(multi_grouped)

# ========== （4）NDVI四分位数与异常值判断 ==========
print("\n（4）NDVI四分位数与异常值判断")
print("=" * 50)

Q1 = df['NDVI'].quantile(0.25)
Q2 = df['NDVI'].quantile(0.50)
Q3 = df['NDVI'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Q1 (25%分位数): {Q1:.4f}")
print(f"Q2 (50%分位数/中位数): {Q2:.4f}")
print(f"Q3 (75%分位数): {Q3:.4f}")
print(f"IQR: {IQR:.4f}")
print(f"异常值判定范围: [{lower_bound:.4f}, {upper_bound:.4f}]")

outliers = df[(df['NDVI'] < lower_bound) | (df['NDVI'] > upper_bound)]
if len(outliers) > 0:
    print(f"\n存在 {len(outliers)} 个NDVI异常值:")
    print(outliers[['区域', '地物类型', 'NDVI']])
else:
    print("\nNDVI数据中未发现异常值")
