import numpy as np

arr = np.array([1,2,3,4,5])

# Save to file
np.save("my_array.npy", arr)

# Load back
loaded = np.load("my_array.npy")
print("Loaded Array:", loaded)