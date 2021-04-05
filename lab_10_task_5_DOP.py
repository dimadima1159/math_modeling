import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

y = np.arange(-1, 1, 0.1)


def diff_func(z, y):
    w, x = z
    dy_dx = w
    dw_dx = (x * w - 2 * y) / (1 - x ** 2)
    return dy_dx, dw_dx


x0 = 3
w0 = 0
z0 = w0, x0
sol = odeint(diff_func, z0, y)

plt.plot(y, sol[:, 0], 'b')
plt.plot(y, sol[:, 1], 'r')
plt.show()
