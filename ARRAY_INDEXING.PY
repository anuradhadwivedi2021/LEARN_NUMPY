import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Element [1,2]:", matrix[1,2])
print("Row 2:", matrix[1,:])
print("Column 3:", matrix[:,2])