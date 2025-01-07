"""
The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""

import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a Function is a ufunc
print(type(myadd))



# Example: Check the type of another function: concatenate().

import numpy as np

print(type(np.concatenate))


# Example : Check the type of something that does not exist. This will produce an error.

import numpy as np

print(type(np.blahblah))


# Example : Use an if statement to check if the function is a ufunc or not.

import numpy as np

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')