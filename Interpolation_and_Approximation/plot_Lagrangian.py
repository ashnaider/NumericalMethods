from Lagrangian import * 

src_file = "Interpolation_and_Approximation/data/lagrangian_data.txt"  # файл с данными
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

