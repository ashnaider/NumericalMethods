"""
Функция для нахождения
корня функции методом бисекции
и функция для построения графика

    * func - Аналитически заданная функция
    * within_eps - Проверка равности чисел a и b 
                с заданной точностью eps

    * root_by_bisection_method - 
        Нахождение корня функции 
        используя метод бисекции

    * plot_func - Строит график функции 
                и отмечает корень

Author: Шнайдер Антон
"""


import math  # библиотека с мат. функциями
# биьлиотека для построение графиков
import matplotlib.pyplot as plt  
import numpy as np  # для работы с массивами

def func(x):
    """Аналитически заданная функция"""
    return x**2 - math.pow(math.cos(x), 2)

def within_eps(a, b, eps):
    """Проверка равности чисел a и b
        с заданной точностью eps"""
    return ((a - eps) < b) and (b < (a + eps))

def root_by_bisection_method(fun, a, b, eps):
    """Нахождение корня функции 
       используя метод бисекции"""

    # проверяем, 
    # не равны ли нулю, с заданной точностью,
    # границы интервала
    if within_eps(fun(a), 0, eps):
        return a
    if within_eps(fun(b), 0, eps):
        return b
    
    i = 0
    while (True):
        # получаем среднюю точку по икс
        c = (a + b) / 2
        fc = fun(c)  # значение функции в ней
        
        # выводим информацию на текущем шаге
        print("[a{i}; b{i}] = [{a:.4f}; {b:.4f}],"
        " => c = (a{i} + b{i})/2 = {c:.4}, "
        "fc = {fc:.4f}".format(i=i, a=a, b=b, c=c, fc=fc))
        i += 1
    
        # если значение равно нулю
        # с заданной точностью
        if within_eps(fc, 0, eps):
            # возвращаем положение икса и выходим
            return c  

        elif fc > 0: # если больше нуля
            # новая граница справа равна с
            b = c
        elif fc < 0: # если меньше нуля
            # новая граница слева равна с
            a = c
    

def plot_func(fun, a, b, root):
    """Строит график функции 
        и отмечает корень"""
    
    # иксы и игреки на интервале [a,b]
    x = np.arange(a, b, 0.1)  
    y = [fun(i) for i in x] 

    # значение функции в корне
    fc = fun(root)  

    # заголовок графика
    plt.title("Finding root using Bisection method")
    plt.plot(x, y, label="Function")  # граифк функции

    # ориентиры для корня на графике
    plt.plot([a, b], [0, 0], color="orange", linestyle="dashed")
    plt.plot([root, root], [fun(a), fun(b)], color="orange", 
                                             linestyle="dashed")

    # отмечаем точку корня на графике
    plt.scatter(([root]), ([fc]), s=70, zorder=3, color="red", 
                label="root: x={:.4f}\nEPS={}".format(fc, eps))
    plt.legend()  # отображаем подписи
    plt.show()  # показываем график


if __name__ == "__main__":
    a = 0  # границы 
    b = 5  # интервала
    eps = 0.01  # заданная точность

    # находим корень с заданной точностью
    root = root_by_bisection_method(func, a, b, eps)
    print(root)

    # строим график
    plot_func(func, a, b, root)

