import numpy as np
import matplotlib.pyplot as plt
# Importing the required libraries

x = np.arange(-50, 50, 0.001) # Here, t is in micro-second(ms)
y = np.cos(x)

plt.plot(x, y)
plt.grid()
plt.xlabel('$t$ (ms)')
plt.ylabel('$x(t)$')
plt.show()
