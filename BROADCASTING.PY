import numpy as np

arr = np.array([1,2,3])
print("Array + 10:", arr + 10)

matrix = np.array([[1],[2],[3]])
print("Broadcasting:\n", matrix + arr)