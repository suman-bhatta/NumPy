""""
Joining NumPy Arrays
Exmple: Join two arrays:
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)



"""
Joining Arrays Using Stack Functions
Example: Stack two arrays:
"""

import numpy as np 

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


"""
Stacking Along Rows
Exmple: Stack two arrays along rows:
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)



"""
Stacking Along Columns
Example: Stack two arrays along columns:
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)



"""
Stacking Along Height (depth)
Example: Stack two arrays along height (depth):
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)