

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
dt=0.1

T=[]
F1=[]
FC1=[]
FV1=[]
D1=[]

while t<10:
    A=A1*(1-0.25*(math.e**(-(t/0.67)**2)))
    D=0.5*rho*CD*A*(v-w)**2
    Fc=fc*(math.e**(-(t/0.67)**2))
    Fv=-25.58*v
    a=(F+Fc+Fv-D)/m
    v=v+a*dt
    t+=dt
    T.append(t)
    F1.append(F)
    FC1.append(Fc)
    FV1.append(Fv)
    D1.append(D)




plt.plot(T,F1)
plt.xlabel('Vreme (s)')
plt.ylabel('Konstantna sila(F)')
plt.title('Sile')
plt.grid(True)
plt.show()

plt.plot(T,FC1)
plt.xlabel('Vreme (s)')
plt.ylabel('Pocetna pokretacka sila')
plt.title('Sile')
plt.grid(True)
plt.show()

plt.plot(T,FV1)
plt.xlabel('Vreme (s)')
plt.ylabel('Sila koja opada sa povecanjem mbrzine')
plt.title('Sile')
plt.grid(True)
plt.show()

plt.plot(T,D1)
plt.xlabel('Vreme (s)')
plt.ylabel('Sila otopra vazduha')
plt.title('Sile')
plt.grid(True)
plt.show()


