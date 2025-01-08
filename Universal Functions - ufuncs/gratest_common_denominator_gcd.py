"Finding GCD (Greatest Common Denominator)"

import numpy as np

num1 = 60
num2 = 90

x = np.gcd(num1, num2)

print(x)


"Finding GCD in Arrays"

import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)