"""
Функции для интерполяции методом полнома Лагранжа,
а также визулизации

    * func - аналитически заданная функция
    * Lagrangian_polynom - интерполяция в точке х, по заданным узловым точкам
    * my_over_round - округление с избытком

Автор: Шнайдер Антон
"""


import math  # импортируем библиотеку math для работы с мат. функциями
import matplotlib.pyplot as plt # для построения графиков
import numpy as np  # для работы с массивами

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


src_file = "data/lagrangian_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'a']) # читаем файл в словарь data

x_points = data['x']  # массив координат х
y_points = [func(i) for i in x_points] # массив точных значений у

POINT_ALPHA = data['a'][0]  # точка а 
actual_value = func(POINT_ALPHA) # точное значение в точке а
# аппроксимированное значение в точке а 
approximate_value = Lagrangian_polynom(POINT_ALPHA, x_points, y_points)  

# вывод информации с выравниванием
print(f"{'Actual value for point ':<30}{POINT_ALPHA}{': '}{actual_value:.4f}")
print(f"{'Approximate value for point ':<30}{POINT_ALPHA}{': '}{approximate_value:.4f}")

x = np.arange(4, 10, 0.3)  # координаты х для графика
y = [func(i) for i in x]   # координаты у для аналитической функции

# координаты у для аппроксимирующей функции
newy = [Lagrangian_polynom(i, x_points, y_points) for i in x]

# построение графика
plt.figure()  # инициализация
plt.plot(x, y, label='Actual')  # график аналитической функции
plt.plot(x, newy, label='Interpolation')  # аппроксимация
plt.title("Lagrangian interpolation") # установка заголовка
plt.xlabel("X")  
plt.ylabel("Y").set_rotation(0)
# обозначаем узловые точки
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.show()




