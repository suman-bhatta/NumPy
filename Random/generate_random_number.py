"""
Generate Random Number
Exmple: Generate a random intiger from 0 to 100
"""

from numpy import random

x = random.randint(100)

print(x)


# Exmple: Generate a random float from 0 to 1:

from numpy import random

x = random.rand()

print(x)


# Exmple: Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(5))

print(x)


# Exmple: Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(3, 5))

print(x)


"""
Floats
Exmples: Generate a 1-D array containing 5 random floats:
"""

from numpy import random

x = random.rand(5)

print(x)


# Exmple: Generate a 2-D array with 3 rows, each row containing 5 random numbers:

from numpy import random

x = random.rand(3, 5)

print(x)



"""
Generate Random Number From Array
Exmple: Return one of the values in an array:
"""

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


# Exmple: Generate a 2-D array that consits of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)