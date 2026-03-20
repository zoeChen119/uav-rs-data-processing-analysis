"""
任务实施完整代码：无人机遥感样点数据读写全流程
对应【任务实施】三、任务实施
功能：
1. 构建模拟遥感样点数据并保存为CSV
2. 读取CSV并查看数据概况
3. 查看缺失值情况
4. 筛选NDVI有效样点
5. 导出有效样点并验证
"""

import pandas as pd
import os

# ========== 第一步：构建模拟遥感样点数据并保存为 CSV ==========
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

# 保存为原始 CSV（模拟外业数据文件）
os.makedirs(r"sample_data", exist_ok=True)
df_raw.to_csv(r"任务4.4代码\sample_data\uav_sample_points.csv",
              index=False, encoding='utf-8-sig')
print("原始样点数据已保存。")
print(df_raw)

# ========== 第二步：读取 CSV 并查看数据概况 ==========
df = pd.read_csv(
    r"任务4.4代码\sample_data\uav_sample_points.csv",
    encoding='utf-8-sig',
    na_values=-9999        # 将 -9999 自动识别为 NaN
)
print("\n数据形状（行×列）：", df.shape)
print("\n字段名称与数据类型：")
print(df.dtypes)
print("\n前 5 行数据预览：")
print(df.head())

# ========== 第三步：查看缺失值情况 ==========
print("\n各字段缺失值数量：")
print(df.isnull().sum())

# ========== 第四步：筛选 NDVI 有效样点 ==========
df_valid = df.dropna(subset=['NDVI']).copy()
print(f"\n原始样点数：{len(df)}，有效样点数：{len(df_valid)}，"
      f"剔除无效样点：{len(df) - len(df_valid)} 条")

# ========== 第五步：导出有效样点并验证 ==========
df_valid.to_csv(
    r"任务4.4代码\sample_data\uav_sample_valid.csv",
    index=False,
    encoding='utf-8-sig'
)
# 验证：重新读入并核查行数
df_check = pd.read_csv(r"任务4.4代码\sample_data\uav_sample_valid.csv",
                       encoding='utf-8-sig')
print(f"\n验证导出结果：读取行数 = {len(df_check)}，"
      f"预期行数 = {len(df_valid)}，"
      f"验证{'通过' if len(df_check) == len(df_valid) else '失败'}")
print("\n有效样点数据前 5 行：")
print(df_check.head())
