"""
任务4.3 - 运行所有案例代码
教材：《无人机遥感数据处理与分析》第四章
本脚本按顺序运行所有案例代码，演示Pandas索引与切片操作
"""

import subprocess
import sys
import os

print("=" * 70)
print("任务4.3 - Pandas索引与切片操作")
print("准备运行所有案例代码...")
print("=" * 70)

# 定义所有案例文件
cases = [
    ("案例1：loc标签索引", "case_01_loc_indexing.py"),
    ("案例2：iloc位置索引", "case_02_iloc_indexing.py"),
    ("案例3：布尔索引条件筛选", "case_03_boolean_filtering.py"),
    ("案例4：多级索引操作", "case_04_multiindex.py"),
    ("完整实施流程", "chapt_4_3_indexing.py")
]

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 逐个运行案例
for i, (case_name, file_name) in enumerate(cases, 1):
    print(f"\n{'=' * 70}")
    print(f"运行 {i}/{len(cases)}: {case_name}")
    print(f"文件: {file_name}")
    print("=" * 70)

    file_path = os.path.join(current_dir, file_name)

    if not os.path.exists(file_path):
        print(f"错误: 文件不存在 - {file_path}")
        continue

    try:
        # 运行Python脚本
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=False,
            text=True,
            cwd=current_dir
        )

        if result.returncode == 0:
            print(f"\n✓ {case_name} 运行成功")
        else:
            print(f"\n✗ {case_name} 运行失败，返回码: {result.returncode}")
    except Exception as e:
        print(f"\n✗ 运行出错: {str(e)}")

print(f"\n{'=' * 70}")
print("所有案例运行完成！")
print("=" * 70)
