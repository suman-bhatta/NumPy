"""
Searchingh Array
Exmple: Find the indexes where the value is 4:
"""

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)


# Example: Find the indexes where the values are even:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# x = np.where(arr%2 == 0)

# print(x)


# Example: Find the indexes where the values are odd:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# x = np.where(arr%2 == 1)

# print(x)


"""
Search Sorted
Example: Find the indexes where the value 7 should be inserted:
"""


# import numpy as np

# arr = np.array([6, 7, 8, 9, 8, 7, 6])

# x = np.searchsorted(arr, 8)

# print(x)


"""
Search From the Right Side
Example: Find the indexes where the value 7 should be inserted, starting from the right:
"""


# import numpy as np

# arr = np.array([6, 7, 8, 9, 8, 7, 6])

# x = np.searchsorted(arr, 7, side='right')

# print(x)



"""
Multiple Values
Example: Find the indexes where the values 2, 4, and 6 should be inserted:
"""

import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)