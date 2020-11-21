from lab_3_task_1 import g
import numpy as np

t = np.arange(0,5,0.1)
print(t)
x0 = 3
v0x = 5

x = x0+v0x*t
print(x)

y0 = 3
v0x = 5

y = y0+v0x*t-((g*t**2)/2)
print(y)
a = np.zeros((len(t),3))
for i in range(len(t)):
  a[i,0] = t[i]
  a[i,1] = x[i]
  a[i,2] = y[i]
print(a)










