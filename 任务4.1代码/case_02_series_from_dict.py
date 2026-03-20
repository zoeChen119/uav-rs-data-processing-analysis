"""
案例2：从字典创建Series
教材：《无人机遥感数据处理与分析》第四章 任务4.1
演示从字典创建Series的方法，字典的键自动成为索引
"""

import pandas as pd

# 从字典创建 Series（城市人口数据示例）
city_data = {
    '北京': 2154.2,
    '上海': 2428.1,
    '广州': 1867.7,
    '深圳': 1768.2,
    '成都': 2093.8
}
city_series = pd.Series(city_data, name='城市人口(万人)')
print("从字典创建的 Series:")
print(city_series)
print(f"\n索引: {city_series.index.tolist()}")
print(f"值: {city_series.values}")