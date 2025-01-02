"""
Iterating Arrays
Exmple: Iterate on the elements of the following 1-D array:
"""

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)



  """"
  Iterating 2-D Arrays
  Example: Iterate on the elements of the following 2-D array:
  """

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)



  """
  Iterate on each scalar element of the 2-D array:
  """

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)



  """
  Iterate on each scalar element of the 3-D array:
  """


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


  """
  Iterating Arrays Using nditer()
  Example: Iterate through the following 3-D array:
  """

  import numpy as np

  arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

  for x in np.nditer(arr):
    print(x)


  """
  Iterating Array With Different Data Types
  Exmple: Iterate through the array as a string:
  """

  import numpy as np

  arr = np.array([1, 2, 3])

  for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)



"""
Iterating With Different Step Size
Example: Iterate through every scalar element of the 2D array skipping 1 element:
"""

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)



"""
Enumerated Iteration Using ndenumerate()
Example: Enumerate on following 1D arrays elements:
"""

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# Example: Enumerate on following 2D array's elements:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)