"""
Функции для интерполяции методом полинома Ньютона
используя разделенные разности

    * get_Newton_separated_diffs_table - получить таблицу разделенных разностей
    * Newton_separated_diffs_interpol - интерполяция в точке х, по коэффициентам из таблицы разностей

Автор: Шнайдер Антон
"""


import numpy as np  # импортируем библиотеку NumPy, для работы с массивами
import matplotlib.pyplot as plt # импортируем PyPlot для построения графиков


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *   # импортируем служебные утилиты 

def get_Newton_separated_diffs_table(x_points, y_points):
    """Функция для получения таблицы коэффициентов полинома"""
    
    check_arr_size(x_points, y_points)  # проверяем размеры массивов

    size = len(x_points)
    pointer = -1

    accum = np.empty(size, dtype=list)  # создаём массив списков размера size
    accum[pointer] = y_points  # разделенные разности 0-го порядка есть сами значения y

    for i in range(size - 1, 0, -1):  # итерации начинаем с конца к началу
        tmp = []  # массив для новой колонки 
        for j in range(i):
            curr = (accum[i][j] - accum[i][j+1]) # разница двух смежных в предыдущей колонке
            # делим на разницу иксов в основании
            curr /= (x_points[j] - x_points[j + size-i]) 
            tmp.append(curr)  # добавляем в колонку новое значение
        pointer -= 1
        accum[pointer] = tmp  # добавляем в массив новую колонку
 
    return accum  # возвращаем таблицу разделенных расностей

def Newton_separated_diffs_interpol(x, table, x_points): 
    """Вычисление значения аппроксимирующей функции в точке х"""
    size = len(x_points)
    sum = 0  # аккумулятор суммы
    for i in range(size):  # по каждой колонке таблицы
        tmp = table[size - 1 - i][0]  # значение на диагонали, то есть первый элемент в колонке
        for j in range(i):  
            tmp *= (x - x_points[j])  # домножаем на соответствующие разности иксов
        sum += tmp  # увеличиваем сумму
    return sum  # возвращаем результат
