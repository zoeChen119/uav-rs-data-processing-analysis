# uav-rs-data-processing-analysis
安徽商贸职业学院-《无人机遥感数据处理与分析》-Chapter4附件代码

# 第四章：数据分析核心库——Pandas应用 编写大纲

## 一、基本信息

- **教材名称**：《无人机遥感数据处理与分析》
- **负责章节**：第四章 数据分析核心库——Pandas应用
- **编写人**：徽商职业学院 陈政伊
- **提交时间**：2026年3月23日

## 二、章节结构

### 项目4 数据分析核心库——Pandas应用

**学习目标**：

1. 掌握Pandas核心数据结构Series和DataFrame
2. 熟练使用Pandas进行数据索引、切片和筛选
3. 掌握无人机遥感数据的读写方法
4. 能够使用Pandas进行遥感数据的统计描述分析

### 任务4.1 Pandas数据结构之Series

**主要内容**：

1. Series的创建方法
   - 从列表创建
   - 从字典创建
   - 从NumPy数组创建
2. Series的基本操作
   - 查看数据信息
   - 数据访问与修改
   - 数据排序
3. Series的运算与统计
   - 算术运算
   - 统计函数（mean, std, min, max等）
   - 缺失值处理

**代码资源**：

- `chapt_4_1_series_creation.py`：Series创建示例
- `chapt_4_1_series_operations.py`：Series操作示例
- `chapt_4_1_series_statistics.py`：Series统计示例

### 任务4.2 Pandas数据结构之DataFrame

**主要内容**：

1. DataFrame的创建方法
   - 从字典创建
   - 从列表创建
   - 从CSV/Excel文件读取
2. DataFrame的基本操作
   - 查看数据信息（info, describe）
   - 列操作（添加、删除、重命名）
   - 行操作（添加、删除）
3. DataFrame的数据类型与转换
   - 数据类型查看与修改
   - 数据类型转换方法

**代码资源**：

- `chapt_4_2_dataframe_creation.py`：DataFrame创建示例
- `chapt_4_2_dataframe_operations.py`：DataFrame操作示例
- `chapt_4_2_dataframe_types.py`：数据类型转换示例

### 任务4.3 Pandas索引与切片操作

**主要内容**：

1. 标签索引与位置索引
   - loc索引（基于标签）
   - iloc索引（基于位置）
2. 布尔索引与条件筛选
   - 单条件筛选
   - 多条件组合筛选
3. 多级索引与数据透视
   - 创建多级索引
   - 数据透视表

**代码资源**：

- `chapt_4_3_indexing.py`：索引操作示例
- `chapt_4_3_filtering.py`：条件筛选示例
- `chapt_4_3_pivot.py`：数据透视示例

### 任务4.4 无人机遥感数据的读写

**主要内容**：

1. 常见遥感数据格式读取
   - CSV格式遥感数据读取
   - Excel格式遥感数据读取
   - 文本格式遥感数据读取
2. 遥感数据格式转换与保存
   - 数据格式转换
   - 数据保存为不同格式
3. 大数据集的分块读取
   - 分块读取大文件
   - 内存优化技巧

**代码资源**：

- `chapt_4_4_read_csv.py`：CSV数据读取示例
- `chapt_4_4_read_excel.py`：Excel数据读取示例
- `chapt_4_4_chunk_reading.py`：分块读取示例

### 任务4.5 案例：无人机遥感样点数据的统计描述

**主要内容**：

1. 案例背景与需求分析
   - 无人机遥感样点数据特点
   - 统计描述需求分析
2. 数据加载与预处理
   - 样点数据加载
   - 数据清洗与预处理
3. 描述性统计分析
   - 基本统计量计算
   - 数据分布分析
   - 相关性分析
4. 可视化统计结果
   - 统计图表绘制
   - 结果解读与分析

**代码资源**：

- `chapt_4_5_case_data_loading.py`：数据加载与预处理
- `chapt_4_5_case_statistics.py`：描述性统计分析
- `chapt_4_5_case_visualization.py`：结果可视化

## 五、参考资料

### 必读资料

1. Pandas官方文档：https://pandas.pydata.org/docs/
2. 《利用Python进行数据分析》（第2版）
3. 无人机遥感数据处理相关论文

### 推荐案例数据集

1. 无人机多光谱遥感数据
2. 无人机LiDAR点云数据
3. 无人机可见光影像数据

