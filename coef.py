import numpy as np
from scipy.integrate import quad

f = 100
T = 1/f

def integrand(t):
	return np.absolute(16*np.sin(100*np.pi*t))

ans, err = quad(integrand, 0, T)
ans = ans/T
print(ans)



