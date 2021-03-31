"""
Построение и визуализация
первой и второй производной
по табличным данным 
с использованем полинома Ньютона
с конечными разностями

Автор: Шнайдер Антон
"""

import matplotlib.pyplot as plt # библиотека для графиков
import numpy as np  # для работы с массивами

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *   # импортируем служебные утилиты 
# полином Ньютона с использованием конечных разностей
from Interpolation_and_Approximation.Newton_finite_diffs import *  
from derivative import *  # производные

src_file = "Derivative/data/num_diff_by_table.txt"  # файл с данными
data = read_data(src_file, ['t', 'y']) # читаем файл в словарь data

# заданы координаты узловых точек 
t_points = data['t']
y_points = data['y']

step = 0.01  # величина постоянного шага

# получаем таблицу конечных разностей
table = get_Newton_finite_diffs_table(t_points, y_points)

srez = 5  # количество узловых точек производной
exp = 5   # степень интерполирующего полинома

# узловые точки первой и второй производной
d1_points = [first_deriv(table, exp, step, i) for i in range(srez)]
d2_points = [second_deriv(table, step, i) for i in range(srez)]

# таблицы разделенный разностей для первой и второй производных
table2 = get_Newton_finite_diffs_table(t_points[:srez], d1_points)
table3 = get_Newton_finite_diffs_table(t_points[:srez], d2_points)

# координаты интерполирующей функции для графика
x = np.arange(0, 0.1, 0.005)
y = [Newton_finite_diffs_interpol(table, i, step) for i in x]

# координаты интерполяции производных для графика
x1 = np.arange(0, 0.05, 0.005)
y2 = [Newton_finite_diffs_interpol(table2, i, step) for i in x1]
y3 = [Newton_finite_diffs_interpol(table3, i, step) for i in x1]

# разбиение графика на подграфики
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(6, 10))
fig.suptitle('Численное дифференцирование')
# заголовки
ax1.set_title('Интерполяция исходной функции\nпо узлам')
ax2.set_title('Первая численная производная')
ax3.set_title('Вторая численная производная')

# построение графиков функций  
ax1.plot(x, y, label='Исходная функция') # график функции

ax2.plot(x, y, label='Исходная функция') # график функции
ax2.plot(x1, y2, label='Первая производная') # график функции

ax3.plot(x, y, label='Исходная функция') # график функции
ax3.plot(x1, y2, label='Первая производная') # график функции
ax3.plot(x1, y3, label='Вторая производная') # график функции

# отображение узловых точек
ax1.scatter(t_points, y_points, marker='o', color='green', label='Узловые точки')

ax2.scatter(t_points, y_points, marker='o', color='green', label='Узловые точки')
ax2.scatter(t_points[:srez], d1_points, marker='o', label='Узлы производной')

ax3.scatter(t_points, y_points, marker='o', color='green', label='Узловые точки')
ax3.scatter(t_points[:srez], d1_points, marker='o', label='Узлы первой производной')
ax3.scatter(t_points[:srez], d2_points, marker='o', label='Узлы второй производной')

ax1.grid()  # сетки
ax2.grid()
ax3.grid()

ax1.legend()  # отображение
ax2.legend()  # названий
ax3.legend()  # элементов
# отступы
plt.tight_layout(pad=1.8)
# сохранение
# plt.savefig('img/num_diff_by_table.png')
plt.show()
