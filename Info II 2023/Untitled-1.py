
import numpy as np

m = np.array([2, 4, 6, 8])

np.save('seguimiento2.npy', a)

m2 = np.load('seguimiento2.npy')
print(m == m2)