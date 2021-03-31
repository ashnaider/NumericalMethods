"""
Функции для интерполяции методом полинома Ньютона
используя конечные разности

    * get_Newton_finite_diffs_table - получить таблицу конечных разностей
    * Newton_finite_diffs_interpol - интерполяция в точке х, по коэффициентам из таблицы разностей
    * get_t - значение компонента t

Автор: Шнайдер Антон
"""


import math  # импортируем библиотеку math для работы с мат. функциями
import matplotlib.pyplot as plt # для построения графиков
import numpy as np  # для работы с массивами


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # также служебные утилиты

def get_Newton_finite_diffs_table(x_points, y_points):
    """Поличить таблицу конечных разностей"""
    check_arr_size(x_points, y_points) # проверяем размеры

    size = len(x_points) + 1  # высота таблицы
    # создаем массив массивов
    table = np.empty(size, dtype=list)
    # первые две колонки иксы и игреки 
    table[0] = x_points
    table[1] = y_points

    # по каждой колонке, начиная со второй
    for i in range(2, size):
        tmp_list = []
        for j in range(size - i):
            # новое значение в новом столбце
            # равно разности двух в предыдущем
            curr = table[i-1][j+1] - table[i-1][j]
            tmp_list.append(curr)
        table[i] = tmp_list
    
    return table  # возвращаем таблицу

def get_t(x, x0, step):
    """Получить значение компонента t"""
    return (x - x0) / step

def Newton_finite_diffs_interpol(table, x, step=None):    
    """Получить приближенное значение для икса"""
    if (step == None):
        step = table[0][1] - table[0][0]

    # получаем t  
    t = get_t(x, table[0][0], step)

    size = len(table)
    fact = 1  # переменная, накапливающая факториал
    num = 1  # накапливает значение для числителя
    sum = 0
    for i in range(1, size):
        if i > 2:
            fact *= i - 1
            num *= (t - i + 2)
        if i == 2:
            num = t
            
        # получаем значение разности очередного порядка
        product = table[i][0]
        product *= num  # домножаем на числитель
        product /= fact  # делим на знаменатель

        sum += product  # увеличиваем сумму
    return sum  #возвращаем сумму
    
