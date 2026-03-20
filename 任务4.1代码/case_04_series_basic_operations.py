"""
案例4：Series的基本操作
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示Series的数据访问、修改、排序和统计操作
"""

import pandas as pd

print("=" * 60)
print("案例4：Series的基本操作")
print("=" * 60)

# 创建无人机植被覆盖度数据
coverage_data = {
    '样区A': 85.6,
    '样区B': 72.3,
    '样区C': 91.2,
    '样区D': 68.7,
    '样区E': 79.4
}
coverage = pd.Series(coverage_data, name='植被覆盖度(%)')

print("原始植被覆盖度数据:")
print(coverage)
print()

# ========== 数据访问 ==========
print("1. 数据访问:")
print("-" * 40)
print(f"样区A的覆盖度: {coverage['样区A']}%")
print(f"第一个元素: {coverage.iloc[0]}%")
print(f"前3个样区:")
print(coverage.iloc[:3])
print()

# ========== 条件筛选 ==========
print("2. 条件筛选:")
print("-" * 40)
high_coverage = coverage[coverage > 80]
print(f"覆盖度大于80%的样区:")
print(high_coverage)
print()

low_coverage = coverage[coverage < 70]
print(f"覆盖度小于70%的样区:")
print(low_coverage)
print()

# ========== 数据修改 ==========
print("3. 数据修改:")
print("-" * 40)
coverage_modified = coverage.copy()

# 修改单个值
coverage_modified['样区B'] = 75.8
print(f"修改样区B为75.8%:")
print(coverage_modified)
print()

# 条件修改：将低于70%的设为70%
coverage_modified[coverage_modified < 70] = 70
print(f"将低于70%的设为70%:")
print(coverage_modified)
print()

# ========== 排序 ==========
print("4. 排序:")
print("-" * 40)
print("按值升序排序:")
print(coverage.sort_values())
print()

print("按值降序排序:")
print(coverage.sort_values(ascending=False))
print()

print("按索引排序:")
print(coverage.sort_index())
print()

# ========== 统计分析 ==========
print("5. 统计分析:")
print("-" * 40)
print(f"平均值: {coverage.mean():.2f}%")
print(f"中位数: {coverage.median():.2f}%")
print(f"标准差: {coverage.std():.2f}%")
print(f"最小值: {coverage.min():.2f}%")
print(f"最大值: {coverage.max():.2f}%")
print()

print("描述性统计:")
print(coverage.describe())
