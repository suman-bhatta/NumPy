"""
Normal (Gaussian) Distribution
Example: Generate a random normal distribution of size 2x3:
"""

from numpy import random

x = random.normal(size=(2, 3))

print(x)



# Example: Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)



"""
Visualization of Normal Distribution
Example:
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()