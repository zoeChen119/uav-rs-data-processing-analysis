"""
任务4.2：Pandas数据结构之DataFrame - 基本操作示例
教材：《无人机遥感数据处理与分析》第四章
作者：[你的姓名]
日期：2026年3月

本文件演示Pandas DataFrame的基本操作方法
包括列操作、行操作、数据修改等
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("任务4.2：Pandas数据结构之DataFrame - 基本操作演示")
print("=" * 60)

# ============================================================================
# 1. 数据准备：创建无人机遥感监测DataFrame
# ============================================================================
print("\n1. 数据准备：无人机遥感监测DataFrame")
print("-" * 40)

# 创建示例数据
data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'],
    '区域': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    '经度': [116.4074, 116.4085, 116.4096, 116.4107, 116.4118, 116.4129, 116.4130, 116.4141],
    '纬度': [39.9042, 39.9053, 39.9064, 39.9075, 39.9086, 39.9097, 39.9108, 39.9119],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63, 0.88],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3, 24.8, 31.2],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9, 60.5, 70.2, 53.7],
    '植被覆盖度': [85.6, 92.3, 78.4, 94.1, 89.2, 91.7, 83.5, 96.8]
}

df = pd.DataFrame(data)
print("原始无人机遥感监测数据:")
print(df)
print(f"\n数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")

# ============================================================================
# 2. 列操作
# ============================================================================
print("\n\n2. 列操作")
print("-" * 40)

# 2.1 选择单列
print("2.1 选择单列（NDVI数据）:")
ndvi_column = df['NDVI']
print(ndvi_column)
print(f"类型: {type(ndvi_column)}")

# 2.2 选择多列
print("\n2.2 选择多列（地理位置和NDVI）:")
location_ndvi = df[['样点ID', '经度', '纬度', 'NDVI']]
print(location_ndvi)

# 2.3 添加新列
print("\n2.3 添加新列（计算温度等级）:")

# 定义温度等级函数
def classify_temperature(temp):
    if temp < 25:
        return '低温'
    elif temp < 30:
        return '适宜'
    else:
        return '高温'

df['温度等级'] = df['温度'].apply(classify_temperature)
print("添加温度等级后的数据:")
print(df[['样点ID', '温度', '温度等级']])

# 2.4 计算派生列
print("\n2.4 计算派生列（植被指数百分比）:")
df['NDVI百分比'] = df['NDVI'] * 100
df['覆盖度等级'] = pd.cut(df['植被覆盖度'], bins=[0, 70, 85, 95, 100],
                         labels=['差', '中', '良', '优'])
print("添加派生列后的数据:")
print(df[['样点ID', 'NDVI', 'NDVI百分比', '植被覆盖度', '覆盖度等级']])

# 2.5 删除列
print("\n2.5 删除列（删除临时计算列）:")
df_copy = df.copy()
df_copy = df_copy.drop(columns=['NDVI百分比'])  # 删除单列
print("删除NDVI百分比列后的数据:")
print(df_copy.columns.tolist())

# 2.6 重命名列
print("\n2.6 重命名列（英文列名改为中文）:")
df_renamed = df.rename(columns={
    'NDVI': '归一化植被指数',
    '温度': '地表温度',
    '湿度': '相对湿度'
})
print("重命名后的列名:")
print(df_renamed.columns.tolist())

# ============================================================================
# 3. 行操作
# ============================================================================
print("\n\n3. 行操作")
print("-" * 40)

# 3.1 选择行（按位置）
print("3.1 选择行（按位置）:")
print("前3行数据:")
print(df.iloc[:3])

print("\n第3到第6行数据:")
print(df.iloc[2:6])

print("\n最后2行数据:")
print(df.iloc[-2:])

# 3.2 选择行（按条件）
print("\n3.2 选择行（按条件）:")

print("NDVI大于0.7的样点:")
high_ndvi = df[df['NDVI'] > 0.7]
print(high_ndvi)

print("\n温度在25-30度之间的样点:")
temp_range = df[(df['温度'] >= 25) & (df['温度'] <= 30)]
print(temp_range)

print("\n区域A且NDVI大于0.6的样点:")
condition = (df['区域'] == 'A') & (df['NDVI'] > 0.6)
area_a_high_ndvi = df[condition]
print(area_a_high_ndvi)

# 3.3 添加新行
print("\n3.3 添加新行（新增样点数据）:")

# 创建新行数据
new_row = {
    '样点ID': 'S009',
    '区域': 'C',
    '经度': 116.4152,
    '纬度': 39.9120,
    'NDVI': 0.71,
    '温度': 27.8,
    '湿度': 62.4,
    '植被覆盖度': 88.6,
    '温度等级': '适宜',
    '覆盖度等级': '良'
}

df_with_new = df._append(new_row, ignore_index=True)
print("添加新行后的数据形状:", df_with_new.shape)
print("新增的样点数据:")
print(df_with_new.tail(1))

# 3.4 删除行
print("\n3.4 删除行（删除特定样点）:")

# 删除NDVI小于0.6的行
df_filtered = df[df['NDVI'] >= 0.6].copy()
print(f"删除低NDVI样点后，剩余样点数: {len(df_filtered)}")
print("删除后的数据:")
print(df_filtered)

# ============================================================================
# 4. 数据修改
# ============================================================================
print("\n\n4. 数据修改")
print("-" * 40)

# 4.1 修改单个值
print("4.1 修改单个值:")
df_modified = df.copy()
df_modified.loc[0, 'NDVI'] = 0.68  # 修改第一行的NDVI值
print("修改S001的NDVI值为0.68:")
print(df_modified[['样点ID', 'NDVI']].head(2))

# 4.2 批量修改列值
print("\n4.2 批量修改列值（温度单位转换）:")
df_modified['温度_华氏度'] = df_modified['温度'] * 9/5 + 32
print("添加华氏温度列:")
print(df_modified[['样点ID', '温度', '温度_华氏度']].head(3))

# 4.3 条件修改
print("\n4.3 条件修改（修正异常湿度值）:")

# 假设湿度低于50%或高于80%为异常
df_modified['湿度修正'] = df_modified['湿度']
df_modified.loc[df_modified['湿度'] < 50, '湿度修正'] = 50
df_modified.loc[df_modified['湿度'] > 80, '湿度修正'] = 80

print("修正后的湿度数据:")
print(df_modified[['样点ID', '湿度', '湿度修正']])

# 4.4 使用apply函数修改
print("\n4.4 使用apply函数修改（植被状况评估）:")

def assess_vegetation(row):
    """评估植被状况"""
    if row['NDVI'] > 0.75 and row['植被覆盖度'] > 90:
        return '优'
    elif row['NDVI'] > 0.65 and row['植被覆盖度'] > 80:
        return '良'
    elif row['NDVI'] > 0.55 and row['植被覆盖度'] > 70:
        return '中'
    else:
        return '差'

df_modified['植被状况'] = df_modified.apply(assess_vegetation, axis=1)
print("植被状况评估结果:")
print(df_modified[['样点ID', 'NDVI', '植被覆盖度', '植被状况']])

# ============================================================================
# 5. 数据排序
# ============================================================================
print("\n\n5. 数据排序")
print("-" * 40)

# 5.1 按单列排序
print("5.1 按单列排序（按NDVI降序）:")
df_sorted_ndvi = df.sort_values('NDVI', ascending=False)
print("按NDVI降序排序:")
print(df_sorted_ndvi[['样点ID', '区域', 'NDVI']])

# 5.2 按多列排序
print("\n5.2 按多列排序（先按区域，再按NDVI降序）:")
df_sorted_multi = df.sort_values(['区域', 'NDVI'], ascending=[True, False])
print("按区域升序、NDVI降序排序:")
print(df_sorted_multi[['样点ID', '区域', 'NDVI']])

# 5.3 按索引排序
print("\n5.3 按索引排序:")
df_reset = df.reset_index(drop=True)  # 重置索引
df_sorted_index = df_reset.sort_index(ascending=False)  # 按索引降序
print("按索引降序排序（前3行）:")
print(df_sorted_index.head(3))

# ============================================================================
# 6. 数据分组与聚合
# ============================================================================
print("\n\n6. 数据分组与聚合")
print("-" * 40)

# 6.1 按区域分组
print("6.1 按区域分组统计:")

grouped_by_area = df.groupby('区域')
print("各区域样点数量:")
print(grouped_by_area.size())

print("\n各区域NDVI平均值:")
print(grouped_by_area['NDVI'].mean())

print("\n各区域温度和湿度的统计描述:")
area_stats = grouped_by_area[['温度', '湿度']].agg(['mean', 'std', 'min', 'max'])
print(area_stats)

# 6.2 多列分组
print("\n6.2 按区域和温度等级分组:")

if '温度等级' in df.columns:
    grouped_multi = df.groupby(['区域', '温度等级'])
    print("各区域温度等级的样点数量:")
    print(grouped_multi.size())

# 6.3 自定义聚合函数
print("\n6.3 自定义聚合函数（计算变异系数）:")

def coefficient_of_variation(series):
    """计算变异系数（标准差/均值）"""
    return series.std() / series.mean() * 100

area_cv = df.groupby('区域')['NDVI'].agg(['mean', 'std', coefficient_of_variation])
area_cv = area_cv.rename(columns={'coefficient_of_variation': '变异系数(%)'})
print("各区域NDVI变异系数:")
print(area_cv)

# ============================================================================
# 7. 数据透视表
# ============================================================================
print("\n\n7. 数据透视表")
print("-" * 40)

# 7.1 创建透视表
print("7.1 创建透视表（区域 vs 温度等级）:")

if '温度等级' in df.columns:
    pivot_table = pd.pivot_table(df,
                                values='NDVI',
                                index='区域',
                                columns='温度等级',
                                aggfunc='mean',
                                fill_value=0)
    print("各区域不同温度等级的平均NDVI:")
    print(pivot_table)

# 7.2 多值透视表
print("\n7.2 多值透视表:")

pivot_multi = pd.pivot_table(df,
                            values=['NDVI', '温度', '湿度'],
                            index='区域',
                            aggfunc={'NDVI': 'mean', '温度': ['min', 'max'], '湿度': 'mean'})
print("各区域多指标统计:")
print(pivot_multi)

# ============================================================================
# 8. 无人机遥感数据实战：数据处理流程
# ============================================================================
print("\n\n8. 无人机遥感数据实战：数据处理流程")
print("-" * 40)

print("8.1 完整的数据处理示例:")

# 步骤1：数据加载与查看
print("步骤1：数据加载与查看")
print(df.info())

# 步骤2：数据清洗
print("\n步骤2：数据清洗")
# 检查缺失值
print("缺失值检查:")
print(df.isnull().sum())

# 步骤3：数据转换
print("\n步骤3：数据转换")
# 添加派生指标
df['植被健康指数'] = df['NDVI'] * df['植被覆盖度'] / 100
print("添加植被健康指数后的数据:")
print(df[['样点ID', 'NDVI', '植被覆盖度', '植被健康指数']].head())

# 步骤4：数据分析
print("\n步骤4：数据分析")
print("各区域植被健康指数统计:")
area_health_stats = df.groupby('区域')['植被健康指数'].describe()
print(area_health_stats)

# 步骤5：数据输出
print("\n步骤5：数据输出准备")
print("处理后的数据形状:", df.shape)
print("处理后的列名:", df.columns.tolist())

# ============================================================================
# 9. 总结与练习
# ============================================================================
print("\n\n9. 总结与练习")
print("-" * 40)

print("""
本章学习了DataFrame的基本操作方法：

1. 列操作：
   - 选择列：df['列名'], df[['列1', '列2']]
   - 添加列：直接赋值或使用assign()
   - 删除列：drop(columns=['列名'])
   - 重命名列：rename(columns={'旧名':'新名'})

2. 行操作：
   - 选择行：iloc[位置], loc[条件]
   - 添加行：append()
   - 删除行：drop(index)或条件筛选

3. 数据修改：
   - 修改单个值：loc[行, 列] = 值
   - 批量修改：条件赋值
   - 使用apply函数：逐行或逐列处理

4. 数据排序：
   - sort_values()：按值排序
   - sort_index()：按索引排序

5. 数据分组：
   - groupby()：按列分组
   - 聚合函数：mean(), sum(), count()等
   - 自定义聚合函数

6. 数据透视表：
   - pivot_table()：创建透视表
   - 多维度分析

练习建议：
1. 对无人机遥感数据进行完整的清洗和转换
2. 练习使用groupby进行分组分析
3. 创建数据透视表分析区域差异
""")

# 练习示例
print("\n练习示例：无人机数据综合分析")
print("=" * 40)

# 创建练习数据
practice_data = {
    '日期': pd.date_range('2026-03-17', periods=20, freq='H'),
    '飞行高度': np.random.uniform(100, 150, 20),
    '飞行速度': np.random.uniform(10, 20, 20),
    '拍摄质量': np.random.choice(['优', '良', '中', '差'], 20),
    '数据量': np.random.randint(100, 1000, 20)
}

df_practice = pd.DataFrame(practice_data)
print("无人机飞行数据:")
print(df_practice.head())

print("\n练习任务:")
print("1. 按拍摄质量分组，计算平均飞行高度和速度")
print("2. 添加数据量等级列（<500为小，500-800为中，>800为大）")
print("3. 创建日期和拍摄质量的透视表")

print("\n" + "=" * 60)
print("任务4.2 DataFrame基本操作示例结束")
print("=" * 60)