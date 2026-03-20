import pandas as pd
import numpy as np

# ========== 第一步：创建无人机遥感样点数据 ==========
print("第一步：创建无人机遥感样点数据")
print("=" * 50)

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
print("无人机遥感样点数据:")
print(df)
print(f"\n数据形状: {df.shape}")

# ========== 第二步：基本统计量计算 ==========
print("\n第二步：基本统计量计算")
print("=" * 50)

# 计算NDVI的基本统计量
print("NDVI基本统计量:")
print(f"  平均值: {df['NDVI'].mean():.4f}")
print(f"  中位数: {df['NDVI'].median():.4f}")
print(f"  标准差: {df['NDVI'].std():.4f}")
print(f"  最小值: {df['NDVI'].min():.4f}")
print(f"  最大值: {df['NDVI'].max():.4f}")
print(f"  极差: {df['NDVI'].max() - df['NDVI'].min():.4f}")

# 计算LST的基本统计量
print("\nLST基本统计量:")
print(f"  平均值: {df['LST'].mean():.2f}℃")
print(f"  中位数: {df['LST'].median():.2f}℃")
print(f"  标准差: {df['LST'].std():.2f}℃")

# 批量计算所有数值列的统计量
print("\n所有数值列的统计摘要:")
print(df.describe())

# ========== 第三步：分组统计分析 ==========
print("\n第三步：分组统计分析")
print("=" * 50)

# 按区域分组统计
print("按区域分组统计（NDVI和温度）:")
grouped_area = df.groupby('区域')[['NDVI', 'LST', '温度']].mean()
print(grouped_area)

# 按地物类型分组统计
print("\n按地物类型分组统计（NDVI和LST）:")
grouped_type = df.groupby('地物类型')[['NDVI', 'LST']].agg(['mean', 'std'])
print(grouped_type)

# 各区域样点数量
print("\n各区域样点数量:")
count_by_area = df.groupby('区域').size()
print(count_by_area)

# ========== 第四步：数据质量评估 ==========
print("\n第四步：数据质量评估")
print("=" * 50)

# 缺失值检测
print("1. 缺失值检测:")
missing_values = df.isnull().sum()
print(missing_values)

# 重复值检测
print("\n2. 重复值检测:")
duplicate_count = df.duplicated().sum()
print(f"  重复行数: {duplicate_count}")

# 数据类型检查
print("\n3. 数据类型检查:")
print(df.dtypes)

# ========== 第五步：异常值检测与处理 ==========
print("\n第五步：异常值检测与处理")
print("=" * 50)

# 使用IQR方法检测LST异常值
Q1 = df['LST'].quantile(0.25)
Q3 = df['LST'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("LST异常值检测（IQR方法）:")
print(f"  Q1: {Q1:.2f}℃")
print(f"  Q3: {Q3:.2f}℃")
print(f"  IQR: {IQR:.2f}℃")
print(f"  正常范围: [{lower_bound:.2f}, {upper_bound:.2f}]℃")

# 识别异常值
outliers = df[(df['LST'] < lower_bound) | (df['LST'] > upper_bound)]
print(f"\n异常值数量: {len(outliers)}")

if len(outliers) > 0:
    print("异常值样点:")
    print(outliers[['区域', '地物类型', 'NDVI', 'LST', '温度']])
    
    # 处理异常值（替换为中位数）
    df_clean = df.copy()
    lst_median = df_clean['LST'].median()
    df_clean.loc[outliers.index, 'LST'] = lst_median
    
    print(f"\n异常值处理（替换为LST中位数）:")
    print(f"  LST中位数: {lst_median:.2f}℃")
    print("  处理后的LST值:")
    print(df_clean.loc[outliers.index, ['NDVI', 'LST', '温度']])
else:
    df_clean = df.copy()
    print("  未发现异常值")

# ========== 第六步：统计结果汇总 ==========
print("\n第六步：统计结果汇总")
print("=" * 50)

print("汇总统计结果:")
print("-" * 40)

print("1. NDVI分布特征:")
print(f"   平均NDVI为{df['NDVI'].mean():.3f}，表明区域植被状况{'' if df['NDVI'].mean() > 0.7 else ''}良好")
print(f"   NDVI标准差为{df['NDVI'].std():.4f}，表明植被覆盖度分布相对{'均匀' if df['NDVI'].std() < 0.1 else '分散'}")

print("\n2. 区域间差异:")
area_ndvi = df.groupby('区域')['NDVI'].mean()
highest_area = area_ndvi.idxmax()
lowest_area = area_ndvi.idxmin()
print(f"   {highest_area}区域NDVI最高({area_ndvi[highest_area]:.3f})")
print(f"   {lowest_area}区域NDVI最低({area_ndvi[lowest_area]:.3f})")
print(f"   区域间差异为{area_ndvi[highest_area] - area_ndvi[lowest_area]:.3f}")

print("\n3. 地物类型间差异:")
type_ndvi = df.groupby('地物类型')['NDVI'].mean()
print(type_ndvi)

print("\n4. 数据质量评估:")
if missing_values.sum() == 0 and duplicate_count == 0:
    print("   数据质量良好，无缺失值和重复值")
else:
    print(f"   数据存在问题：{missing_values.sum()}个缺失值，{duplicate_count}个重复值")

print("\n" + "=" * 50)
print("任务4.5 统计描述分析完成")
print("=" * 50)