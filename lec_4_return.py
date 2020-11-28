def my_func(a=1,b=0):
 x1=3*a-b
 x2=3*a+b
 return(x1,x2)
tmp=my_func(4,3)
print(tmp[0])
print(my_func()[1])