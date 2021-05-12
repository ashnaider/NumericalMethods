from func import *   # аналитическая функция
from plot_func import *  # для построения графика

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # служебные утилиты

def secant_method(fun, a, b, eps=0.01, max_iter=200):
    """метод секущих (модификация метода Ньютона)"""
    x0 = a  # начальное 
    x1 = b  # приближение
    x_next = 0
    i = 0
    while True:
        print("xi-1 = {:.5f}".format(x0))
        print("xi = {:.5f}".format(x1))
        print("f(xi-1) = {:.5f}".format(fun(x0)))
        print("f(xi) = {:.5f}".format(fun(x1))) 
        # следующих икс по формуле
        x_next = x1 - fun(x1) * (x1 - x0) / (fun(x1) - fun(x0)) 
        print("x_next: {:.5f}\n".format(x_next)) # печатаем

        i += 1
        # если модуль разницы текущего 
        # и предудыщего значения 
        # меньше чем эпсилон 
        # или превышено кол-во итераций
        if within_eps(x_next, x1, eps) or i > max_iter:
            print("break: {:.5f} - {:.5f} = {:.5f}".format(x_next, x1, x_next - x1))
            # выходим
            break

        # запоминаем предыдущие значения
        x0 = x1
        x1 = x_next

    print("i: ", i)
    return x_next  # возвращаем корень


if __name__ == "__main__":
    a = 0.6  # границы 
    b = a+1  # интервала
    eps = 0.001  # заданная точность

    # находим корень с заданной точностью
    root = secant_method(func, a, b, eps)
    print("root: {:.7f}".format(root))

    # строим график
    plot_func(func, -1, 1.5, root, eps, 
        title="Finding root using secant method")

