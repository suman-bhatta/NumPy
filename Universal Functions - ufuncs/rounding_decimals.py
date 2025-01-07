""""
There are primarily five ways of rounding off decimals in NumPy:
- truncation
= fix
- rounding
- floor
- ceil
"""

"Truncation"

import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)


"Fix"

import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)


"Rounding"

import numpy as np  

arr = np.around(3.1666, 2)

print(arr)


"Floor"

import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)


"Ceil"

import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)