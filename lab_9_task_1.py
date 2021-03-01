import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

def radio_function(N, t):
  dNdt = k * N
  return dNdt

N_0 = 10
k = 1/20

solve_Bi = odeint(radio_function, N_0, t)

plt.plot(t, solve_Bi[:,0])
plt.show()
