n=int(input('введите натуральное число:'))
a = 1
b = 2
print(a, b, end=" ")
for i in range(3,n+1):
    print(a+b, end=" ")
    c = a
    a = b
    b = c+a