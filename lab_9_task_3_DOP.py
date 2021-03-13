import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 365, 0.1)

def radio_function(a, t):
    dvdt = (R**2*L)/W*a
    return dvdt
a_0=147
R=6400
L=3.827 * 10**26
W_0= 0 
W=(2*np.pi)/365
solve_Bi = odeint(radio_function, a_0, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
