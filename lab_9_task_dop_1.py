import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
h0 = 1000
t = np.arange(0,h0)


def radio_function(v, x):
    dNdt = F /v
    return dNdt


MZ = 6 * 10 ** 24
G = 6.67 * 10 ** -11
R = 6317 * 10**3
F = (G * MZ) / ((R + h0) ** 2)
v_0 = 3

solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
