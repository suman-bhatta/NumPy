"""
Zipf Distribution
Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
"""

from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)



"""
Visualization of Zipf Distribution
Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()