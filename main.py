import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)

#horizontal slicing
print(b[:])
print(b[0:2])
print(b[1:3])
print(b[2:3])

#vertical slicing
print(b[:,0:2])
print(b[:,2:3])
print(b[0:2,0:2])