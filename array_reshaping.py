"""
Reshape From 1-D to 2-D
Example: Reshape from 1-D to 2-D:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 4)

print(newarr)


"""
Reshape From 1-D to 3-D
Exmple: Reshape from 1-D to 3-D:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


"""
Can We Reshape Into any Shape?
Example: Try converting 1-D array with 8 elements to a 2-D array with 3 elements in each dimension (will raise an error):
"""

import numpy as np  

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)



"""
Returns Copy or View?
Example: Check if the returned array is a copy or a view:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)



"""
Unknown Dimension
Example: Convert 1D array with 8 elements to 3D array with 2x2 elements:
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)



# Flattening the arrays
# Example: Convert the array into a 1D array:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)