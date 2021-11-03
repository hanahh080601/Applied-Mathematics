from __future__ import division, print_function, unicode_literals
import numpy as np 

def grad(x):
    return 2 * (np.exp(-x) - 2 / np.exp(x)) * (-np.exp(-x) + 2 / np.exp(x))

def cost(x):
    return (np.exp(-x) - 2 / np.exp(x)) ** 2

def myGD(alpha, x0):
    x = [x0]
    for it in range(50000):
        x_new = x[-1] - alpha * grad(x[-1])
        if abs(grad(x_new)) < 1e-4:
            break
        x.append(x_new)
    return (x[-1], it)

x,_ = myGD(0.1, 3)
print(myGD(0.1, 3))
print(cost(x))