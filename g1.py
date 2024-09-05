import numpy as np
import matplotlib.pyplot as plt
import math

rho = 1.293 
A = 0.45  
CD = 1.2  
F_v = 400 
VT=math.sqrt(2*(F_v)/(rho*CD*A))
print("Teorijska maksimalna brzina trkaca je:",VT) 
