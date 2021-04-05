import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.1)


def diff_func(z, t):
    y, w = z
    dy_dt = w
    dw_dt = np.sqrt(1 - w ** 2)
    return dy_dt, dw_dt


y0 = 0.1
w0 = 0
z0 = y0, w0
sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 0], 'b')
plt.plot(t, sol[:, 1], 'r')
plt.show()
