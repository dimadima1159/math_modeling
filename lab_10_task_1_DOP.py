import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)


def diff_func(q, t):
    x, y, z = q
    dx_dt = 3 * x - y + z
    dy_dt = x + y + z
    dz_dt = 4 * x - y + 4 * z
    return dx_dt, dy_dt, dz_dt


x0 = -71
y0 = 1
z0 = -3
q0 = x0, y0, z0

sol = odeint(diff_func, q0, t)

plt.plot(t, sol[:, 0], 'b')
plt.plot(t, sol[:, 1], 'r')
plt.plot(t, sol[:, 2], 'g')
plt.show()
