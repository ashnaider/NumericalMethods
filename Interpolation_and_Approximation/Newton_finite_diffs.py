"""
Функции для интерполяции методом полинома Ньютона
используя конечные разности,
а также визулизации

    * get_Newton_finite_diffs_table - получить таблицу конечных разностей
    * Newton_finite_diffs_interpol - интерполяция в точке х, по коэффициентам из таблицы разностей
    * get_t - значение компонента t

Автор: Шнайдер Антон
"""


import math  # импортируем библиотеку math для работы с мат. функциями
import matplotlib.pyplot as plt # для построения графиков
import numpy as np  # для работы с массивами

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
    


src_file = "data/newton_finite_diffs_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# координаты узловых точек
x_points = data['x']
y_points = data['y']

step = 1  # величина постоянного шага

# получаем таблицу
table = get_Newton_finite_diffs_table(x_points, y_points)
print(table)

# координаты аппроксимирующей функции для графика
x = np.arange(0, 7, 0.3)
y = [Newton_finite_diffs_interpol(table, i, step) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Interpolation') # график функции
plt.title("Newton finite difference polynomial interpolation")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("img/Newton_finite_diffs_interpol.png")
plt.show()