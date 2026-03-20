# uav-rs-data-processing-analysis

《无人机遥感数据处理与分析》第四章配套代码资源

---

## 基本信息

- **教材名称**：《无人机遥感数据处理与分析》
- **负责章节**：第四章 数据分析核心库——Pandas 应用
- **编写人**：徽商职业学院 陈政伊
- **提交时间**：2026 年 3 月 23 日

---

## 项目概述

本仓库为教材第四章的全部配套代码，以**无人机遥感地面采样数据**为贯穿场景，系统演示 Pandas 库在遥感数据处理中的核心用法。代码按任务组织，从 Series/DataFrame 基础结构，到索引切片、文件读写，再到综合统计分析，循序渐进，适合职业院校学生课堂学习与自主练习。

---

## 目录结构

```
uav-rs-data-processing-analysis/
├── README.md
├── 任务4.1代码/          # Pandas Series 数据结构
│   ├── case_01_series_from_list.py
│   ├── case_02_series_from_dict.py
│   ├── case_03_series_with_nan.py
│   ├── case_04_series_basic_operations.py
│   ├── case_05_series_operations_statistics.py
│   └── run_all_cases.py
├── 任务4.2代码/          # Pandas DataFrame 数据结构
│   ├── case_01-dataframe_from_dict.py
│   ├── case_02-dataframe_from_list.py
│   ├── case_03-dataframe_from_numpy.py
│   ├── case_04-dataframe_with_nan.py
│   ├── case_05-datafram-col.py
│   ├── case_06-dataframe-raw.py
│   ├── case_07-dataframe-others.py
│   └── run_all_visualizations.py
├── 任务4.3代码/          # Pandas 索引与切片操作
│   ├── case_01_loc_indexing.py
│   ├── case_02_iloc_indexing.py
│   ├── case_03_boolean_filtering.py
│   ├── case_04_multiindex.py
│   └── run_all_cases.py
├── 任务4.4代码/          # 无人机遥感数据读写
│   ├── case_01_read_csv_lookinfo.py
│   ├── case_02_to_csv_exp.py
│   ├── case_03_excel_rw.py
│   ├── run_all_case.py
│   ├── 巩固提高_参考答案.py
│   └── sample_data/
│       ├── uav_sample_points.csv    # 原始数据（含 -9999 无效值）
│       ├── uav_sample_points.xlsx
│       ├── uav_sample_valid.csv     # 清洗后有效数据
│       └── uav_sample_valid.xlsx
└── 任务4.5代码/          # 综合案例：遥感样点统计描述分析
    ├── case_01_basic_stats.py
    ├── case_02_group_anal.py
    ├── case_03_quality-outlier-detection.py
    ├── run_all_case.py
    └── 巩固提高_参考答案.py
```

---

## 各任务说明

### 任务 4.1　Pandas 数据结构之 Series

**学习目标**：掌握 Series 的多种创建方式，熟练进行数据访问、排序、统计与缺失值处理。

| 文件 | 主要内容 |
|------|---------|
| `case_01_series_from_list.py` | 从列表创建 NDVI 植被指数 Series，自定义样点索引，查看 `.shape`、`.mean()`、`.idxmax()` |
| `case_02_series_from_dict.py` | 从字典创建城市人口 Series，字典键自动成为索引，查看 `.index`、`.values` |
| `case_03_series_with_nan.py` | 含缺失值的传感器温度数据，使用 `.isna()`、`.count()`、`.dropna()` 检测与清洗 |
| `case_04_series_basic_operations.py` | 植被覆盖度数据的访问、条件修改、按值/按索引排序及描述统计 |
| `case_05_series_operations_statistics.py` | 时序 NDVI 数据，演示算术运算、线性插值填充缺失值（`.interpolate()`）、3 天移动平均（`.rolling(3).mean()`） |
| `run_all_cases.py` | 批量调度脚本，依次运行以上所有案例 |

---

### 任务 4.2　Pandas 数据结构之 DataFrame

**学习目标**：掌握 DataFrame 的多种创建方式及行列操作，能够进行排序、分组统计和数据透视。

| 文件 | 主要内容 |
|------|---------|
| `case_01-dataframe_from_dict.py` | 从字典创建遥感样点 DataFrame（样点ID、经纬度、NDVI、温度、湿度） |
| `case_02-dataframe_from_list.py` | 从嵌套列表创建 DataFrame，演示自定义行索引 |
| `case_03-dataframe_from_numpy.py` | 从 NumPy 二维数组创建 DataFrame，指定列名和行索引 |
| `case_04-dataframe_with_nan.py` | 含缺失值的 DataFrame，用 `.isna().sum()` 统计各列及全局缺失数 |
| `case_05-datafram-col.py` | 列操作全示范：单列选取、多列选取、新增派生列（NDVI 百分比）、删列、重命名列 |
| `case_06-dataframe-raw.py` | 行操作全示范：按位置/条件选行、修改单值、批量运算（温度单位转换）、条件修改 |
| `case_07-dataframe-others.py` | 多列排序、`groupby` 分组统计、`pivot_table` 数据透视 |
| `run_all_visualizations.py` | 一键运行并生成 6 张图表（DPI=300）保存至 `figures/` 目录 |

**生成图表（`figures/` 目录）**：

| 文件名 | 内容 |
|--------|------|
| `figure_4_2_1_dataframe_structure.png` | DataFrame 表格结构 |
| `figure_4_2_2_ndvi_temp.png` | 各样点 NDVI 与温度对比柱状图 |
| `figure_4_2_3_area_statistics.png` | 区域分组统计四联图（柱状图、散点图、饼图、气泡图） |
| `figure_4_2_4_dataframe_methods.png` | `head()`、`tail()`、`describe()`、`dtypes` 演示 |
| `figure_4_2_5_pivot_table.png` | 透视表热力图 + 分组柱状图 |
| `figure_4_2_6_column_operations.png` | 列操作演示四联图 |

---

### 任务 4.3　Pandas 索引与切片操作

**学习目标**：区分并熟练使用标签索引、位置索引与布尔索引，掌握多级索引的创建与查询。

| 文件 | 主要内容 |
|------|---------|
| `case_01_loc_indexing.py` | `.loc[]` 标签索引：单标签、范围标签、列表标签选取 |
| `case_02_iloc_indexing.py` | `.iloc[]` 位置索引：单行、多行、切片、行列同时切片 |
| `case_03_boolean_filtering.py` | 布尔索引：单条件（NDVI > 0.7）、多条件与（&）和或（\|）、`.isin()`、`.query()` |
| `case_04_multiindex.py` | 多级索引：`set_index(['区域','样点ID'])` 创建，顶层查询、完整路径查询、`.xs()` 横截面查询 |
| `run_all_cases.py` | 批量调度脚本，依次运行以上所有案例 |

---

### 任务 4.4　无人机遥感数据的读写

**学习目标**：掌握用 Pandas 读写 CSV 和 Excel 格式遥感数据的完整流程，包括无效值识别、数据清洗与导出验证。

| 文件 | 主要内容 |
|------|---------|
| `case_01_read_csv_lookinfo.py` | `pd.read_csv()` 读取 CSV，`na_values=-9999` 自动标记无效值，查看数据形状、字段类型、前 5 行 |
| `case_02_to_csv_exp.py` | 用 `dropna()` 筛除 NDVI 无效行，`to_csv()` 导出（`index=False`，`encoding='utf-8-sig'`） |
| `case_03_excel_rw.py` | `read_excel()` 指定工作表与 openpyxl 引擎读取；`to_excel()` 指定工作表名称导出 |
| `run_all_case.py` | 完整五步骤任务实施：构建数据 → 读取概况 → 缺失值查看 → 筛选有效样点 → 导出并验证 |
| `巩固提高_参考答案.py` | 拓展练习：额外筛选"农田"类有效样点，只保留经纬度和 NDVI 三列，导出并双重验证（行数+列数） |

**样本数据（`sample_data/`）**：

| 文件 | 说明 |
|------|------|
| `uav_sample_points.csv` | 原始数据，10 条记录，其中 3 条 NDVI=-9999（均为裸土地类） |
| `uav_sample_valid.csv` | 清洗后数据，7 条有效记录（去除全部无效值） |
| `uav_sample_points.xlsx` / `uav_sample_valid.xlsx` | 以上数据的 Excel 版本 |

数据字段：`longitude`（经度）、`latitude`（纬度）、`NDVI`（归一化植被指数）、`LST`（地表温度）、`land_type`（地物类型：农田 / 林地 / 裸土）

---

### 任务 4.5　案例：无人机遥感样点数据的统计描述

**学习目标**：综合运用 Pandas 完成遥感样点数据的全流程统计分析，包括基本统计量、分组统计、数据质量评估与异常值检测处理。

| 文件 | 主要内容 |
|------|---------|
| `case_01_basic_stats.py` | NDVI 的均值/中位数/标准差/极差，温度的四分位数，批量 `.describe()` |
| `case_02_group_anal.py` | 按区域（A/B/C）、按地物类型（农田/林地/裸土）分别聚合，多级分组，`size()` 计数 |
| `case_03_quality-outlier-detection.py` | 缺失值检测 → 重复值检测 → 数据类型检查 → IQR 法异常值检测（S008 的 LST=45.0 为植入异常）→ 中位数替换处理 |
| `run_all_case.py` | 完整六步骤综合分析：创建数据集 → 基本统计量 → 分组统计 → 数据质量评估 → 异常值检测与处理 → 统计结果汇总（含自动文字解读） |
| `巩固提高_参考答案.py` | 拓展练习：湿度变异系数计算、NDVI 最高/最低样点识别、多级分组统计、NDVI 四分位数与异常值判断 |

**综合数据集（10 个样点）**：

| 字段 | 说明 | 典型范围 |
|------|------|---------|
| 样点ID | 采样点编号 | S001 ~ S010 |
| 区域 | 采样区域 | A / B / C |
| 地物类型 | 土地覆盖 | 农田 / 林地 / 裸土 |
| NDVI | 归一化植被指数 | 0.58 ~ 0.88 |
| LST | 地表温度 | 25.8 ~ 32.5 ℃ |
| 温度 | 气温 | 24.9 ~ 29.3 ℃ |
| 湿度 | 相对湿度 | 53.7 ~ 72.3 % |

---

## 环境依赖

```
pandas
numpy
matplotlib
openpyxl
```

安装方式：

```bash
pip install pandas numpy matplotlib openpyxl
```

中文字体配置（matplotlib）：代码中已统一设置 `SimHei` / `Microsoft YaHei`，Windows 系统无需额外操作。

---

## 快速运行

每个任务文件夹下均提供 `run_all_cases.py` 或 `run_all_case.py`，可一键运行该任务的全部案例：

```bash
# 进入对应任务目录后运行
python run_all_cases.py   # 任务4.1、4.3
python run_all_visualizations.py  # 任务4.2（同时生成图表）
python run_all_case.py    # 任务4.4、4.5
```

> **注意**：任务 4.4 的案例文件使用了相对路径引用 `sample_data/`，建议在**项目根目录**下运行，或根据实际路径调整脚本中的文件路径。

---

## 参考资料

1. [Pandas 官方文档](https://pandas.pydata.org/docs/)
2. 《利用 Python 进行数据分析》（第 3 版），Wes McKinney 著
3. 无人机遥感数据处理相关论文与行业标准
