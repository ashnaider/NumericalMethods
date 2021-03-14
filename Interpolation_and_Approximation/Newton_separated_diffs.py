"""
Функции для интерполяции методом полинома Ньютона
используя разделенные разности,
а также визулизации

    * get_Newton_separated_diffs_table - получить таблицу разделенных разностей
    * Newton_separated_diffs_interpol - интерполяция в точке х, по коэффициентам из таблицы разностей

Автор: Шнайдер Антон
"""


import numpy as np  # импортируем библиотеку NumPy, для работы с массивами
import matplotlib.pyplot as plt # импортируем PyPlot для построения графиков

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



src_file = "data/newton_separated_diffs_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# заданы координаты узловых точек 
x_points = data['x']
y_points = data['y']

# получаем таблицу разделенных разностей
table = get_Newton_separated_diffs_table(x_points, y_points)

# вывод информации
print("Approximation value in point x=1: ", Newton_separated_diffs_interpol(1, table, x_points))

# координаты аппроксимирующей функции для графика
x = np.arange(0, 7, 0.3)
y = [Newton_separated_diffs_interpol(i, table, x_points) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Interpolation') # график функции
plt.title("Newton polynomial interpolation")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("img/Newton_separated_diffs_interpol.png")
plt.show()