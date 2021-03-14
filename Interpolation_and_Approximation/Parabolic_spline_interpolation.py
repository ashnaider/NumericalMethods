"""
Функции для интерполяции методом параболических сплавнов
и их визуализация

    * get_Parabolic_spline_table - рассчитать таблицу с коэффициентами 
    * Parabolic_spline - интерполяция в точке икс, используя таблицу

Автор: Шнайдер Антон    
"""


import numpy as np  # для работы с массивами
import matplotlib.pyplot as plt # для построения графиков

from utils import *  # вспомогательные функции

def get_Parabolic_spline_table(x_points, y_points, D=0, deriv_pos='begin'):
    """Получить таблицу коэффициентов по заданным узловым точкам и производной"""
    check_arr_size(x_points, y_points) # проверка массивов на размер

    size = len(x_points) - 1

    # таблица коэффициентов
    table = {
            "x": x_points,
            "y": y_points,
            "h": [],
            "z": [],
            "a": y_points,
            "b": [],
            "c": [],
        }
    

    # зполняем столбец h
    for i in range(size):
        # разница следующего и предыдущего икса
        curr = table["x"][i + 1] - table["x"][i]
        table["h"].append(curr) # добавляем в таблицу

    # заполняем столбец z
    for i in range(size):
        # разница  следующего и предыдущего игрека
        curr = table["y"][i + 1] - table["y"][i]
        # делим на разницу след. и пред. икса
        curr /= table["h"][i]
        table["z"].append(curr) # добавляем в таблицу

    # заполняем столбец b
    table["b"] = np.empty(size+1)  # выделяем необходимое место

    # переводим значение параметра в нижний регистр
    deriv_pos = deriv_pos.lower()  

    # если производная задана в начале интервала
    if deriv_pos == 'begin':
        start = 1    # итерируемся с начала
        stop = size  # к концу
        step = 1     # с шагом один
        b_step = -1  # b[i] = 2z[i] - b[i-1]
        # значение b[0] равно производной в начале интервала
        table["b"][0] = D

    # если производная задана в конце интервала
    elif deriv_pos == 'end':
        start = size - 1  # итерируемся с конца
        stop = -1         # к началу
        step = -1         # с шагом минус один
        b_step = 1    # b[i] = 2z[i] - b[i+1]  
        # значение b[r] равно производной в конце интервала
        table["b"][size] = D

    else:
        # кидаем исключение, если параметр deriv_pos неправильно задан
        raise ValueError("Unknown parameter for deriv_pos: " + deriv_pos)

    for i in range(start, stop, step):
        # получаем значение b[i-1] или b[i+1]
        # в зависимости от заданных параметров
        prev_b = table["b"][i + b_step]

        # рассчитываем значение b[i]
        curr = 2 * table["z"][i]
        curr -= prev_b

        # записываем значение в таблицу
        table["b"][i] = curr

    # заполняем значения параметра c
    for i in range(size):
        # разность следующего и текущего b
        curr = table["b"][i+1] - table["b"][i]
        # делённая на 2h
        curr /= (2 * table["h"][i])

        table["c"].append(curr) # записываем в таблицу

    return table


def Parabolic_spline(x, table):
    """Интерполяция в точке икс используя таблицу коэффициентов"""
    # кол-во интервалов на один меньше чем узловых точек
    size = len(table["x"]) - 1 

    # если икс вне границ интервала (экстраполяция)
    # по умолчанию равен среднему
    interval = int((size - 1) / 2) 

    for i in range(size):
        # если икс лежит в каком-то подинтервале
        if table["x"][i] <= x and x <= table["x"][i+1]:
            interval = i  # запоминаем
            break  # и выходим
          
    # получаем значение многочлена
    res = table["a"][interval]
    res += table["b"][interval] * (x - table["x"][interval])
    res += table["c"][interval] * pow(x - table["x"][interval], 2)

    return res  # возвращаем результат


src_file = "data/parabolic_spline_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# заданы координаты узловых точек 
x_points = data['x']
y_points = data['y']

#  получаем таблицу коэффициентов
table = get_Parabolic_spline_table(x_points, y_points, D=0, deriv_pos='end')

print(table)

# координаты интерполирующей функции для графика
x = np.arange(1, 6, 0.05)
y = [Parabolic_spline(i, table) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Interpolation') # график функции
plt.title("Parabolic spline interpolation")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
#plt.savefig("img/Parabolic_spline.png")
plt.show()





