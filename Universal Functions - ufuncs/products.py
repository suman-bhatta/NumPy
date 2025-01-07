"Products"

import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)


# Example: Find the product of the elements of two arrays:

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)


"Product Over an Axis"

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)


"Cummulative Product"

import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)