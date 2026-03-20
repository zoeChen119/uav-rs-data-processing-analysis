"""
任务4.3：Pandas索引与切片操作 - 可视化脚本
教材：《无人机遥感数据处理与分析》第四章
作者：[你的姓名]
日期：2026年3月

本文件运行任务4.3的所有代码并生成可视化图表
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# 创建图表保存目录
import os
if not os.path.exists('figures'):
    os.makedirs('figures')

print("=" * 70)
print("任务4.3：Pandas索引与切片操作 - 可视化运行")
print("=" * 70)

# ============================================================================
# 创建无人机遥感监测数据集
# ============================================================================
print("\n创建无人机遥感监测数据集...")

data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010'],
    '区域': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
    '日期': pd.date_range('2026-03-10', periods=10, freq='D'),
    '经度': [116.4074, 116.4085, 116.4096, 116.4107, 116.4118,
            116.4129, 116.4130, 116.4141, 116.4152, 116.4163],
    '纬度': [39.9042, 39.9053, 39.9064, 39.9075, 39.9086,
            39.9097, 39.9108, 39.9119, 39.9120, 39.9131],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63, 0.88, 0.71, 0.79],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3, 24.8, 31.2, 27.8, 29.5],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9, 60.5, 70.2, 53.7, 62.4, 57.9],
    '植被覆盖度': [85.6, 92.3, 78.4, 94.1, 89.2, 91.7, 83.5, 96.8, 88.6, 93.2]
}

# 设置样点ID为索引
df = pd.DataFrame(data).set_index('样点ID')
print("数据集创建完成!")
print("\n" + "=" * 70)
print("DataFrame基本信息")
print("=" * 70)
print(df)
print(f"\n数据形状: {df.shape}")
print(f"索引: {df.index.tolist()}")
print(f"列名: {df.columns.tolist()}")

# ============================================================================
# 图1：标签索引 (loc) 示例
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1.1 选择单个行
ax = axes[0, 0]
row_s003 = df.loc['S003']
ax.axis('tight')
ax.axis('off')
table_data = [[key, f'{value}'] for key, value in row_s003.items()]
table = ax.table(cellText=table_data,
               colLabels=['列名', '值'],
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
ax.set_title('图4-3-1 选择单个行：df.loc["S003"]', fontsize=12, fontweight='bold', pad=10)

# 1.2 选择多个行
ax = axes[0, 1]
rows_selected = df.loc[['S001', 'S004', 'S007']]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=rows_selected.values,
               colLabels=rows_selected.columns,
               rowLabels=rows_selected.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('图4-3-2 选择多个行：df.loc[["S001", "S004", "S007"]]', 
           fontsize=12, fontweight='bold', pad=10)

# 1.3 选择行范围
ax = axes[1, 0]
rows_range = df.loc['S002':'S005']
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=rows_range.values,
               colLabels=rows_range.columns,
               rowLabels=rows_range.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('图4-3-3 选择行范围：df.loc["S002":"S005"]', 
           fontsize=12, fontweight='bold', pad=10)

# 1.4 选择行和列
ax = axes[1, 1]
subset = df.loc['S001':'S003', ['NDVI', '温度']]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=subset.values,
               colLabels=subset.columns,
               rowLabels=subset.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.6)
ax.set_title('图4-3-4 选择特定行和列：df.loc["S001":"S003", ["NDVI", "温度"]]', 
           fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('figures/figure_4_3_1_loc_indexing.png', dpi=300, bbox_inches='tight')
print("\n✓ 图4-3-1 已保存: 标签索引 (loc) 示例")
plt.close()

# ============================================================================
# 图2：位置索引 (iloc) 示例
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 2.1 选择第2行
ax = axes[0, 0]
row_2 = df.iloc[2]
ax.axis('tight')
ax.axis('off')
table_data = [[key, f'{value}'] for key, value in row_2.items()]
table = ax.table(cellText=table_data,
               colLabels=['列名', '值'],
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
ax.set_title('图4-3-5 选择第2行：df.iloc[2]', fontsize=12, fontweight='bold', pad=10)

# 2.2 选择多行
ax = axes[0, 1]
rows_pos = df.iloc[[0, 3, 6]]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=rows_pos.values,
               colLabels=rows_pos.columns,
               rowLabels=rows_pos.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('图4-3-6 选择多行：df.iloc[[0, 3, 6]]', 
           fontsize=12, fontweight='bold', pad=10)

# 2.3 选择行范围
ax = axes[1, 0]
rows_range_pos = df.iloc[2:6]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=rows_range_pos.values,
               colLabels=rows_range_pos.columns,
               rowLabels=rows_range_pos.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('图4-3-7 选择行范围：df.iloc[2:6]', 
           fontsize=12, fontweight='bold', pad=10)

# 2.4 选择行和列
ax = axes[1, 1]
subset_pos = df.iloc[1:5, 2:6]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=subset_pos.values,
               colLabels=subset_pos.columns,
               rowLabels=subset_pos.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('图4-3-8 选择行和列：df.iloc[1:5, 2:6]', 
           fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('figures/figure_4_3_2_iloc_indexing.png', dpi=300, bbox_inches='tight')
print("✓ 图4-3-2 已保存: 位置索引 (iloc) 示例")
plt.close()

# ============================================================================
# 图3：布尔索引示例
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 3.1 单条件筛选
ax = axes[0, 0]
high_ndvi = df[df['NDVI'] > 0.7]
bars = ax.bar(high_ndvi.index.tolist(), high_ndvi['NDVI'], 
              color='#2c7fb8', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-9 单条件筛选：NDVI > 0.7', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim([0, 1.0])
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# 3.2 多条件组合（与）
ax = axes[0, 1]
condition_a = (df['区域'] == 'A') & (df['NDVI'] > 0.65)
area_a_high = df[condition_a]
bars = ax.bar(area_a_high.index.tolist(), area_a_high['NDVI'], 
              color='#e6550d', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-10 多条件（与）：区域=A且NDVI>0.65', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim([0, 1.0])
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# 3.3 多条件组合（或）
ax = axes[1, 0]
condition_b = (df['温度'] > 30) | (df['湿度'] < 60)
extreme_conditions = df[condition_b]
bars = ax.bar(range(len(extreme_conditions)), 
              [extreme_conditions.iloc[i]['NDVI'] for i in range(len(extreme_conditions))],
              color='#2ca02c', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-11 多条件（或）：温度>30或湿度<60', fontsize=12, fontweight='bold')
ax.set_xticks(range(len(extreme_conditions)))
ax.set_xticklabels(extreme_conditions.index.tolist())
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 3.4 query方法
ax = axes[1, 1]
query_result = df.query("NDVI > 0.7 and 温度 < 30")
bars = ax.bar(query_result.index.tolist(), query_result['NDVI'], 
              color='#756bb1', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-12 query方法：NDVI>0.7且温度<30', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim([0, 1.0])
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('figures/figure_4_3_3_boolean_indexing.png', dpi=300, bbox_inches='tight')
print("✓ 图4-3-3 已保存: 布尔索引示例")
plt.close()

# ============================================================================
# 图4：复杂查询示例
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 4.1 特定时间段的高植被覆盖样点
ax = axes[0, 0]
condition1 = (df['日期'] > '2026-03-12') & (df['植被覆盖度'] > 90)
query1 = df.loc[condition1]
bars = ax.bar(query1.index.tolist(), query1['植被覆盖度'], 
              color='#2c7fb8', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('植被覆盖度(%)', fontsize=11, fontweight='bold')
ax.set_title('图4-3-13 3月12日后且植被覆盖度>90%', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

# 4.2 各区域NDVI最高的样点
ax = axes[0, 1]
max_ndvi_by_area = df.loc[df.groupby('区域')['NDVI'].idxmax()]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
bars = ax.bar(max_ndvi_by_area.index.tolist(), max_ndvi_by_area['NDVI'], 
              color=[colors[i] for i in max_ndvi_by_area['区域'].map({'A':0, 'B':1, 'C':2})],
              edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-14 各区域NDVI最高的样点', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim([0, 1.0])
# 添加图例
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                              markerfacecolor=colors[i], 
                              markersize=10, label=f'区域{area}') 
                   for i, area in enumerate(['A', 'B', 'C'])]
ax.legend(handles=legend_elements, fontsize=10)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# 4.3 温度和湿度都在适宜范围的样点
ax = axes[1, 0]
condition3 = (df['温度'].between(25, 30)) & (df['湿度'].between(60, 70))
query3 = df.loc[condition3]
bars = ax.bar(query3.index.tolist(), query3['NDVI'], 
              color='#2ca02c', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-15 温度25-30度且湿度60-70%', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# 4.4 复杂条件query
ax = axes[1, 1]
query4 = df.query("""
    (NDVI > 0.7 and 温度 < 30) or
    (植被覆盖度 > 90 and 湿度 between 55 and 65)
""")
bars = ax.bar(query4.index.tolist(), query4['NDVI'], 
              color='#e6550d', edgecolor='black', linewidth=1)
ax.set_xlabel('样点ID', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-16 复杂条件query查询', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('figures/figure_4_3_4_complex_queries.png', dpi=300, bbox_inches='tight')
print("✓ 图4-3-4 已保存: 复杂查询示例")
plt.close()

# ============================================================================
# 图5：索引操作对比
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 5.1 loc vs iloc对比
ax = axes[0, 0]
x = np.arange(3)
width = 0.35
# 使用loc选择
loc_data = df.loc['S001':'S003', 'NDVI']
# 使用iloc选择
iloc_data = df.iloc[0:3, df.columns.get_loc('NDVI')]
bars1 = ax.bar(x - width/2, loc_data.values, width, label='loc["S001":"S003"]',
              color='#2c7fb8', edgecolor='black', linewidth=1)
bars2 = ax.bar(x + width/2, iloc_data.values, width, label='iloc[0:3]',
              color='#e6550d', edgecolor='black', linewidth=1)
ax.set_xlabel('样点', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-17 loc vs iloc对比', fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(['S001', 'S002', 'S003'])
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 5.2 切片行为对比
ax = axes[1, 0]
# loc切片（包含结束位置）
loc_slice = df.loc['S002':'S005', 'NDVI']
# iloc切片（不包含结束位置）
iloc_slice = df.iloc[1:4, df.columns.get_loc('NDVI')]
x1 = np.arange(len(loc_slice))
x2 = np.arange(len(iloc_slice))
ax.bar(x1 - 0.2, loc_slice.values, 0.4, label='loc["S002":"S005"] (4个)',
       color='#2c7fb8', edgecolor='black', linewidth=1)
ax.bar(x2 + 0.2, iloc_slice.values, 0.4, label='iloc[1:4] (3个)',
       color='#e6550d', edgecolor='black', linewidth=1)
ax.set_xlabel('样点位置', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('图4-3-18 切片行为：loc包含结束位，iloc不包含', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 5.3 多级索引示例
ax = axes[0, 1]
df_multi = df.reset_index().set_index(['区域', '样点ID'])
area_a = df_multi.loc['A']
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=area_a.values,
               colLabels=area_a.columns,
               rowLabels=area_a.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(7)
table.scale(1.0, 1.3)
ax.set_title('图4-3-19 多级索引：df_multi.loc["A"]', fontsize=12, fontweight='bold', pad=10)

# 5.4 索引排序
ax = axes[1, 1]
df_sorted = df.sort_index(ascending=False)
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df_sorted.values,
               colLabels=df_sorted.columns,
               rowLabels=df_sorted.index.tolist(),
               cellLoc='center',
               loc='center')
table.auto_set_font_size(False)
table.set_fontsize(7)
table.scale(1.0, 1.3)
ax.set_title('图4-3-20 索引降序排序：df.sort_index(ascending=False)', 
           fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('figures/figure_4_3_5_index_operations.png', dpi=300, bbox_inches='tight')
print("✓ 图4-3-5 已保存: 索引操作对比")
plt.close()

# ============================================================================
# 总结
# ============================================================================
print("\n" + "=" * 70)
print("运行完成!")
print("=" * 70)
print(f"\n共生成5张图表，保存在 figures/ 目录下:")
print("  1. figure_4_3_1_loc_indexing.png - 标签索引 (loc) 示例")
print("  2. figure_4_3_2_iloc_indexing.png - 位置索引 (iloc) 示例")
print("  3. figure_4_3_3_boolean_indexing.png - 布尔索引示例")
print("  4. figure_4_3_4_complex_queries.png - 复杂查询示例")
print("  5. figure_4_3_5_index_operations.png - 索引操作对比")
print("\n所有图表已保存完成，可以插入到Word文档中!")
print("=" * 70)
