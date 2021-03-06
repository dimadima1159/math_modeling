import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1000, 10)


def radio_function(v, t):
  F = b - k * v
  dvdt = F/m
  return dvdt

b = 1
k = 2
m = 10
v_0 = 2
solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
