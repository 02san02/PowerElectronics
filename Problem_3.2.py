import numpy as np
import matplotlib.pyplot as plt
# Importing the required libraries

x = np.arange(-50*10**-3, 50*10**-3, 1e-6) # Here, t is in second(s)
y = np.cos(100*np.pi*x)

plt.plot(x, y)
plt.grid()
plt.xlabel('$t$ (s)')
plt.ylabel('$x(t)$')
plt.show()
