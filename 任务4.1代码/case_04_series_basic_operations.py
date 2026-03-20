"""
案例4：Series的基本操作
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示Series的数据访问、修改、排序和统计操作
"""

import pandas as pd

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

# 数据访问
print(f"\n样区A的覆盖度: {coverage['样区A']}%")
print(f"第一个元素: {coverage.iloc[0]}%")
print(f"前3个样区:\n{coverage.iloc[:3]}")

# 数据修改
coverage_modified = coverage.copy()
coverage_modified['样区B'] = 75.8
coverage_modified[coverage_modified < 70] = 70
print(f"\n修改后的数据（修正样区B，将低于70%的设为70%）:")
print(coverage_modified)

# 排序
print(f"\n按值升序排序:\n{coverage.sort_values()}")
print(f"\n按索引排序:\n{coverage.sort_index()}")

# 统计分析
print(f"\n平均值: {coverage.mean():.2f}%")
print(f"中位数: {coverage.median():.2f}%")
print(f"标准差: {coverage.std():.2f}%")
print(f"\n描述性统计:")
print(coverage.describe())
