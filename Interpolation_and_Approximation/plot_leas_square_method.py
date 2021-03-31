from least_square_method import *
    
src_file = "Interpolation_and_Approximation/data/least_square_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# заданы координаты точек 
x_points = data['x']
y_points = data['y']

# получаем коэффициенты 
coeffs = get_least_square_method_coeffs(x_points, y_points)

# икс и игрек для графика
x = np.arange(0, 7, 0.3)
y = [line_approximate(i, coeffs) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Approximation') # график функции
plt.title("Least square method")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("Interpolation_and_Approximation/img/Least_square_method.png")
plt.show()