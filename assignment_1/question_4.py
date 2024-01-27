import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3-x
    
def df(x):
    return 3*x**2-1

def newton_raphson(f, df, x1, tol):
    if count>500:
        return None, None   
    x2 = x1 - f(x1)/df(x1)
    if abs(f(x2)) < tol :
        return x2
    else:
        return newton_raphson(f, df, x2, tol)

x_range = np.linspace(-1.5, 1.5, 100) #We are taking 100 points (values) b/w [-1.5,1.5]
tol = 1e-6

result = {} #We will store the result here ,as x : root

for x0 in x_range:
    root = newton_raphson(f, df, x0, tol)
    if root is not None:
        result[x0] = root

print(result)        