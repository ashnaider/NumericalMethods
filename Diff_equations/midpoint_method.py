"""
Функции для численного решения
задачи Коши для обыкновенного дифференциального
уравнения методом средней точки

    * midpoint_method - метод Эйлера - Коши

Автор: Шнайдер Антон
"""

from diff_equations import *

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from utils import *

# библиотека для построение графиков
import matplotlib.pyplot as plt  
import numpy as np  # для работы с массивами
import pandas as pd # для работы с табличными данными 
from dataclasses import make_dataclass
# для создания классов данных 


def midpoint_method(x0, y0, a, b, h):
    """Задача Коши методом средней точки"""
    Iteration = make_dataclass("Iteration", 
                    [
                        ("xi", float), 
                        ("yi", float), 
                        ("yi_sq", float),
                        ("delta_yi", float),
                        ("actual_yi", float),
                        ("eps", float)
                    ])
    # создаём таблицу и
    # заполняем первую строку таблицы начальными значениями
    df = pd.DataFrame([Iteration(x0, y0, 0, 0, diff_eq_solution(x0), 
                        abs(y0 - diff_eq_solution(x0)))])

    # получаем иксы на интервале [a;b+h]
    # с шагом h
    x = np.arange(a, b+h, h)

    i = 1
    for xi in x[i:]:
        # получаем предыдущие значения x и y
        # из таблицы 
        y_prev = df.loc[i-1]['yi']
        x_prev = df.loc[i-1]['xi']

        xi_sq = x_prev + h / 2.0  # получаем х и у с волной
        yi_sq = y_prev + (h / 2.0) * f(x_prev, y_prev)

        k = 8  # вывод информации
        print(f"~x{i} = x{i-1} + h/2 = {x_prev:.2f} + {h:.2f} / 2 = {xi_sq:.{k}f}")
        print(f"~y{i} = y{i-1} + h/2 * f(x{i-1}, y{i-1}) = "
              f"{y_prev:.{k}f} + {h:.2f} / 2 * f({x_prev:.2f}, {y_prev:.{k}f}) = "
              f"{y_prev:.{k}f} + {h:.2f} / 2 * {f(x_prev, y_prev):.{k}f} = {yi_sq:.{k}f}")

        delta_y = h * f(xi_sq, yi_sq) # вычисляем дельта игрек
        yi = yi_sq + delta_y  # получаем игрек для текущего узла

        # вывод информации
        print(f" y{i} = ~y{i} + h * f(~x{i}, ~y{i}) = "
              f"{yi_sq:.{k}f} + {h:.2f} * f({xi_sq:.3f}, {yi_sq:.{k}f}) = "
              f"{yi_sq:.{k}f} + {h:.2f} * "
              f"{f(xi_sq, yi_sq):.{k}f}"
              f" = {yi:.{k}f}\n")

        # точное значение аналитического решения
        actual_y = diff_eq_solution(xi)
        eps = abs(actual_y - yi)  # погрешность
        # добавляем в таблицу новую строку
        df = df.append([Iteration(xi, yi, yi_sq, delta_y, actual_y, eps)], ignore_index=True)
        i+=1
    
    print(df, "\n")  # печатаем таблицу
    return df  # возвращаем таблицу


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
    print(f"h = {h1}")
    df = midpoint_method(x0, y0, a, b, h1)
    print(f"h = {h2}")
    df2 = midpoint_method(x0, y0, a, b, h2)

    # сохраняем таблицу как csv файл
    df.to_csv(f"Diff_equations/output/midpoint_h={h1}.csv", float_format='%1.5f', sep=";")
    df2.to_csv(f"Diff_equations/output/midpoint_h={h2}.csv", float_format='%1.5f', sep=";")

    plt.xlabel("X")  # обозначаем оси
    plt.ylabel("Y")
    plt.title("Задача Коши методом средней точки\n"
                "y' = (y + x)^2\ny(0)=0")
    plt.plot(df.xi, df.yi, label=f"h={h1}")  # строим 
    plt.plot(df2.xi, df2.yi, label=f"h={h2}") # графики
    plt.scatter(df.xi, df.yi)  # отмечаем узловые точки
    plt.scatter(df2.xi, df2.yi, label="узловые точки")
    plt.legend()
    plt.grid()  # сохраняем график
    # plt.savefig("img/midpoint_method_diff_eq.png")
    plt.show()  # отображаем графики