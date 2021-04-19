"""
Функции для численного 
интегрирования 

    * func_1 - Аналитически заданная исходная функция для задания 4.2
    * func_2 - Аналитически заданная исходная функция для задания 4.3
    * left_rectangles_integral - метод левых прямоугольников
    * right_rectangles_integral - метод правых прямоугольников 
    * central_rectangles_integral - метод центральных прямоугольников
    * trapezoid_integral - метод трапеций
    * Simpson - интегрирование методом Симпсона (r=2) и
                               методом Симпсона 3/8 (r=3)

Параметры интегрирования:
a - левая граница
b - правая граница
h - шаг разбиения

Параметры интегрирования можно задать в файле integral_data.txt

Автор: Шнайдер Антон
"""

import math  # библиотека с мат. функциями
import numpy as np  # библиотека для работы с массивами


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # служебные утилиты

def func_1(x):
    """Аналитически заданная исходная функция для задания 4.2"""
    denom = (math.exp(x) - 1)
    if (denom == 0):
        return 0
    return x**3 / denom    

def func_2(x):
    """Аналитически заданная исходная функция для задания 4.3"""
    res = func_1(x)
    res *= math.cos((55 * math.pi * x) / (-9))
    return res

def left_rectangles_integral(a, b, h, fun):
    """метод левых прямоугольников"""
    x = np.arange(a, b, h)  # иксы с а по b с шагом h
    y = np.array([fun(i) for i in x])  # значения функции в этих точках
                                       # начиная с х0 
    
    sum = y.sum()  # сумма значений функции в точках на всём интервале
    res = sum * h  # домножаем на шаг разбиения
    return res

def right_rectangles_integral(a, b, h, fun):
    """метод правых прямоугольников"""
    x = np.arange(a, b, h)  # иксы с а по b с шагом h
    y = np.array([fun(i+h) for i in x])  # значения функции в этих точках
                                         # начиная с х1 
    sum = y.sum()  # сумма значений функции в точках на всём интервале
    res = sum * h  # домножаем на шаг разбиения
    return res


def central_rectangles_integral(a, b, h, fun):
    """метод центральных прямоугольников"""
    x = np.arange(a, b+h, h)  # иксы с а по b+h с шагом h
    y = np.array([fun(i) for i in x])  # значения функции в этих точках

    sum = 0
    # сумма попарных смежных значений игреков деленная на два
    for i in range(len(y) - 1):
            sum += (y[i] + y[i+1]) / 2
    
    return sum * h  # домножаем на шаг разбиения

def trapezoid_integral(a, b, h, fun):
    """метод трапеций"""
    x = np.arange(a, b+h, h)  # иксы с а по b+h с шагом h
    y = np.array([fun(i) for i in x])   # значения функции в этих точках

    sum = 0
    # сумма попарных смежных значений игреков
    for i in range(len(y) - 1):
            sum += y[i] + y[i+1]
    
    # домножаем на шаг разбиения и делим на два
    res = sum * (h / 2)
    return res


def Simpson(func, a, b, h, r=2):
    """интегрирование методом Симпсона (r=2) и
            методом Симпсона 3/8 (r=3)"""
    if r == 2:  # коэффициенты Котеса для степени 2
        Cotes_coeffs = (1/6, 4/6, 1/6)
    elif r == 3: # коэффициенты Котеса для степени 3
        Cotes_coeffs = (1/8, 3/8, 3/8, 1/8)
    else:
        print("No Simpson methods for r = ", r)
        return -1

    intervals = (b - a) / h  # кол-во интервалов
    V = int(intervals / r)   # кол-во элементарных отрезков 

    x = np.arange(a, b+h, h)  # иксы и игреки узловых точек
    y = [func(i) for i in x]  # с шагом разбиения h 

    sum = 0
    for j in range(V):
        for i in range(r+1):
            # умножаем необходимый коэффициент Котеса
            # на соответствующий игрек
            sum += Cotes_coeffs[i] * y[r * j + i] 

    sum *= r * h  
    return sum


def print_integrals(a, b, h):
    li = left_rectangles_integral(a, b, h, func_2)  # левые прямоугольники
    print("left int: ", li)

    ri = right_rectangles_integral(a, b, h, func_2)  # правые прямоугольники
    print("right int: ", ri)

    h1 = 0.5   # шаги разбиения
    h2 = 0.25
    h3 = 0.125
    # центральные прямоугольники и порядок точности
    ci_h1 = central_rectangles_integral(a, b, h1, func_2)  
    ci_h2 = central_rectangles_integral(a, b, h2, func_2)
    ci_h3 = central_rectangles_integral(a, b, h3, func_2)
    print("central int for h1: ", ci_h1)
    print("central int for h2: ", ci_h2)
    print("central int for h3: ", ci_h3)
    print("central int 1_pogreshnost: ", ci_h1 - ci_h2)
    print("central int 2_pogreshnost: ", ci_h1 - ci_h3)

    # метод трапеций и порядок точности
    trap_int_h1 = trapezoid_integral(a, b, h1, func_2)
    trap_int_h2 = trapezoid_integral(a, b, h2, func_2)
    trap_int_h3 = trapezoid_integral(a, b, h3, func_2)
    print("trapez for h1: ", trap_int_h1)
    print("trapez for h2: ", trap_int_h2)
    print("trapez for h3: ", trap_int_h3)
    print("Pogrshnost 1: ", (trap_int_h1 - trap_int_h2) / 3)
    print("Pogrshnost 2: ", (trap_int_h1 - trap_int_h3) / 3)

    # метод Симпсона и порядок точности
    simp_r2_h1 = Simpson(func_2, a, b, h1, r=2)
    simp_r2_h2 = Simpson(func_2, a, b, h2, r=2)
    simp_r2_h3 = Simpson(func_2, a, b, h3, r=2)
    print("Simpson (r=2) for h1: {:.5f}".format(simp_r2_h1))
    print("Simpson (r=2) for h2: {:.5f}".format(simp_r2_h2))
    print("Simpson (r=2) for h3: {:.5f}".format(simp_r2_h3))
    print("Pogreshnost 1: {:.6f}".format((simp_r2_h1 - simp_r2_h2)/15.0))
    print("Pogreshnost 2: {:.6f}".format((simp_r2_h1 - simp_r2_h3)/15.0))

    # метод Симпсона 3/8 и порядок точности
    simp_r3_h1 = Simpson(func_2, a, b, h1, r=3)
    simp_r3_h2 = Simpson(func_2, a, b, h2, r=3)
    simp_r3_h3 = Simpson(func_2, a, b, h3, r=3)
    print("Simpson (r=3) for h1: {:.5f}".format(simp_r3_h1))
    print("Simpson (r=3) for h2: {:.5f}".format(simp_r3_h2))
    print("Simpson (r=3) for h3: {:.5f}".format(simp_r3_h3))
    print("Pogreshnost 1: {:.6f}".format((simp_r3_h1 - simp_r3_h2)/15.0))
    print("Pogreshnost 2: {:.6f}".format((simp_r3_h1 - simp_r3_h3)/15.0))


if __name__ == "__main__":  # если файл запущен напрямую
    src_file = "Integrals/data/integral_data.txt"  # файл с данными
    data = read_data(src_file, ['a', 'b', 'h'])  # читаем указанные строки

    # получаем значения
    a = data['a'][0]
    b = data['b'][0]
    h = data['h'][0]

    # печатаем значения интегралов
    print_integrals(a, b, h)

