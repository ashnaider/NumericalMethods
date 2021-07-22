"""
Функции для численного решения
задачи Коши для обыкновенного дифференциального
уравнения методом Рунге-Кутты
а также построение графиков

    * Runge_Kutte_method - метод Рунге-Кутты

Автор: Шнайдер Антон
"""

# библиотека для построение графиков
import matplotlib.pyplot as plt  
import numpy as np  # для работы с массивами

from diff_equations import *


def Runge_Kutte_method(x0, y0, a, b, h):
    x = np.arange(a, b, h)

    p, xi_p, k = 9, 2, 11
    str = f"i/v-xi{' '*(xi_p-2)}-ri{' '*(p-2)}-delta_yi{' '*(p-8)}"\
          f"-yi{' '*(p-2)}-actual_y{' '*(p-8)}-eps{' '*(p-3)}"
    str = str.replace('-', '\t')
    print(str)
    str = "-" * 92 + "\n"
    
    res = [y0]
    y_prev = y0
    actual_y = 0
    eps = abs(y0 - actual_y)
    i = 0
    for xi in x:
        r1 = h * f(xi, y_prev)
        r2 = h * f(xi + h/2, y_prev + r1/2)
        r3 = h * f(xi + h/2, y_prev + r2/2)
        r4 = h * f(xi + h, y_prev + r3)

        delta_y = 1/6 * (r1 + 2*r2 + 2*r3 + r4)
        actual_y = diff_eq_solution(xi)
        eps = abs(y_prev - actual_y)

        blank = '_' * k
        str += f"{i}/1 {xi:.{xi_p}f} {r1:.{p}f} {blank} {y_prev:.{p}f} "\
            f"{actual_y:.{p}f} {eps:.{p}f}\n"
        str += f"{i}/2 {xi + h/2:.{xi_p}f} {r2:.{p}f} "\
            f"{blank} {blank} {blank}\n"
        str += f"{i}/3 {xi + h/2:.{xi_p}f} {r3:.{p}f} {blank} "\
            f"{blank} {blank}\n"
        str += f"{i}/4 {xi + h:.{xi_p}f} {r4:.{p}f} {delta_y:.{p}f} "\
            f"{blank} {blank} {blank}\n"

        str = str.replace(" ", "\t")
        str += "-" * 92 + "\n"

        yi = y_prev + delta_y
        y_prev = yi
        res.append(yi)
        i += 1

    print(str)
    return res
            


if __name__ == "__main__":
    x0, y0 = 0, 0
    a, b = 0, 0.5
    h1 = 0.1
    h2 = h1 / 2
    
    x1 = np.arange(a, b+h1, h1)
    x2 = np.arange(a, b+h2, h2)
    y1 = Runge_Kutte_method(x0, y0, a, b+h1, h1)
    y2 = Runge_Kutte_method(x0, y0, a, b+h2, h2)
    y1.pop(), y2.pop()

    actual_x = np.arange(a, b, 0.01)
    actual_y = [diff_eq_solution(i) for i in actual_x]
    
    plt.xlabel("X")  # обозначаем оси
    plt.ylabel("Y")
    plt.title("Задача Коши методом Рунге-Кутты\ny' = (y + x)^2\ny(0)=0")
    plt.plot(x1, y1, label=f"h={h1}")  # строим 
    plt.plot(x2, y2, label=f"h={h2}") # графики
    plt.plot(actual_x, actual_y, label="Аналитическое решение")
    plt.scatter(x1, y1)  # отмечаем узловые точки
    plt.scatter(x2, y2, label="узловые точки")
    plt.legend()
    plt.grid()  # сохраняем изображение
    plt.show()  # отображаем графики


