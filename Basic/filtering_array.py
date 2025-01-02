"""
Filtering Arrays
Example: Get the indexes where the values are even:
"""

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# x = [True, False, True, False, True, False, True, False]

# newarr = arr[x]

# print(newarr)


"""
Creating the Filter Array
Exmple: Create a filter array that will return only values higher than 42:
"""

# import numpy as np

# arr = np.array([41, 42, 43, 44]) 


# # create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#     # if the element is higher than 42, set the value to True, otherwise False:
#     if element > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)


# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)



# Exmple: Create a filter array that will return only even elements from the original array:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#     # if the element is completely divisble by 2, set the value to True, otherwise False:
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)


# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)



"""
Creating Filter Directly From Array
Example: Create a filter array that will return only values higher than 42:
"""

# import numpy as np

# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


# Example: Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)