import math 
import numpy as np  

#function
def f(x):
    return np.exp(x) - (3*x) - math.sin(x)
#input
a = float(input('Lower Boundary: '))
b = float(input('Upper Boundary: '))
e = float(input('Error Margin: '))
#computation
c = (a+b)/2
print(f(a))
print(f(c))
#decision
while abs(f(c))>e:
    v = f(a)*f(c)
    if v == 0:
        break
    elif v < 0:
        b = c
    else:
        a = c
    c = (a+b)/2
print(f"The root is approximately: {c}")
