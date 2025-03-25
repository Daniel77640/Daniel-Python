import matplotlib.pyplot as plt
# initializing the data
x = [10, 20, 30, 40]
y = [20, 30, 40, 50]
# plotting the data
plt.plot (x, y)
# Adding the title
plt.title ("Simple plot")
#Adding the labels
plt.ylabel ("y-axis")
plt.xlabel ("x-axis")
plt.show ()


import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 1]
plt.plot (x, y)
plt.xlabel ("x - axis")
plt.ylabel ("y - axis")
plt.show ()

import matplotlib.pyplot as plt
x = [240.85, 249.42, 307.5]
y = [249.42, 240.85, 307.5]
plt.plot (x, y)
plt.xlabel ("mensalidade")
plt.ylabel ("valores")
plt.show ()

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis ([0, 6, 0, 20])
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
y, x = np.mgrid [slice (-4, 4 + dy, dy),
                        slice(-4, 4 + dx, dx)]
z = (1 - x / 3. + x ** 5 + y ** 5) * np.exp(-x ** 2 - y * 2)
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()
c = plt.imshow(z, cmap ='Greens', vmin = z_min, vmax = z_max,
                        extent = [x.min(), x.max(), y.min(), y.max()],
                            interpolation='nearest', origin ='lower')
plt.colorbar(c)
plt.title('matplotlib.pyplot.imshow() funcion Example',
                                                    fontweight ="bold")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(Z1, cmap ="binary_r", interpolation ='nearest',
 extent = extent, alpha = 1)

def geeks(x, y):
 return (1 - x / 2 + x**5 + y**6) * np.exp(-(x**2 + y**2))

Z2 = geeks(X, Y)

plt.imshow(Z2, cmap ="Greens", alpha = 0.7,
           interpolation ='bilinear', extent = extent)

plt.title('matplotlib.pyplot.imshow() function Example',
 fontweight ="bold")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
y1 = [2, 3, 4.5]
y2 = [1, 1.5, 5]
plt.plot(y1)
plt.plot(y2)
plt.legend(["blue", "green"], loc ="lower right")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), '--b', label ='Sine')
ax.plot(x, np.cos(x), c ='r', label ='Cosine')
ax.axis('equal')

leg = ax.legend(loc ="lower left")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

val, res = 100, 15
x = np.sin(val + res * np.random.randn(10000)) - np.cos(val + res *
np.random.randn(10000))

n, bins, patches = plt.hist(x, 200,density = True, facecolor ='g',
 alpha = 0.5)

plt.grid(True)

plt.title('matplotlib.pyplot.grid() function \
Example\n\n', fontweight ="bold")

plt.show()

# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))
# Creating first axes for the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# Creating second axes for the figure
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])
# Adding the data to be plotted
ax1.plot([5, 4, 3, 2, 1], [2, 3, 4, 5, 6])
ax2.plot([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
plt.show()


import pylab as plt
import numpy as np

X = np.linspace(0, 3, 200)
Y1 = X**2 + 3
Y2 = np.sin(X)
Y3 = np.cos(X)

plt.plot(X, Y1, lw=4)
plt.plot(X, Y2, lw=4)
plt.plot(X, Y3, lw=4)

plt.fill_between(X, Y1, Y2, color='k', alpha=.5)
plt.fill_between(X, Y1, Y3, color='y', alpha=.5)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = ['A', 'B', 'C', 'D']
y1 = np.array([10, 20, 10, 30])
y2 = np.array([20, 25, 15, 25])
y3 = np.array([12, 15, 19, 6])
y4 = np.array([10, 29, 13, 19])
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')
plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Round 1", "Round 2", "Round 3", "Round 4"])
plt.title("Scores by Teams in 4 Rounds")
plt.show() 