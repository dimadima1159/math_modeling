import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(1, 365, 0.1)

def radio_function(W_0, t):
    dvdt = (R**2*L)/(W*a)
    return dvdt
a=147*10**6
R=6400
L=3.827*10**26 
W=(2*np.pi)/365
W_0=0
solve_Bi = odeint(radio_function, a, t)

plt.plot(t, solve_Bi[:, 0])
plt.show()
