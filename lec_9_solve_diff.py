import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0, 10**6, 100)
# запись диф. уравнения в виде функции
def radio_function(m,t):
  dmit = -k * m
  return dmit
m_b = 10
k = 1,61 * 10**-6
solve_Bi = odeint(radio_function,m_b,t)
plt.piot(t,solve_Bi[1,0])
plt. show