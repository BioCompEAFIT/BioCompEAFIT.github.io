import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('Aminoacidos')
plt.ylabel('Ocurrencias')
plt.title('Ocurrencias Vs Aminoacidos')
plt.grid(True)
#plt.savefig("test.png")
plt.show()
