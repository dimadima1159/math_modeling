import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений

def move_func(s, t):
  (x1, v_x1, y1, v_y1,
   x2, v_x2, y2, v_y2,
   x3, v_x3, y3, v_y3) = s

# Диманика первого тела под влиянием второго и третьего

  dxdt1 = v_x1
  dv_xdt1 = (- G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 - G * m3 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)

  dy_dt1 = v_y1
  dv_ydt1 = (- G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 - G * m3 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 + k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5 + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)

  dxdt2 = v_x2
  dv_xdt2 = (- G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 - G * m3 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)

  dy_dt2 = v_y2
  dv_ydt2 = (- G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 - G * m3 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5 + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)

  dxdt3 = v_x3
  dv_xdt3 = (- G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 - G * m2 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 + k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)

  dy_dt3 = v_y3
  dv_ydt3 = (- G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 - G * m2 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5 + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)

  return (dxdt1, dv_xdt1, dy_dt1, dv_ydt1,
          dxdt2, dv_xdt2, dy_dt2, dv_ydt2,
          dxdt3, dv_xdt3, dy_dt3, dv_ydt3)

# Определяем начальные значения и параметры, входящие в систему диф. уравнений
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = - 149 * 10**9
v_x20 = 0
y20 = 0
v_y20 = - 30000

x30 = 0
v_x30 = 15000
y30 = 149 * 10**9
v_y30 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)

m1 = 1.1 * 10**30
q1 = - 1.1 * 10**20

m2 = 2.1 * 10**30
q2 = 2.1 * 10**20

m3 = 3.6 * 10**30
q3 = - 3.1 * 10**20

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

# Решаем систему диф. уравнений

sol = odeint(move_func, s0, t)

def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
    return ((x1, y1), (x2, y2), (x3, y3))

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')


def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()
