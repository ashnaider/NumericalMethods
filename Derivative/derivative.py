"""
Функции для получения 
численных значений первой и второй производной
используя формулу, полученную из полинома Ньютона
с конечными разностами

    * first_deriv - первая численная производная
    * second_deriv - вторая численная производная 

Автор: Шнайдер Антон
"""


def first_deriv(table, exp, h, i_start):
    """Первая численная производная"""
    res = 0.0
    sign = 1.0
    for i in range(exp):
        res += (table[i + 2][i_start] / (i + 1) ) * sign
        sign *= -1.0
    res /= h
    return res

def second_deriv(table, h, i_start):
    """Вторая численная производная для полинома Ньютона 5й степени"""
    res = table[3][i_start] - table[4][i_start]
    res += (11.0 * table[5][i_start]) / 12.0 
    res -= (5.0 * table[6][i_start]) / 6.0
    res *= 10000
    return res