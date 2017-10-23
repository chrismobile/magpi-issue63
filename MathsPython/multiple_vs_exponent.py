import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(-10.0, 10.0, 1.0)

plt.plot(x, x*2, 'r^')
plt.plot(x, x**2, 'bo')

plt.legend()
plt.show()
