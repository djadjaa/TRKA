import numpy as np


rho = 1.293 
A = 0.45  
CD = 1.2  
m = 80  
F_v = 400  
x_krajnje = 100  
w = 0  
t_cilj = 6.3  


dt = 0.01  
t = 0
x = 0
v = 0

while x < x_krajnje:
  
    D = 0.5 * rho * CD * A * (v - w)**2
    
    a = (F_v - D) / m
  
    v += a * dt
    x += v * dt
    t += dt


print("Vreme dolaska na cilj:", round(t, 1), "s")


#d) Nađi izraz za ubrzanje trkača.
#Koristimo drugi njutnov zakon  Fv= m*a pritom na njega utice
# sila otopra vazduha i zato je formula : Fv=m*a -> a=FV-D/m
