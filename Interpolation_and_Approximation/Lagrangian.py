"""
Функции для интерполяции методом полнома Лагранжа

    * func - аналитически заданная функция
    * Lagrangian_polynom - интерполяция в точке х, по заданным узловым точкам
    * my_over_round - округление с избытком

Автор: Шнайдер Антон
"""


import math  # импортируем библиотеку math для работы с мат. функциями
import matplotlib.pyplot as plt # для построения графиков
import numpy as np  # для работы с массивами

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # также служебные утилиты

def func(x):  # функция, заданная аналитически
    """ln(x)^(11/2)"""
    return math.pow(math.log(x), 11.0/2.0)  # возвращяем её значение в точке х

def Lagrangian_polynom(x, x_points, y_points):  
    """аппроксимация значения в точке х на основании узловых точек""" 
    
    check_arr_size(x_points, y_points) # проверяем что массивы точек одинковой длины 

    sum = 0  # аккумулятор суммы
    # cумма с i по r (кол-во узловых точек, то есть длина массива)
    for i in range(len(x_points)):  
        #  временный аккумулятор произведения 
        product = y_points[i]  
        for j in range(len(x_points)):  # произведение с j по r, j != i
            if j != i: # если j == i, переходим к след итерации
                # получаем произведение по формуле    
                product *= (x - x_points[j]) / (x_points[i] - x_points[j])  
        sum += product  # увеличиваем сумму
    return sum  # возвращаем аппроксимированное значение в точке х

def my_over_round(x, c):
    """Функция для округления с избытком"""
    newx = round(x, c)  # округляем с точностью до 'c' знаков после запятой
    newx += 10 ** -c  # прибавляем один в последний разряд
    return newx  # возвращаем результат





