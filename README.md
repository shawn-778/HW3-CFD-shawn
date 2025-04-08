# HW3-CFD-shawn
使用了 sympy、random和 matplotlib.pyplot三个库
代码部分解释：
1.定义了差分公式函数：diff_1，diff_2
2.生成随机多项式函数，计算其一阶和二阶导数的符号解析表达式。利用差分公式计算导数，并比较数值求导结果与解析解之间的误差。定义函数 solve_error(f)，计算基于当前 delta_x 值下两种差分公式的误差，打印误差项用于对比分析。
