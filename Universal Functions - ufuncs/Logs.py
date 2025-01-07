"Log at Base 2"

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))


"Log at Base 10"

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))


"Natural Log, or Log at Base e"

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))


"Log at Any Base"

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))