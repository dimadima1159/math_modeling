def changer(a,b):
  x=3*a-b
  return x
#print(changer())
print(changer(3,2))

def my_func(a=1,b=2):
 x=3*a-b
 return x 
print(my_func())
print(my_func(3,2))
print(my_func(5))
print(my_func(b=5))
print(my_func(b=5,a=3))