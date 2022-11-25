import numpy as np
arr = np.array([[2,3,2],[4,2,5],[2,2,7]], dtype="float32")
print(arr)
print(np.where(arr == 2)[1][-2])
print(arr)
y = str("r")
x = str("a"+y+"r")
