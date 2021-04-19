"""
Класс, с методами построения графиков
методов численного интегрирования 

Параметры интегрирования:
a - левая граница
b - правая граница
h - шаг разбиения

Автор: Шнайдер Антон
"""


import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from integral import *  # функции из файла integral.py
from Interpolation_and_Approximation.Lagrangian import *

import matplotlib.pyplot as plt  # для работы с графиками
import matplotlib.patches as patches  # для дополнительных фигур на графике
import numpy as np  # бибилиотека для работы с массивами

class Integral_Plots:
    def __init__(self, a, b, h, func):  # конструктор класса
        self.a = a  # пределы 
        self.b = b  # интегрирования
        self.h = h  # шаг разбиения

        self.func = func  # аналически заданная функция

         # количество узлов
        self.r = int(abs(self.b - self.a) / self.h) 

        # иксы на интервале a-b для графика
        # игреки на интервале a-b для графика
        self.x = np.arange(self.a, self.b+self.h, 0.01)  
        self.y = [self.func(i) for i in self.x]  

        # иксы для интегрирования
        self.x_bar = np.arange(self.a, self.b, self.h)  

    def plot_func(self, fig, axs):
        """строит аналитически заданную функцию на, 
        пеереданном в качестве параметра, графике"""
        # график аналитической функции
        axs.plot(self.x, self.y, color="red", label="Actual function", linewidth=3.0)  

    def _add_h(self, axs):
        """добавляет значение шага разбиения на график"""
        handles, labels = axs.get_legend_handles_labels()
        handles.insert(0, patches.Patch(color='none', label=("h = " + str(self.h))))
        return handles

    def plot_left_rectangles(self):
        """Построение левых прямоугольников"""
        # игреки для левых прямоугольников
        y_left = [self.func(i) for i in self.x_bar]  

        # начинаем построение графика
        fig, axs = plt.subplots()  

        axs.title.set_text("Left rectangles integral")
        self.plot_func(fig, axs)
        # строим левые прямоугольники
        axs.bar(self.x_bar, y_left, width=self.h, align='edge', 
                    edgecolor='black', 
                    label="Left rectangles")
        # показываем подписи элементов графика
        plt.legend(handles=self._add_h(axs), loc='upper left')
        plt.savefig("Integrals/img/left_rectangles.png")                  
        plt.show()  # показываем график

    def plot_right_rectangles(self):
        """построение правых прямоугольников"""
        # игреки для правых прямоугольников
        y_right = [self.func(i+self.h) for i in self.x_bar]  
        
        fig, axs = plt.subplots()  

        axs.title.set_text("Right rectangles integral")
        self.plot_func(fig, axs)  # строим аналитическую функцию
        # строим правые прямоугольники
        axs.bar(self.x_bar, y_right, width=self.h, align='edge', 
                    edgecolor='black', 
                    label="Right rectangles")
        # показываем подписи элементов графика
        plt.legend(handles=self._add_h(axs), loc='upper left')
        plt.savefig("Integrals/img/right_rectangles.png")                  
        plt.show()  # показывам график

    def plot_central_rectangles(self):
        """построение центральных прямоугольников"""
        # игреки для центральных 
        y_center = [self.func(i+self.h/2) for i in self.x_bar]  

        fig, axs = plt.subplots()  # начинаем построение графика

        axs.title.set_text("Central rectangles integral")
        self.plot_func(fig, axs)
        # строим центральные прямоугольники
        axs.bar(self.x_bar, y_center, width=self.h, align='edge',
                    edgecolor='black', 
                    label="Central rectangles")
        # показываем подписи элементов графика
        plt.legend(handles=self._add_h(axs), loc='upper left')    
        plt.savefig("Integrals/img/central_rectangles.png")                  
        plt.show()  # показывам график

    def plot_trapezoids(self):
        # чтобы нарисовать трапецию, нужно собрать 
        # координаты четырех её точек 
        # начиная с левой нижней и против часовой стрелки.
        # Для удобства, сначала соберем только иксы 
        # а потом игреки
        x_trapez = np.arange(self.a, self.b+self.h, self.h)  # игреки для трапеций

        x_trapezoid_patches_coords = []
        for i in range(self.r):  # по количеству узлов
            tmp = [x_trapez[i], x_trapez[i+1]]
            # получаем координаты иксов для i-й трапеции
            x_trapezoid_patches_coords.append([tmp[0], tmp[1], tmp[1], tmp[0]])

        y_trapezoid_patches_coords = []
        for coord in x_trapezoid_patches_coords:
            # получаем координаты игреков для i-й трапеции
            tmp = [0, 0, self.func(coord[2]), self.func(coord[3])]
            y_trapezoid_patches_coords.append(tmp)

        fig, axs = plt.subplots() 
        axs.title.set_text("Trapezoid integral")
        self.plot_func(fig, axs)
        for i in range(self.r):  # строим трапеции
            # из массивов иксов и игреков, получим общий функцией zip
            # и разобьём их на массив пар координат x,y
            # и отобразим на графике
            label = "Trapezoids" if i == (self.r-1) else ""

            axs.add_patch(patches.Polygon(xy=list(zip(x_trapezoid_patches_coords[i], 
                                                    y_trapezoid_patches_coords[i])),
            edgecolor="black", label=label))
        # показываем подписи элементов графика
        plt.legend(handles=self._add_h(axs), loc='upper left')   
        plt.savefig("Integrals/img/Trapezoids.png") 
        plt.show()  # показывам график

    def plot_Simpson(self, r=2):
        """построение криволинейных страпеций для метода Симпсона"""
        node_x = np.arange(self.a, self.b + self.h, self.h)  # иксы и игреки
        node_y = [self.func(i) for i in node_x]           # в узловых точках

        intervals = (self.b - self.a) / self.h  # количество интервалов
        V = int(intervals / r)  # число элементарных отрезков
        elementary_segment = r * h  # длина элементраного отрезка

        fig, axs = plt.subplots()  # начинаем построение граифка
        axs.title.set_text("Simpson integral (r={})".format(r))  # добавляем подпись

        for i in range(V):
            label = "Curved trapezoids" if i == (V-1) else ""

            left_slice = i * r          # границы левого и правого
            right_slice = (i + 1) * r   # срезов по массивам узловых точек 

            # границы очередного 
            # элементарного отрезка
            segment_left = i * elementary_segment              
            segment_right = segment_left + elementary_segment  

            # получаем интерполирующую кривую на элементарном участке функции
            segment_x = np.arange(segment_left, segment_right, 0.01)
            segment_y = [
                Lagrangian_polynom(i, node_x[left_slice:right_slice+1], 
                                    node_y[left_slice:right_slice+1]) 
                for i in segment_x
                        ]

            axs.plot(segment_x, segment_y, color="black")  # строим кривую
            # заполняем площадь под ней, чтобы отобразить криволинейную трапецию
            axs.fill_between(segment_x, segment_y, color="tab:blue", 
                             edgecolor="black", label=label)
            
        self.plot_func(fig, axs)
        # показываем подписи элементов графика
        plt.legend(handles=self._add_h(axs), loc='upper left')
        plt.savefig("Integrals/img/Simpson(r={}).png".format(r)) 
        plt.show()  # показывам график


src_file = "Integrals/data/integral_data.txt"  # файл с данными
data = read_data(src_file, ['a', 'b', 'h'])  # читаем нужные строки
# получаем данные
a = data['a'][0]
b = data['b'][0]
h = data['h'][0]

# инициализируем класс интеграла 
integ = Integral_Plots(a, b, h, func_1)
integ.plot_left_rectangles()    # левые прямоугольники
integ.plot_right_rectangles()   # правые прямоугольники
integ.plot_central_rectangles() # центральные прямоугольники
integ.plot_trapezoids()         # трапеции

integ.plot_Simpson(r=2)         # криволинейные трапеции для Симпсона
integ.plot_Simpson(r=3)         # криволинейные трапеции для Симпсона
