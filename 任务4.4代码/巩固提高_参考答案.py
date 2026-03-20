"""
巩固提高：代码实操题参考答案
在上述任务实施代码的基础上，完成以下操作：
（1）在原始样点数据中，额外筛选出 land_type 为"农田"的有效样点（NDVI 不为 NaN 且 land_type 为农田），统计该类样点的数量；
（2）将筛选结果只保留 longitude、latitude、NDVI 三列，导出为 uav_farmland_valid.csv；
（3）重新读取导出文件，打印行数与列数，验证结果是否符合预期。
"""

import pandas as pd
import os

# ========== 准备原始数据 ==========
data = {
    'longitude': [116.32, 116.33, 116.34, 116.35, 116.36,
                  116.37, 116.38, 116.39, 116.40, 116.41],
    'latitude':  [39.91, 39.92, 39.93, 39.94, 39.95,
                  39.96, 39.97, 39.98, 39.99, 40.00],
    'NDVI':      [0.82, 0.75, -9999, 0.68, 0.91,
                  -9999, 0.55, 0.78, 0.83, -9999],
    'LST':       [28.5, 29.1, 30.2, 27.8, 26.5,
                  31.0, 29.9, 28.3, 27.1, 32.0],
    'land_type': ['农田', '农田', '裸土', '农田', '林地',
                  '裸土', '农田', '林地', '农田', '裸土']
}
df_raw = pd.DataFrame(data)

# ========== （1）筛选 land_type 为"农田"的有效样点 ==========
df = df_raw.copy()
# 将 -9999 标记为 NaN
df.loc[df['NDVI'] == -9999, 'NDVI'] = None

# 筛选：NDVI 有效 且 land_type 为农田
df_farmland_valid = df.dropna(subset=['NDVI'])
df_farmland_valid = df_farmland_valid[df_farmland_valid['land_type'] == '农田']

print(f"农田有效样点数量：{len(df_farmland_valid)}")
print("\n农田有效样点数据：")
print(df_farmland_valid)

# ========== （2）只保留指定三列并导出 ==========
df_export = df_farmland_valid[['longitude', 'latitude', 'NDVI']]
df_export.to_csv(
    r"任务4.4代码\sample_data\uav_farmland_valid.csv",
    index=False,
    encoding='utf-8-sig'
)
print("\n农田有效样点已导出至 uav_farmland_valid.csv")

# ========== （3）重新读取并验证 ==========
df_check = pd.read_csv(r"任务4.4代码\sample_data\uav_farmland_valid.csv",
                      encoding='utf-8-sig')
print(f"\n验证导出结果：")
print(f"读取行数 = {len(df_check)}")
print(f"读取列数 = {len(df_check.columns)}")
print(f"列名 = {list(df_check.columns)}")

if len(df_check) == len(df_farmland_valid) and len(df_check.columns) == 3:
    print("验证通过！导出结果符合预期。")
else:
    print("验证失败，请检查代码逻辑。")
