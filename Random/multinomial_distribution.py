"""
Multinomial Distribution
Example: Draw out a sample for dice roll:
"""

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)