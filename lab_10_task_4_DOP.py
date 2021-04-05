import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1)


def diff_func(z, y):
    y, w = z
    dy_dx = w
    dw_dx = ((4 * x ** 2 + 1) * y - x * w) / x ** 2
    return dy_dx, dw_dx


y0 = 3
w0 = 0.1
z0 = y0, w0
sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'r')
plt.show()
