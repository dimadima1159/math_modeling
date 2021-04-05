import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.1)

def diff_func(w,t):
  x, y = w
  
  dx_dt = 3*x - 2*y + (np.exp(3*t))/(np.exp(t)+1)
  dy_dt = x - (np.exp(3*t))/ ((np.exp(t) + 1))
  
  return dx_dt, dy_dt

x0 = 5
y0 = -7
w0 = x0, y0
sol = odeint(diff_func, w0, t)

plt.plot(t, sol[:,1], 'b')
plt.plot(t, sol[:,0], 'r')

plt.legend()
plt.show()
