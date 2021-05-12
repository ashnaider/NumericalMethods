"""
    * plot_func - Строит график функции 
                и отмечает корень
"""

# библиотека для построение графиков
import matplotlib.pyplot as plt  
import numpy as np  # для работы с массивами

def plot_func(fun, a, b, root, eps, title="Root finding", save=False):
    """Строит график функции 
        и отмечает корень"""
    
    # иксы и игреки на интервале [a,b]
    x = np.arange(a, b, 0.01)  
    y = [fun(i) for i in x] 

    # значение функции в корне
    fc = fun(root)  
    min_y, max_y = min(y), max(y)
    min_x, max_x = min(x), max(x)

    # заголовок графика
    plt.title(title)

    plt.plot(x, y, label="Function")  # граифк функции
    # plt.gca().set_aspect('equal', adjustable='box')

    plt.plot([min_x, max_x], [0, 0], color="blue", label="X, Y")
    plt.plot([0, 0], [min_y, max_y], color="blue")

    # ориентиры для корня на графике
    plt.plot([a, b], [fc, fc], color="orange", linestyle="dashed")
    plt.plot([root, root], [min_y, max_y], color="orange", 
                                             linestyle="dashed")
    


    # отмечаем точку корня на графике
    plt.scatter(([root]), ([fc]), s=70, zorder=3, color="red", 
                label="root: x = {:.4f}\n"
                "{tab}y = {:.4f}\nEPS={}".format(root, fun(root), eps, tab=8*" "))
    
    plt.legend()  # отображаем подписи

    if (save):
        underscore_title = title.replace(" ", "_", len(title))
        plt.savefig(f"img/{underscore_title}.jpg")

    plt.show()  # показываем график