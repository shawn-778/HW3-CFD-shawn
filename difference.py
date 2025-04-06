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
