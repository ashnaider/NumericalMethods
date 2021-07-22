"""
Функции для численного решения
задачи Коши для обыкновенного дифференциального
уравнения явным методом Эйлера

    * Eulers_method - метод Эйлера

Автор: Шнайдер Антон
"""


# библиотека для построение графиков
import matplotlib.pyplot as plt  
import numpy as np  # для работы с массивами
import pandas as pd # для работы с табличными данными 
from dataclasses import make_dataclass
# для создания классов данных 

# дифференциальные уравнения
from diff_equations import *


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *



def Eulers_method(x0, y0, a, b, h):
    """
    Euler's numerical method
    for solving differential equation
    with initial condition x0, y0
    on the interval [a; b]
    """

    Iteration = make_dataclass("Iteration", 
                    [
                        ("xi", float), 
                        ("yi", float), 
                        ("delta_yi", float),
                        ("actual_yi", float),
                        ("eps", float)
                    ])

    # создаём таблицу и
    # заполняем первую строку таблицы начальными значениями
    df = pd.DataFrame([Iteration(x0, y0, 0, diff_eq_solution(x0), 
                        abs(y0 - diff_eq_solution(x0)))])
    
    # получаем иксы на интервале [a;b+h]
    # с шагом h
    x = np.arange(a, b+h, h)

    i = 1
    # начинаем итерироваться со второго элемента
    for xi in x[i:]:
        # получаем предыдущие значения x и y
        # из таблицы 
        y_prev = df.iloc[i-1]["yi"]
        x_prev = df.iloc[i-1]["xi"]

        # вычисляем правуб часть ДУ f(x, y)
        fi = f(x_prev, y_prev)
        delta_y = h * fi  # получаем дельта у
        yi = y_prev + delta_y  # получаем новый игрек

        k = 5  # вывод информации на экран
        print(f"y{i} = y{i-1} + h * f(x{i-1}, y{i-1})"
                  f" = {y_prev:.{k}f} + {h:.{k}f} * "
                  f"({x_prev:.{k}f} + {y_prev:.{k}f})^2"
                  f" = {yi:.{k}f}")

        # вычисляем настоящее аналитическое
        # значение решения в точке xi
        actual_y = diff_eq_solution(xi)

        # добавляем в таблицу новую строку с данными
        df = df.append([Iteration(xi, yi, delta_y, actual_y, abs(actual_y - yi))], 
                            ignore_index=True)
        i += 1

    print(df)  # печатаем таблицу
    return df  # возвращаем таблицу
    

# если файл запущен напрямую
if __name__ == "__main__":
    # читаем данные из файла
    data = read_data("Diff_equations/data/h=0.05.txt", ["a", "b", "h", "x0", "y0"])
    x0 = data["x0"][0]
    y0 = data["y0"][0]
    a = data["a"][0]
    b = data["b"][0]

    h1 = 0.1
    h2 = 0.05

    # рассчитываем таблицу для h=0.1 и h=0.05
    df = Eulers_method(x0, y0, a, b, h1)
    df2 = Eulers_method(x0, y0, a, b, h2)

    df.to_csv(f"Diff_equations/output/Euler_h={h1}.csv", float_format='%1.5f', sep=";")
    df2.to_csv(f"Diff_equations/output/Euler_h={h2}.csv", float_format='%1.5f', sep=";")

    plt.xlabel("X")  # обозначаем оси
    plt.ylabel("Y")
    plt.title("Задача Коши явным методом Эйлера\ny' = (y + x)^2\ny(0)=0")
    plt.plot(df.xi, df.yi, label=f"h={h1}")  # строим 
    plt.plot(df2.xi, df2.yi, label=f"h={h2}") # графики
    plt.scatter(df.xi, df.yi)  # отмечаем узловые точки
    plt.scatter(df2.xi, df2.yi, label="узловые точки")
    plt.legend()
    plt.grid()
    # plt.savefig("img/Eulers_method_diff_eq.png")
    plt.show()  # отображаем графики


