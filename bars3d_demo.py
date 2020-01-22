"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
height = [23, 4, 10, 9, 10]
for c, z in zip(['orange', 'r', 'g', 'b', 'y'], [4, 3, 2, 1, 0]):
    xs = np.arange(5) 
    ys = np.asarray(height)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(ys)
   # cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('Weeks')
ax.set_ylabel('Values')
ax.set_zlabel('Counts')
date = '10th-16th Jan'
plt.title('Engineer Values '+date+' 2020')
plt.show()
