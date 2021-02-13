import matplotlib.pyplot as plt
import numpy as np
def lissaju(a=3,A=1,b=6,B=1):
  t=np.arange(1,10,0.01)
  D = np.pi/2
  x=A*np.sin(a*t+D)
  y=B*np.sin(b*t)
  plt.plot(x,y)
  plt.show()
lissaju()
