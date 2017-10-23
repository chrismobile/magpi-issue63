import matplotlib.pyplot as plt 
import numpy as np

def f(x):
    return np.sin(x)/x

def g(x):
    return np.cos(x)

x = np.arange(-15.0, 15.0, 0.1)

plt.plot(x, f(x), 'r', label="sin(x)/x")
plt.plot(x, g(x), 'b', label="cos(x)")

plt.legend()
plt.show()
