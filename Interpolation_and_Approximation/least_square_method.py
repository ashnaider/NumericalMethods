"""
Функции для аппроксимации методом наименьших квадратов
и их визуализация

    * get_least_square_method_coeffs - получить коэффициенты
    * line_approximate - аппроксимация прямой в точке икс

Автор: Шнайдер Антон
"""


import numpy as np  # для работы с массивами
import matplotlib.pyplot as plt # для построения графиков

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

    
src_file = "data/least_square_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# заданы координаты точек 
x_points = data['x']
y_points = data['y']

# получаем коэффициенты 
coeffs = get_least_square_method_coeffs(x_points, y_points)

# икс и игрек для графика
x = np.arange(0, 7, 0.3)
y = [line_approximate(i, coeffs) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Approximation') # график функции
plt.title("Least square method")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("img/Least_square_method.png")
plt.show()



