"""
Функция для нахождения
корня нелинейного уравнения 
методом простых итераций
    
    * simple_iteration - 
        Нахождение корня  
        используя метод простых итераций

    * func_preob -
        преобразованная функция

Author: Шнайдер Антон
"""

from func import *   # аналитическая функция
from plot_func import *  # для построения графика

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # служебные утилиты

def simple_iteration(fun, a, b, eps=0.01, max_iter=200):
    """Нахождение корня методом простой итерации"""
    x_next = abs(a + b) / 2  # начальоне приближение 
    x_prev = x_next   # запоминаем предыдущее

    i = 0
    while True:
        # получаем следующее значение
        x_next = fun(x_next)
        # печатаем его
        print("root: {:.5f}".format(x_next))

        i += 1
        # если модуль разницы концов отрезка
        # равен нулю с заданной точностью
        # или превышено кол-во итераций
        if within_eps(x_next, x_prev, eps) or i > max_iter:
            # завершаем роботу
            break

        # запоминаем предыдущее
        x_prev = x_next

    print("i: ", i)  # количество итераций
    return x_next  # возвращаем корень


def func_preob(x):
    """Преобразованная функция"""
    return math.sqrt(math.sqrt(math.log(x+2.0) + 0.5))

if __name__ == "__main__":

    a = 0.6  # границы 
    b = a+1  # интервала
    eps = 0.001  # заданная точность

    # находим корень с заданной точностью
    root = simple_iteration(func_preob, a, b, eps)
    print("root: {:.7f}".format(root))
    print("f(root): ", func(root))

    # строим график
    plot_func(func, -1, 1.5, root, eps, 
        title="Finding root using simple iterations method")
