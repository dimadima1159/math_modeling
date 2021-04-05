import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def diff_func(z, t):
  w, y = z

  dy_dt = w
  dw_dt = -4 * w - 5 * y

  return dy_dt, dw_dt

y0 = 4
w0 = -1

z0 = w0, y0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:,1], 'b')
plt.plot(x, sol[:,0], 'r')

plt.legend()
plt.show()
