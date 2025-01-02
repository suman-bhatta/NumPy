"""
Data Types in NumPy
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
# Checking the Data Type of an Array

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Example: Create an array with data type string:

import numpy as np
arr = np.array(['python', 'java', 'javascript'])
print(arr.dtype)


"""
Creating Arrays With a Defined Data Type
Example: Create an array with data type string:
"""

import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


# Example: Create an array with data type 4 bytes integer:

import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# What if a Value Can Not Be Converted?
# Example: A non integer string like 'python' can not be converted to integer (will raise an error):

import numpy as np
arr = np.array(['python', 'java', 'javascript'], dtype='i')


"""
Converting Data Type on Existing Arrays
Example: Change data type from float to integer by using 'i' as parameter value:
"""

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr.dtype)

# Example: Change data type from integer to boolean:

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# Example: Change data type from float to integer by using int as parameter value:

import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)