"""
Функции для аппроксимации методом наименьших квадратов

    * get_least_square_method_coeffs - получить коэффициенты
    * line_approximate - аппроксимация прямой в точке икс

Автор: Шнайдер Антон
"""


import numpy as np  # для работы с массивами
import matplotlib.pyplot as plt # для построения графиков


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *  # вспомогательные функции

def get_least_square_method_coeffs(x_points, y_points):
    """Получить таблицу коэффициентов для аппроксимации прямой"""
    check_arr_size(x_points, y_points) # проверяем размер массивов

    size = len(x_points)

    # начальная инициализация элементов
    # в матрице Грамма
    f2f2 = size 
    f1f1 = f1f2 = f1y = f2y = 0
    
    # вычисляем скаларные произведения в матрице Грамма
    for i in range(size):
        f1f1 += x_points[i] * x_points[i]
        f1f2 += x_points[i]
        f1y += x_points[i] * y_points[i]
        f2y += y_points[i]

    # находим определители для метода Крамера
    d = f1f1 * f2f2 - f1f2 * f1f2
    d1 = f1y * f2f2 - f1f2 * f2y
    d2 = f1f1 * f2y - f1y * f1f2

    # получаем коэффициенты
    c1 = d1 / d
    c2 = d2 / d

    # возвращаем словарь коэффициентов
    return {'c1':c1, 'c2':c2}


def line_approximate(x, coeffs):
    """Аппроксимация в точке икс по заданным коэффициентам"""
    return x * coeffs['c1'] + coeffs['c2']





