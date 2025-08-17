import numpy as np

arr = np.arange(1, 13)      # 1 se 12 tak number
reshaped = arr.reshape(3, 4) # 3 row × 4 column

print("Original Array:", arr)
print("Reshaped Array:\n", reshaped)