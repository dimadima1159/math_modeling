from lab_3_task_1 import g
from math import cos, tan , sqrt, pi
h = 100 
b = 30*pi/180
a = pi/3
v = sqrt((tan(b)**2*g*h)/(2*(cos(a)**2*(1-tan(b)*tan(a)))))
print (v)
T = 200
z = 300
from lab_3_task_1 import e,k,h
from math import pi
N = (2/sqrt(pi))*(h/(k*T)**(3/2))*(e**(-z/k*T))*(z**(T/2))
print (N)