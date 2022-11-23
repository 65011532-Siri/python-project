import numpy as np
arr = np.array([[2,3,2],[4,2,5],[2,2,7]], dtype="float32")
print(arr)
print(np.where(arr == 2)[1][-2])
arr [0,0] = 0
print(arr)
np.savetxt("try.txt", arr, fmt="%f")
arr2 = np.loadtxt("try.txt")
x = np.ndim(arr2)
print(x)
x = arr2 [0,0]
print(x)