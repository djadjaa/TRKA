

import numpy as np
import matplotlib.pyplot as plt

rho = 1.293 
A = 0.45  
CD = 1.2  
w=0
m = 80  
F_v = 400  
v=0
t=0
x=0
dt=0.1
X=[]
T=[]
V=[]
A1=[]
while t<10:
    D=0.5*rho*CD*A*(v-w)**2
    a=(F_v-D)/m
    x=x+v*dt
    v=v+a*dt
    t+=dt
    X.append(x)
    T.append(t)
    V.append(v)
    A1.append(a)


plt.plot(T,X)
plt.xlabel('Vreme (s)')
plt.ylabel('Pozicija (m)')
plt.title('Funkcija pozicije od vremena')
plt.grid(True)
plt.show()

plt.plot(T,V)
plt.xlabel('Vreme (s)')
plt.ylabel('Brzina (m/s)')
plt.title('Funkcija brzine od vremena')
plt.grid(True)
plt.show()


plt.plot(T,A1)
plt.xlabel('Vreme (s)')
plt.ylabel('Ubrzanje (m/s)^2')
plt.title('Funkcija ubrzanja od vremena')
plt.grid(True)
plt.show()
