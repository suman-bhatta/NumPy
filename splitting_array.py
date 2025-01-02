"""
Splitting an array into two subarrays
Example: Split the array into three subarrays where each subarray has two elements:
"""

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)


# Exmple: Split the array in 4 parts

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


"""
Split Into Arrays
Exmple: Split the 2-D array into three 2-D arrays.
"""

# import numpy as np

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)



"""
Splitting 2-D Arrays
Example: Split the 2-D array into three 2-D arrays along rows.
"""

# import numpy as np 

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3) 

# print(newarr)


# Exmple: Split the 2-D array into three 2-D arrays along columns:

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3, axis=1)

# print(newarr)


# Exmple: Split the 2-D array into three 2-D arrays along columns:

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr =  np.array_split(arr, 3, axis=1)

# print(newarr)


# Exmple: Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)