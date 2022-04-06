import numpy as np

def array_info(array):
    print(array)
    print('ndim:',array.ndim)
    print('shape:',array.shape)
    print('dtype:',array.dtype)
    print('itemsize:',array.itemsize)
    print('nbytes:',array.nbytes)
    print("strides:",array.strides)
    
a1 = np.array([1,2,3,4,5,6])
a2 = np.array([[1,2,3],
              [4,5,6]])
a3 = np.array([[[0,1],
              [2,3]],
               
              [[4,5],
              [6,7]]])

# array_info(a3)

m1 = np.arange(1, 5)
m2 = np.arange(3, 7)
# m2 = np.sort(m2, axis=1)[::-1]

print(np.dot(m1, m2))
# print(np.matmul(m1, m2))

