import matplotlib.pyplot as plt
import numpy as np
import math

from func import *

a = -1.5
b = 2

# a = 0.6
# b = a + 1

x = np.arange(a, b, 0.1)
y = [func(i) for i in x]

plt.plot(x, y)
# plt.xlim(-3, 3)
# plt.ylim(-3, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

