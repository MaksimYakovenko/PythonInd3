#л
import numpy as np
import matplotlib.pyplot as plt
from math import *
from matplotlib import animation

def fun(x):
    '''Повертає значення функції f для всіх точок з x
    '''
    try:
        y = 1 / (1 + x ** 2)
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.zeros(n)
        for i in range(n):
            y[i] = 1 / (1 + x[i] ** 2)
    return y

def aproxF(x, k):
    s = np.zeros(x.size)
    a = 1
    for i in range(2, k, 2):
        s += a
        a *= - x * x
    return s


fig = plt.figure()
ax = plt.axes(xlim=(-0.99999, 1), ylim=(0, 3))
line, = ax.plot([], [], lw=1)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(-1, 1, 100)
    y = aproxF(x, i)

    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=25, interval=2000, blit=True)

xx = np.linspace(-0.99999999, 1, 100)
s = fun(xx)
plt.plot(xx, s, 'r')

plt.show()
