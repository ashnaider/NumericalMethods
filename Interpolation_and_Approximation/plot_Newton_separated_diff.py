
from Newton_separated_diffs import *

src_file = "Interpolation_and_Approximation/data/newton_separated_diffs_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# заданы координаты узловых точек 
x_points = data['x']
y_points = data['y']

# получаем таблицу разделенных разностей
table = get_Newton_separated_diffs_table(x_points, y_points)

# вывод информации
print("Approximation value in point x=1: ", Newton_separated_diffs_interpol(1, table, x_points))

# координаты аппроксимирующей функции для графика
x = np.arange(0, 7, 0.3)
y = [Newton_separated_diffs_interpol(i, table, x_points) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Interpolation') # график функции
plt.title("Newton polynomial interpolation")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("Interpolation_and_Approximation/img/Newton_separated_diffs_interpol.png")
plt.show()