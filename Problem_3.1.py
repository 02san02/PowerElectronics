import numpy as np
import matplotlib.pyplot as plt

# RC filter frequency response
def H(f):
	s = 1j*2*np.pi*f
	den = np.polyval([1,1],s*C*R)
	H = 1/den
	return H

# List of filter Characteristics
Rl = [3*1e2, 5*1e2,7*1e2]
Cl = [5e-6, 10e-6, 15e-6]
colour = ["b", "g", "r"] # Colour shade of graphs

# Plotting the filter amplitude response
f_0 = 50.0
f = np.linspace(-3*f_0,3*f_0,1e2)
for i in range(3):
	R = Rl[i]
	C = Cl[i]
	plt.plot(f, abs(H(f)), colour[i], label="{} ohm, {} faraday".format(Rl[i], Cl[i]))
	plt.legend()	
plt.grid() # minor
plt.xlabel('$f$ (Hz)')
plt.ylabel('$H(f)$')
plt.show()
