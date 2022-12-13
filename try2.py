import numpy as np
a = np.array([[8,2,3,],[3,5,6],[1,8,9],[1,5,6],[2,8,9]])
print(a)
a = a[a[:, 0].argsort()]
#c = np.copy(a)
print(a)
#for i in b:
#    c = np.delete(a, (i), axis=0)
#print(a)
#print(c)