import numpy as np
from scipy.integrate import quad
# Importing libraries which are needed

f = 100 # Frequency of signal
T = 1/f # Time period

def integrand(t): # Defining an integrand to integrate w.r.t. to t (time)
	return np.absolute(16*np.sin(100*np.pi*t)) # The function we need to integrate 

ans, err = quad(integrand, 0, T) # Saving the output of the integration in variables
ans = ans/T
print(ans)
# finally, printing it



