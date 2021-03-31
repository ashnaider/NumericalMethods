"""
Численное дифференцирование
полиномом Ньютона
используя конечные разности,
а также визулизации

    * func - аналитически заданная производная
    * actual_first_deriv - аналитически заданная производная

Автор: Шнайдер Антон
"""

import matplotlib.pyplot as plt # библиотека для графиков
import numpy as np  # для работы с массивами
import math  # мат. функции

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *   # импортируем служебные утилиты 
# полином Ньютона с использованием конечных разностей
from Interpolation_and_Approximation.Newton_finite_diffs import *  
from derivative import *  # производные

def func(x):
    """Аналитически заданная исходная функция"""
    return 60.0 * (1 - math.cos((math.pi * x * 55.0) / -9.0))

def actual_first_deriv(x):
    """Аналитическая производная функции"""
    return (1100.0 * math.pi * math.sin((math.pi * x * 55.0) / (9.0))) / 3.0


a0 = 30  # начальная точка
step = 0.04  # величина постоянного шага
exp = 3  # степень интерполирующего полинома
p = 7  # кло-во узловых точек (0-7)
deriv_p = 5  # кол-во узловых точек для производной
 
# узловые точки аналитической функции
x_points = np.arange(a0, a0 + p * step, step)  
y_points = [func(i) for i in x_points]

# получаем таблицу конечных разностей для функции
table = get_Newton_finite_diffs_table(x_points, y_points)

# узловые точки для численной производной
d1_points = [first_deriv(table, exp, step, i) for i in range(deriv_p)]
# узловые точки для аналитической производной
actual_d1_points = [actual_first_deriv(i) for i in x_points]

# таблица конечных разностей для узловых точек
# численной производной
table2 = get_Newton_finite_diffs_table(x_points[:deriv_p], d1_points)

# координаты интерполирующей функции для графика
x = np.arange(a0, a0 + p * step, 0.005)
y = [Newton_finite_diffs_interpol(table, i, step) for i in x]

# координаты для интерполяции численной производной по точкам
x1 = np.arange(a0, a0 + deriv_p * step, 0.005)
y2 = [Newton_finite_diffs_interpol(table2, i, step) for i in x1]

# координаты аналитической производной
y3 = [actual_first_deriv(i) for i in x1]

# разбиваем график на два подграфика
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(7, 8))
fig.suptitle('Численное дифференцирование') # заголовок
# подзаголовки
ax1.set_title('Интерполяция исходной функции\nпо узлам')
ax2.set_title('Первая производная')

# построение функций и производных
ax1.plot(x, y, label='Исходная функция') 

ax2.plot(x, y, label='Функция') 
ax2.plot(x1, y2, label='Численная производная') 
ax2.plot(x1, y3, label='Аналитическая производная')

# отображение узловых точек
ax1.scatter(x_points, y_points, marker='o', color='green', label='Узловые точки')

ax2.scatter(x_points, y_points, marker='o', color='green', label='Узлы функции')
ax2.scatter(x_points[:deriv_p], d1_points, marker='o', label='Узлы численной производной')

ax1.grid()  # отображение
ax2.grid()  # сетки

ax1.legend()  # обозначение
ax2.legend()  # элементов графика
# отступы на графике
plt.tight_layout(pad=1.08)
# сохранение (опционально)
# plt.savefig('img/num_diff_by_func.png')
plt.show() # показать график
