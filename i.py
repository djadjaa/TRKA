

import numpy as np
import matplotlib.pyplot as plt
import math

rho = 1.293 
A1 = 0.45  
CD = 1.2  
w=0
m = 80  
F= 400 
fc=488
v=0
t=0
x=0
dt=0.1

X=[]
T=[]
V=[]
A_1=[]

while t<10:
    A=A1*(1-0.25*(math.e**(-(t/0.67)**2)))
    D=0.5*rho*CD*A*(v-w)**2
    Fc=fc*(math.e**(-(t/0.67)**2))
    Fv=-25.58*v
    a=(F+Fc+Fv-D)/m
    x=x+v*dt
    v=v+a*dt
    t+=dt
    X.append(x)
    T.append(t)
    V.append(v)
    A_1.append(a)


plt.plot(T,X)
plt.xlabel('Vreme (s)')
plt.ylabel('Predjen put(m)')
plt.title('Funkcija predjenog puta od vremena')
plt.grid(True)
plt.show()

plt.plot(T,V)
plt.xlabel('Vreme (s)')
plt.ylabel('Brzina(m/s)')
plt.title('Funkcija brzine od vremena')
plt.grid(True)
plt.show()

plt.plot(T,A_1)
plt.xlabel('Vreme (s)')
plt.ylabel('Ubrzanje(m/s^2)')
plt.title('Funkcija ubrzanja od vremena')
plt.grid(True)
plt.show()


