"""
案例3：Excel文件读写示例
对应【知识学习】三、Excel文件的读写——read_excel()与to_excel()
"""

import pandas as pd

# 读取 Excel 文件（第 1 张工作表）
df_excel = pd.read_excel(
    r"任务4.4代码\sample_data\uav_sample_points.xlsx",
    sheet_name=0,
    na_values=-9999,
    engine='openpyxl'  # 使用openpyxl引擎处理可能加密的文件
)
print("Excel 数据读取成功，形状：", df_excel.shape)

# 将处理结果写出为 Excel 文件
df_excel.dropna(subset=['NDVI']).to_excel(
    r"任务4.4代码\sample_data\uav_sample_valid.xlsx",
    sheet_name='有效样点',
    index=False
)
print("有效样点已导出至 uav_sample_valid.xlsx")
