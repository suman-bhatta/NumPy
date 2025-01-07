"Summations"

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)


# Example: Sum the values in arr1 and the values in arr2:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)


"Summation Over an Axis"

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)


"Cummulative Sum"

import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)