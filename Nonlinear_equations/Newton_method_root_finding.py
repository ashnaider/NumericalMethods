"""
Функция для нахождения
корня нелинейного уравнения 
методом Ньютона
    
    * simple_iteration - 
        Нахождение корня  
        используя метод Ньютона

    * func_deriv -
        первая производная функции

Author: Шнайдер Антон
"""

from func import *   # аналитическая функция
from plot_func import *  # для построения графика
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from utils import *  # служебные утилиты

def Newton_root_finding_method(fun, fun_deriv, a, b, eps=0.01, max_iter=200):
    """Корень нелинейного уравнения методом Ньютона"""
    x_next = (a+b)/2  # начальное приближение
    x_prev = x_next   # запоминаем предыдущее значение


    i = 0
    while True:
        # получаем след. значение по формуле
        x_next = x_next - fun(x_next) / fun_deriv(x_next)
        print("{:.5f} - {:.5f} / {:.5f}".format(x_prev, fun(x_next), fun_deriv(x_next)))
        print("x_next: {:.5f}".format(x_next))  # печатаем его

        i += 1
        # если модуль разницы текущего 
        # и предудыщего значения 
        # меньше чем эпсилон 
        # или превышено кол-во итераций
        if within_eps(x_next, x_prev, eps) or i > max_iter:
            print("diff = x_next - x_prev = {:.5f} - {:.5f} = {:.7f}".format(x_next, x_prev, abs(x_prev - x_next)))
            # выходим
            break

        x_prev = x_next  # запоминаем предыдущее значение

    return x_next  # возвращаем корень


def func_deriv(x):
    """ПРоизводная аналитически заданной функции"""
    return 1.0 / (x + 2) - 4.0 * x**3.0

if __name__ == "__main__":
    a = 0.6  # границы 
    b = a+1  # интервала
    eps = 0.001  # заданная точность

    # находим корень с заданной точностью
    root = Newton_root_finding_method(func, func_deriv, a, b, eps)
    print("root: {:.7f}".format(root))

    # строим график
    plot_func(func, -1, 1.5, root, eps, 
        title="Finding root using Newthon method", save=True)




                    