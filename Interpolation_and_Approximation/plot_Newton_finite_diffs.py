from Newton_finite_diffs import *


src_file = "Interpolation_and_Approximation/data/newton_finite_diffs_data.txt"  # файл с данными
data = read_data(src_file, ['x', 'y']) # читаем файл в словарь data

# координаты узловых точек
x_points = data['x']
y_points = data['y']

step = 1  # величина постоянного шага

# получаем таблицу
table = get_Newton_finite_diffs_table(x_points, y_points)
print(table)

# координаты аппроксимирующей функции для графика
x = np.arange(0, 7, 0.3)
y = [Newton_finite_diffs_interpol(table, i, step) for i in x]

# построение графика
plt.figure() # инициализация
plt.plot(x, y, label='Interpolation') # график функции
plt.title("Newton finite difference polynomial interpolation")
plt.xlabel("X")
plt.ylabel("Y").set_rotation(0)
# обозначение узловых точек
plt.scatter(x_points, y_points, marker='o', color='green', label='Node points')
plt.legend()
plt.grid()
plt.savefig("Interpolation_and_Approximation/img/Newton_finite_diffs_interpol.png")
plt.show()