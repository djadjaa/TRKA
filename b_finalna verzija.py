import numpy as np
import matplotlib.pyplot as plt


F_v = 400  
m = 80  


def pozicija(t):
    a = F_v / m  
    return 1/2 * a * t**2 


t_tacke = np.linspace(0, 10, 100)  
x = pozicija(t_tacke)


plt.plot(t_tacke, x)
plt.xlabel('Vreme (s)')
plt.ylabel('Pozicija (m)')
plt.title('Položaj sprintera kao funkcija vremena')
plt.show()