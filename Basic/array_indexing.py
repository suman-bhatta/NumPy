"""
Access Array Elements
Example: Get the first element from the following array:
"""

# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[0])

# Example: Get the second element from the following array.

# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[1])

# Example: Get third and fourth elements from the following array and add them.

# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[2] + arr[3])


"""
Access 2-D Arrays
Example: Access the 2nd element on 1st dim:
"""

# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st dim: ', arr[0, 1])

# Example: Access the 5th element on 2nd dim:

# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('5th element on 2nd dim: ', arr[1, 4])



"""
Access 3-D Arrays
Example: Access the third element of the second array of the first array:
"""

# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])


"""
Negative Indexing
Use negative indexing to access an array from the end.
Example: Print the last element from the 2nd dim:
"""

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])