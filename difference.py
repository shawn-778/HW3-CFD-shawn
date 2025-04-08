import sympy as sp
import random
import matplotlib.pyplot as plt

# 两种差分公式
def diff_1(u, x_0, delta_x):
    offsets = list(range(-1, 2, 1))
    fun_value = [u.subs(x, x_0 + offset * delta_x) for offset in offsets]
    u_x = (fun_value[2] - fun_value[0]) / (2 * delta_x)
    u_xx = (fun_value[2] + fun_value[0] - 2 * fun_value[1]) / delta_x ** 2
    return u_x, u_xx


def diff_2(u, x_0, delta_x):
    offsets = list(range(0, 4, 1))
    fun_value = [u.subs(x, x_0 + offset * delta_x) for offset in offsets]
    u_x = (-11 * fun_value[0] + 18 * fun_value[1] - 9 * fun_value[2] + 2 * fun_value[3]) / (6 * delta_x)
    u_xx = (2 * fun_value[0] - 5 * fun_value[1] + 4 * fun_value[2] - 1 * fun_value[3]) / delta_x ** 2
    return u_x, u_xx
x = sp.symbols('x')
# 第二题
print("-" * 200)
print("question 2")

max_index = 7
indices = list(range(max_index))  # 用于检验格式精度的指数
max_polynomial_index = 11
polynomial_indices = list(range(max_polynomial_index))  # 构造多项式函数的项数
parameters = [random.uniform(-10, 10) for _ in range(max_polynomial_index)]  # 随机生成多项式系数
f = sum(parameter * x ** index for parameter in parameters for index in polynomial_indices)
f_x = sp.diff(f, x, 1)
f_xx = sp.diff(f, x, 2)
delta_x = [0.1 ** index for index in indices]  # 不断减小的delta_x
x_0 = random.uniform(-1, 1)

u_1 = [diff_1(f, x_0, delta_x[index]) for index in indices]
u_x_1, u_xx_1 = zip(*u_1)
u_2 = [diff_2(f, x_0, delta_x[index]) for index in indices]
u_x_2, u_xx_2 = zip(*u_2)
u_x_s = f_x.subs(x, x_0)
u_xx_s = f_xx.subs(x, x_0)

print(f'f(x)={f}')
print("first derivative ", u_x_s, u_x_1, u_x_2)
print("second derivative ", u_xx_s, u_xx_1, u_xx_2)
e_x_1 = [(-u_x_s + u_x_1[index]) / delta_x[index] ** 2 for index in indices]
e_xx_1 = [(-u_xx_s + u_xx_1[index]) / delta_x[index] for index in indices]
e_x_2 = [(-u_x_s + u_x_2[index]) / delta_x[index] ** 3 for index in indices]
e_xx_2 = [(-u_xx_s + u_xx_2[index]) / delta_x[index] ** 2 for index in indices]  # 误差项除以对应阶数

plt.figure(figsize=(14, 8))
plt.subplot(2, 2, 1)
plt.plot(indices, e_x_1)
plt.xticks(indices, [f'{d:.{max_index - 1}f}' for d in delta_x], rotation=30)
plt.subplot(2, 2, 2)
plt.plot(indices, e_x_2)
plt.xticks(indices, [f'{d:.{max_index - 1}f}' for d in delta_x], rotation=30)
plt.subplot(2, 2, 3)
plt.plot(indices, e_xx_1)
plt.xticks(indices, [f'{d:.{max_index - 1}f}' for d in delta_x], rotation=30)
plt.subplot(2, 2, 4)
plt.plot(indices, e_xx_2)
plt.xticks(indices, [f'{d:.{max_index - 1}f}' for d in delta_x], rotation=30)
plt.show()
# 第三题
print("-" * 200)
print('question 3')
max_index = 5
max_polynomial_index = 3
indices = list(range(max_index))  # 用于检验格式精度的指数
polynomial_indices = list(range(max_polynomial_index))  # 当项数为3时没有截断误差
parameters = [random.uniform(-10, 10) for _ in range(max_polynomial_index)]  # 随机生成多项式系数
f = sum(parameter * x ** index for parameter in parameters for index in polynomial_indices)
g = sp.sin(x)


def solve_error(f):  # 求误差
    f_x = sp.diff(f, x, 1)
    f_xx = sp.diff(f, x, 2)
    delta_x = [0.1 ** index for index in indices]  # 不断减小的delta_x
    x_0 = random.uniform(-1, 1)
    u_1 = [diff_1(f, x_0, delta_x[index]) for index in indices]
    u_x_1, u_xx_1 = zip(*u_1)
    u_2 = [diff_2(f, x_0, delta_x[index]) for index in indices]
    u_x_2, u_xx_2 = zip(*u_2)
    u_x_s = f_x.subs(x, x_0)
    u_xx_s = f_xx.subs(x, x_0)
    e_x_1 = [-u_x_s + u_x_1[index] for index in indices]
    e_xx_1 = [-u_xx_s + u_xx_1[index] for index in indices]
    e_x_2 = [-u_x_s + u_x_2[index] for index in indices]
    e_xx_2 = [-u_xx_s + u_xx_2[index] for index in indices]
    return e_x_1, e_x_2, e_xx_1, e_xx_2


e_x_1, e_x_2, e_xx_1, e_xx_2 = solve_error(f)
print("舍入误差：")
print(e_x_1)
print(e_x_2)
print(e_xx_1)
print(e_xx_2)
e_x_1, e_x_2, e_xx_1, e_xx_2 = solve_error(g)
print("截断误差和舍入误差")
print(e_x_1)
print(e_x_2)
print(e_xx_1)
print(e_xx_2)

print("-" * 200)
