"""
Функция для нахождения
корня нелинейного уравнения 
методом ложного положения
    
    * false_position_method - 
        Нахождение корня  
        используя метод ложного положения

Author: Шнайдер Антон
"""

from func import *   # аналитическая функция
from plot_func import *  # для построения графика

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # служебные утилиты

def false_position_method(fun, a, b, eps=0.01, max_iter=200):
    """метод ложного положения"""
    x_next = a    # начальное приближение 
    x_prev = x_next  # запоминаем предыдущее значение
    d = (a+b) / 2  # фиксированная точка d
    
    i = 0
    while True:
        print("{:.5f} - ({:.5f} - {:.5f}) / ({:.5f} - {:.5f}) * {:.5f}".format(
            x_next, d, x_next, fun(d), fun(x_next), fun(x_next)
        ))
        # получаем след. икс по формуле 
        x_next = x_next - fun(x_next) * (d - x_next) / (fun(d) - fun(x_next))
        print("x_next: {:.5f}\n".format(x_next))  # печатаем

        i += 1
        # если модуль разницы текущего 
        # и предудыщего значения 
        # меньше чем эпсилон 
        # или превышено кол-во итераций
        if within_eps(x_next, x_prev, eps) or i > max_iter:
            print("break: {:.5f} - {:.5f} = {:.5f}".format(x_next, x_prev, x_next - x_prev))
            # выходим
            break

        x_prev = x_next  # запоминаем предыдущее значение

    return x_next  # возвращаем корень


if __name__ == "__main__":
    a = 0.6  # границы 
    b = a+1  # интервала
    eps = 0.001  # заданная точность

    # находим корень с заданной точностью
    root = false_position_method(func, a, b, eps)
    print("root: {:.7f}".format(root))

    # строим график
    plot_func(func, -1, 1.5, root, eps, 
            title="Finding root using false position method")
