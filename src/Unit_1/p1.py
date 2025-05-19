import numpy as np
import matplotlib.pyplot as plt 

t = np.linspace(0,1,500)
x = np.cos(2*np.pi*t)

plt.figure()

plt.plot(t, x, '-r')
plt.grid()
plt.title('example_signal_cos')

plt.show()
