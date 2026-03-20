"""
案例2：筛选有效样点并导出
对应【知识学习】二、CSV文件的写出——to_csv()
"""

import pandas as pd

# 读取原始数据（已将 -9999 识别为 NaN）
df = pd.read_csv(
    r"任务4.4代码\sample_data\uav_sample_points.csv",
    encoding='utf-8-sig',
    na_values=-9999
)

# 筛选 NDVI 有效行（去除 NaN）
df_valid = df.dropna(subset=['NDVI']).copy()
print(f"原始样点数：{len(df)}，有效样点数：{len(df_valid)}")

# 导出有效样点到新 CSV
df_valid.to_csv(
    r"任务4.4代码\sample_data\uav_sample_valid.csv",
    index=False,           # 不写入行索引
    encoding='utf-8-sig'   # 防止 Excel 打开中文乱码
)
print("有效样点数据已导出至 uav_sample_valid.csv")
