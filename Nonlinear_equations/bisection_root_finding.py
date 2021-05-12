"""
Функция для нахождения
корня функции методом бисекции
    
    * root_by_bisection_method - 
        Нахождение корня функции 
        используя метод бисекции

Author: Шнайдер Антон
"""

from func import *   # аналитическая функция
from plot_func import *  # для построения графика

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # служебные утилиты

def root_by_bisection_method(fun, a, b, eps, max_iter=200):
    """Нахождение корня функции 
       используя метод бисекции"""

    if fun(a) < fun(b):
        a, b = b, a

    i = 0
    while (True):
        # если модуль разности 
        # концов отрезков
        # равен нулю 
        # с заданной точностью
        if within_eps(a, b, eps):
            print("abs(b - a) = {b} - {a}"
            " = {bma} < eps, f(a) = {fa:.4f}"
            "".format(a=a, b=b, bma=b-a, fa=fun(a)))
            print("i = ", i+1)
            # возвращаем положение икса(а) и выходим
            return a

        # получаем среднюю точку по икс
        c = (a + b) / 2.0
        fc = fun(c)  # значение функции в ней
        
        # выводим информацию на текущем шаге
        print("[a{i}; b{i}] = [{a:.4f}; {b:.4f}],"
        " => c = (a{i} + b{i})/2 = {c:.4}, "
        "fc = {fc:.4f}".format(i=i, a=a, b=b, c=c, fc=fc))

        i += 1
        curr = fun(a) * fc  # f(a) * f(c) 

        if curr < 0: # если меньше нуля
            # новая граница справа равна с
            b = c
        elif curr > 0: # если больше нуля
            # новая граница слева равна с
            a = c
        elif within_eps(curr, 0, eps):
            # если равно нулю, завершаем
            return c
        elif i > max_iter:
            # если кол-во итераций 
            # превышает максимум - выходим
            return c
    

if __name__ == "__main__":

    a = 0.6  # границы 
    b = a+1  # интервала
    eps = 0.01  # заданная точность

    # находим корень с заданной точностью
    root = root_by_bisection_method(func, a, b, eps)
    print("root: {:.7f}".format(root))

    # строим график
    plot_func(func, -1, 1.5, root, eps, 
        title="Finding root using bisection method")



