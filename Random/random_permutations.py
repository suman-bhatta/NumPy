"""
Random Permutations of Elements
Example: Shuffle the array:
"""

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)



"""
Generating Permutation of Arrays
Example: Generate a random permutation of elements of the array:
"""

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))


