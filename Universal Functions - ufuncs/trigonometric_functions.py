"Trigonometric Functions"

import numpy as np

x = np.sin(np.pi/2)

print(x)


"Find sine values for all of the values in arr:"

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)


"Convert Degrees Into Radians"

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)


"Radians to Degrees"

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


"Finding Angles"

x = np.arcsin(1.0)

print(x)


"Find the angle for all of the sine values in the array:"

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)


"Hypotenues"

base = 3
perpendicular = 4

x = np.hypot(base, perpendicular)

print(x)