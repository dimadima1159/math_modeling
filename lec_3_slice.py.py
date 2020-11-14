import numpy as np
a = [5,6,7,10,8,4,3]
print(a[:]) # start=1, stop=len(a), step=1
print(a[3::2])
print(a[::3])
print(a[::])

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A[0,1:2:1])
print(A[1:2:1,0])
print(A[1, :])
B = A[:, ::-1]
print('A', A)
print('B', B)
