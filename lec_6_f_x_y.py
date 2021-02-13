import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(radius=10):
  x = np.arange(-2*radius, 2*radius, 0.1)
  y = np.arange(-2*radius, 2*radius, 0.1)

  rad = np.linspace(1,10,12)

  X, Y = np.meshgrid(x, y)
  fxy = X**2 + Y**2
  plt.contour(X, Y, fxy, levels=rad**2)
  plt.axis('equal')
  plt.show()
circle_plotter()
