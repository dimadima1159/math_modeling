import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(1, 100, 1)


def radio_function(v, t):
    dig = a_0 -(y * v**2)/2
    return dig


y = 0.5
m = 70
a_0 = 3
v_0 = 0

solve_Bi = odeint(radio_function, a_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
