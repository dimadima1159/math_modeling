import numpy as np
import matplotlib.pyplot as plt
 
def function(x, a, b):
    y = []
    for i in range(len(x)):
        if x[i] < a:
            y.append(a**2)
        if x[i] >= a and x[i] <= b:
            y.append(x[i]**2)
        if x[i] > b:
            y.append(b**2)
    return x, y
 
sol = function(np.linspace(-3, 3, 300), 0, 2)
plt.plot(sol[0], sol[1])
 
plt.show()
