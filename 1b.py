import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 6.3, 100)  

a=9.81

x_t = 0.5 * a * t**2

plt.figure(figsize=(8, 4))
plt.plot(t, x_t, label='Pozicija x(t)')
plt.xlabel('Vreme')
plt.ylabel('Pozicija')
plt.show()
