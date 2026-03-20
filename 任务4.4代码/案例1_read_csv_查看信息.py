"""
案例1：读取遥感样点CSV文件并查看基本信息
对应【知识学习】一、CSV文件的读取——pd.read_csv()
"""

import pandas as pd

# 读取无人机遥感地面样点数据
df = pd.read_csv(
    r"任务4.4代码\sample_data\uav_sample_points.csv",
    encoding='utf-8-sig',      # 处理带 BOM 的中文 CSV
    na_values=-9999            # 将 -9999 标记为无效值（NaN）
)

# 查看基本信息
print("数据形状（行×列）：", df.shape)
print("\n字段名称与类型：")
print(df.dtypes)
print("\n前 5 行数据预览：")
print(df.head())
