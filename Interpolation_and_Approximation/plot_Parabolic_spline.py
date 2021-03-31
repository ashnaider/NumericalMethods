from Parabolic_spline_interpolation import *

src_file = "Interpolation_and_Approximation/data/parabolic_spline_data.txt"  # файл с данными
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
plt.savefig("Interpolation_and_Approximation/img/Parabolic_spline.png")
plt.show()

