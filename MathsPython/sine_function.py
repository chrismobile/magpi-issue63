import matplotlib.pyplot as plt 
import numpy as np

def f(x):
    return np.sin(x)/x

x = np.arange(-15.0, 15.0, 0.1)

plt.plot(x, f(x))
plt.show()
