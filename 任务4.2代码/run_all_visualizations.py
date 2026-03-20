"""
任务4.2：Pandas数据结构之DataFrame - 可视化脚本
教材：《无人机遥感数据处理与分析》第四章
作者：陈政伊
日期：2026年3月

本文件运行任务4.2的所有代码并生成可视化图表
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
print("任务4.2：Pandas数据结构之DataFrame - 可视化运行")
print("=" * 70)

# ============================================================================
# 创建完整的无人机遥感监测数据集
# ============================================================================
print("\n创建无人机遥感监测数据集...")

complete_remote_data = {
    '样点ID': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'],
    '区域': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
    '经度': [116.4074, 116.4085, 116.4096, 116.4107, 116.4118, 116.4129, 116.4130, 116.4141],
    '纬度': [39.9042, 39.9053, 39.9064, 39.9075, 39.9086, 39.9097, 39.9108, 39.9119],
    'NDVI': [0.65, 0.72, 0.58, 0.81, 0.69, 0.75, 0.63, 0.88],
    '温度': [25.3, 28.7, 23.9, 30.1, 26.5, 29.3, 24.8, 31.2],
    '湿度': [65.2, 58.7, 72.3, 55.8, 68.9, 60.5, 70.2, 53.7],
    '植被覆盖度': [85.6, 92.3, 78.4, 94.1, 89.2, 91.7, 83.5, 96.8]
}

df = pd.DataFrame(complete_remote_data)
print("数据集创建完成!")
print("\n" + "=" * 70)
print("DataFrame基本信息")
print("=" * 70)
print(df)
print(f"\n数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")

# ============================================================================
# 图1：DataFrame结构展示
# ============================================================================
fig, ax = plt.subplots(figsize=(12, 5))
ax.axis('tight')
ax.axis('off')

# 创建DataFrame显示
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)

# 设置标题
ax.set_title('无人机遥感监测DataFrame数据', fontsize=14, fontweight='bold', pad=20)

plt.savefig('figures/figure_4_2_1_dataframe_structure.png', dpi=300, bbox_inches='tight')
print("\n✓ 图4-1 已保存: DataFrame结构展示")
plt.close()

# ============================================================================
# 图2：NDVI和温度的柱状图对比
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# NDVI柱状图
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']
bars1 = ax1.bar(df['样点ID'], df['NDVI'], color=colors, edgecolor='black', linewidth=0.5)
ax1.set_xlabel('样点编号', fontsize=12, fontweight='bold')
ax1.set_ylabel('NDVI值', fontsize=12, fontweight='bold')
ax1.set_title('各采样点NDVI值对比', fontsize=13, fontweight='bold')
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.set_ylim([0, 1.0])

# 添加数值标签
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom', fontsize=9)

# 温度柱状图
bars2 = ax2.bar(df['样点ID'], df['温度'], color='#e6550d', edgecolor='black', linewidth=0.5)
ax2.set_xlabel('样点编号', fontsize=12, fontweight='bold')
ax2.set_ylabel('温度(°C)', fontsize=12, fontweight='bold')
ax2.set_title('各采样点温度对比', fontsize=13, fontweight='bold')
ax2.grid(axis='y', alpha=0.3, linestyle='--')

# 添加数值标签
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('figures/figure_4_2_2_ndvi_temp.png', dpi=300, bbox_inches='tight')
print("✓ 图4-2 已保存: NDVI和温度对比柱状图")
plt.close()

# ============================================================================
# 图3：区域分组统计
# ============================================================================
# 按区域分组统计
area_stats = df.groupby('区域').agg({
    'NDVI': ['mean', 'std', 'max'],
    '温度': ['mean', 'std', 'max'],
    '湿度': 'mean'
})

print("\n" + "=" * 70)
print("区域分组统计")
print("=" * 70)
print(area_stats)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

# 各区域NDVI平均值
area_means = df.groupby('区域')['NDVI'].mean()
colors_region = ['#1f77b4', '#ff7f0e', '#2ca02c']
axes[0].bar(area_means.index, area_means.values, color=colors_region, 
           edgecolor='black', linewidth=1, alpha=0.8)
axes[0].set_xlabel('区域', fontsize=12, fontweight='bold')
axes[0].set_ylabel('NDVI平均值', fontsize=12, fontweight='bold')
axes[0].set_title('各区域NDVI平均值对比', fontsize=13, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3, linestyle='--')

# 各区域温度分布
for idx, area in enumerate(['A', 'B', 'C']):
    area_data = df[df['区域'] == area]['温度']
    axes[1].scatter([idx] * len(area_data), area_data, 
                    s=200, alpha=0.6, label=f'区域{area}')
axes[1].set_xlabel('区域', fontsize=12, fontweight='bold')
axes[1].set_ylabel('温度(°C)', fontsize=12, fontweight='bold')
axes[1].set_title('各区域温度分布散点图', fontsize=13, fontweight='bold')
axes[1].set_xticks([0, 1, 2])
axes[1].set_xticklabels(['区域A', '区域B', '区域C'])
axes[1].legend(fontsize=10)
axes[1].grid(axis='y', alpha=0.3, linestyle='--')

# 各区域样点数量
area_counts = df.groupby('区域').size()
axes[2].pie(area_counts.values, labels=[f'区域{i}' for i in area_counts.index],
            autopct='%1.0f%%', colors=colors_region,
            startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
axes[2].set_title('各区域样点数量占比', fontsize=13, fontweight='bold')

# NDVI与温度关系
scatter = axes[3].scatter(df['NDVI'], df['温度'], 
                          s=df['植被覆盖度'], 
                          c=[colors_region[i] for i in df['区域'].map({'A':0, 'B':1, 'C':2})],
                          alpha=0.6, edgecolors='black', linewidth=1)
axes[3].set_xlabel('NDVI', fontsize=12, fontweight='bold')
axes[3].set_ylabel('温度(°C)', fontsize=12, fontweight='bold')
axes[3].set_title('NDVI与温度关系（气泡大小=植被覆盖度）', fontsize=13, fontweight='bold')
axes[3].grid(alpha=0.3, linestyle='--')

# 添加图例
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors_region[i],
                              markersize=10, label=f'区域{area}') 
                   for i, area in enumerate(['A', 'B', 'C'])]
axes[3].legend(handles=legend_elements, fontsize=10)

plt.tight_layout()
plt.savefig('figures/figure_4_2_3_area_statistics.png', dpi=300, bbox_inches='tight')
print("✓ 图4-3 已保存: 区域分组统计图表")
plt.close()

# ============================================================================
# 图4：DataFrame属性和方法演示
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 4.1 head()和tail()对比
head_df = df.head(3)
tail_df = df.tail(3)

# 显示前3行
ax = axes[0, 0]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=head_df.values,
                 colLabels=head_df.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 1.4)
ax.set_title('df.head(3) - 前3行数据', fontsize=12, fontweight='bold', pad=10)

# 显示后3行
ax = axes[0, 1]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=tail_df.values,
                 colLabels=tail_df.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.set_scale(1.1, 1.4)
ax.set_title('df.tail(3) - 后3行数据', fontsize=12, fontweight='bold', pad=10)

# 4.2 描述性统计
ax = axes[1, 0]
ax.axis('tight')
ax.axis('off')
desc_stats = df.describe()
table = ax.table(cellText=desc_stats.round(2).values,
                 colLabels=desc_stats.columns,
                 rowLabels=desc_stats.index,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(7)
table.scale(1.1, 1.3)
ax.set_title('df.describe() - 描述性统计', fontsize=12, fontweight='bold', pad=10)

# 4.3 数据类型
ax = axes[1, 1]
ax.axis('tight')
ax.axis('off')
dtypes_df = pd.DataFrame({'列名': df.columns, '数据类型': df.dtypes.astype(str)})
table = ax.table(cellText=dtypes_df.values,
                 colLabels=dtypes_df.columns,
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)
ax.set_title('df.dtypes - 数据类型', fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('figures/figure_4_2_4_dataframe_methods.png', dpi=300, bbox_inches='tight')
print("✓ 图4-4 已保存: DataFrame属性和方法演示")
plt.close()

# ============================================================================
# 图5：数据透视表
# ============================================================================
# 添加温度等级
def classify_temperature(temp):
    if temp < 25:
        return '低温'
    elif temp < 30:
        return '适宜'
    else:
        return '高温'

df['温度等级'] = df['温度'].apply(classify_temperature)

# 创建透视表
pivot_ndvi = pd.pivot_table(df,
                            values='NDVI',
                            index='区域',
                            columns='温度等级',
                            aggfunc='mean',
                            fill_value=0)

print("\n" + "=" * 70)
print("数据透视表")
print("=" * 70)
print("各区域不同温度等级的平均NDVI:")
print(pivot_ndvi)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 透视表热力图
ax = axes[0]
im = ax.imshow(pivot_ndvi.values, cmap='YlOrRd', aspect='auto')

# 设置刻度
ax.set_xticks(np.arange(len(pivot_ndvi.columns)))
ax.set_yticks(np.arange(len(pivot_ndvi.index)))
ax.set_xticklabels(pivot_ndvi.columns)
ax.set_yticklabels(pivot_ndvi.index)

# 添加数值标签
for i in range(len(pivot_ndvi.index)):
    for j in range(len(pivot_ndvi.columns)):
        text = ax.text(j, i, f'{pivot_ndvi.values[i, j]:.2f}',
                      ha="center", va="center", color="black", fontweight='bold')

ax.set_xlabel('温度等级', fontsize=12, fontweight='bold')
ax.set_ylabel('区域', fontsize=12, fontweight='bold')
ax.set_title('各区域不同温度等级的平均NDVI', fontsize=13, fontweight='bold')

# 添加颜色条
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('NDVI值', fontsize=11, fontweight='bold')

# 分组柱状图
x = np.arange(len(pivot_ndvi.index))
width = 0.25
colors_temp = ['#2c7fb8', '#7fcdbb', '#fee08b']

for idx, temp_level in enumerate(pivot_ndvi.columns):
    ax = axes[1]
    bars = ax.bar(x + idx * width, pivot_ndvi[temp_level].values, 
                  width, label=temp_level, color=colors_temp[idx],
                  edgecolor='black', linewidth=1)
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # 只对非零值添加标签
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}',
                   ha='center', va='bottom', fontsize=9)

axes[1].set_xlabel('区域', fontsize=12, fontweight='bold')
axes[1].set_ylabel('NDVI平均值', fontsize=12, fontweight='bold')
axes[1].set_title('各区域不同温度等级的NDVI对比', fontsize=13, fontweight='bold')
axes[1].set_xticks(x + width)
axes[1].set_xticklabels([f'区域{i}' for i in pivot_ndvi.index])
axes[1].legend(fontsize=11)
axes[1].grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('figures/figure_4_2_5_pivot_table.png', dpi=300, bbox_inches='tight')
print("✓ 图4-5 已保存: 数据透视表可视化")
plt.close()

# ============================================================================
# 图6：列操作演示
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 6.1 单列选择
ax = axes[0, 0]
ndvi_col = df['NDVI']
bars = ax.bar(df['样点ID'], ndvi_col, color='#2c7fb8', 
              edgecolor='black', linewidth=1)
ax.set_xlabel('样点编号', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('选择单列：df["NDVI"]', fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=8)

# 6.2 多列选择
ax = axes[0, 1]
selected_df = df[['样点ID', 'NDVI', '温度']]
x_pos = np.arange(len(selected_df))
width = 0.35
bars1 = ax.bar(x_pos - width/2, selected_df['NDVI'], width, 
               label='NDVI', color='#2c7fb8', edgecolor='black', linewidth=1)
bars2 = ax.bar(x_pos + width/2, selected_df['温度']/40, width,
               label='温度/40', color='#e6550d', edgecolor='black', linewidth=1)
ax.set_xlabel('样点编号', fontsize=11, fontweight='bold')
ax.set_ylabel('值', fontsize=11, fontweight='bold')
ax.set_title('选择多列：df[["NDVI", "温度"]]', fontsize=12, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(selected_df['样点ID'])
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 6.3 添加派生列
ax = axes[1, 0]
df_copy = df.copy()
df_copy['NDVI百分比'] = df_copy['NDVI'] * 100
bars = ax.bar(df_copy['样点ID'], df_copy['NDVI百分比'], 
              color='#2ca02c', edgecolor='black', linewidth=1)
ax.set_xlabel('样点编号', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI百分比(%)', fontsize=11, fontweight='bold')
ax.set_title('添加派生列：df["NDVI百分比"] = df["NDVI"] * 100', 
             fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.1f}%', ha='center', va='bottom', fontsize=8)

# 6.4 数据排序
ax = axes[1, 1]
df_sorted = df.sort_values('NDVI', ascending=False)
bars = ax.bar(df_sorted['样点ID'], df_sorted['NDVI'], 
              color='#1f77b4', edgecolor='black', linewidth=1)
ax.set_xlabel('样点编号（按NDVI降序排序）', fontsize=11, fontweight='bold')
ax.set_ylabel('NDVI', fontsize=11, fontweight='bold')
ax.set_title('数据排序：df.sort_values("NDVI", ascending=False)', 
             fontsize=12, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{height:.2f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('figures/figure_4_2_6_column_operations.png', dpi=300, bbox_inches='tight')
print("✓ 图4-6 已保存: 列操作演示")
plt.close()

# ============================================================================
# 总结
# ============================================================================
print("\n" + "=" * 70)
print("运行完成!")
print("=" * 70)
print(f"\n共生成6张图表，保存在 figures/ 目录下:")
print("  1. figure_4_2_1_dataframe_structure.png - DataFrame结构展示")
print("  2. figure_4_2_2_ndvi_temp.png - NDVI和温度对比柱状图")
print("  3. figure_4_2_3_area_statistics.png - 区域分组统计图表")
print("  4. figure_4_2_4_dataframe_methods.png - DataFrame属性和方法演示")
print("  5. figure_4_2_5_pivot_table.png - 数据透视表可视化")
print("  6. figure_4_2_6_column_operations.png - 列操作演示")
print("\n所有图表已保存完成，可以插入到Word文档中!")
print("=" * 70)
