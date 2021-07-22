"""
Служебные функции 
    * check_arr_size - проверить массивы на размер
    * read_data - прочитать данные из файла
Автор: Шнайдер Антон
"""


import inspect  # для полезной информации об объектах в Pyhton 


def within_eps(a, b, eps):
    """Проверка равности чисел a и b
        с заданной точностью eps"""
    # return ((a - eps) < b) and (b < (a + eps))
    return abs(a - b) < eps


def check_arr_size(lhs, rhs):
    """Проверяет размеры массивов на равенство"""
    if (len(lhs) != len(rhs)):  # если длины массивов разные
        func = inspect.stack()[1].function  # получаем имя функции, из которой была запрошена проверка
        raise ValueError("In function %s: x and y arrays have different lengths" % func)  # кидаем исключение


def read_data(file_name, headers):
    """Из указанного файла прочитать данные с указанными заголовками"""
    res = {}  # инициализируем словарь
    # открываем файл на чтение
    with open(file=file_name, mode='r') as f:
        # читаем каждую строку в файле
        for line in f:
            # если строка пустая 
            if line.strip() == "":
                continue  # переходим на след итерацию

            # ищем позицию символа ":" в строке
            semi_index = line.index(':')
            # получаем в заголовок строки 
            # (срез массива до индекса символа ":")
            curr_header = line[:semi_index]
            
            # если заголовок один из тех, что нам нужен
            if curr_header in headers:
                # читаем данные из него в массив
                res[curr_header] = list(map( lambda x: float(x.replace(',', '').strip()), line[semi_index+1:].split(',')))

        return res  # возвращаем словарь


            
    

