"Find LCM (Lowest Common Multiple) of two integers"

import numpy as np 

num1 = 60
num2 =  48

x = np.lcm(num1, num2)

print(x)


"Finding LCM in Arrays"


import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)


"Finding LCM of all elements in an array"

import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)