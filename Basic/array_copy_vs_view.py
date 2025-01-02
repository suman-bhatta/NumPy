"""
NumPy Array Copy vs View
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
"""

# COPY:
#Example: Make a copy, change the original array, and display both arrays:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)


# VIEW:
# Example: Make a view, change the original array, and display both arrays:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)


# Make Changes in the VIEW:
# Example: Make a view, change the view, and display both arrays:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31

# print(arr)
# print(x)


# Check if Array Owns it's Data
# Example: Print the value of the base attribute to check if an array owns it's data or not:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)