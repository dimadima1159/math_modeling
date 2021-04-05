import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.01, 5, 0.1)


def diff_func(z, x):
    y, w = z
    dy_dx = w
    dw_dx = (w ** 2 - ((3*y**2)/np.sqrt(x)))/y
    return dy_dx, dw_dx


y0 = 0.01
w0 = 1
z0 = y0, w0
sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b')
plt.plot(x, sol[:, 1], 'r')
plt.show()
