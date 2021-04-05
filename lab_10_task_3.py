import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)


def diff_func(z, x):
    w, y = z

    dy_dt = w
    dw_dt = np.sin(x) + np.cos(x)

    return dy_dt, dw_dt


y0 = 3
w0 = 0
z0 = w0, y0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'r')

plt.show()
