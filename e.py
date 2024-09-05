

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
while t<10:
    D=0.5*rho*CD*A*(v-w)**2
    a=(F_v-D)/m
    x=x+v*dt
    v=v+a*dt
    t+=dt
    X.append(x)
    T.append(t)
    V.append(v)


plt.plot(T,X)
plt.xlabel('Vreme (s)')
plt.ylabel('Pozicija (m)')
plt.title(12345)
plt.grid(True)
plt.show()

plt.plot(T,V)
plt.xlabel('Vreme (s)')
plt.ylabel('Brzina (m/s)')
plt.title(12345)
plt.grid(True)
plt.show()

