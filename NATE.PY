import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print("Horizontal Stack:\n", np.hstack((a,b)))
print("Vertical Stack:\n", np.vstack((a,b)))
print("Concatenate:\n", np.concatenate((a,b), axis=0))