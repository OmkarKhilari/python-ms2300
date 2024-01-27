import numpy as np
import matplotlib.pyplot as plt

def fx(x):
    return 3*x + np.sin(x) - np.exp(x)

def dfx(x):
    return 3 + np.cos(x) - np.exp(x) 

#  Question 3a

x_values = np.linspace(-4, 4, 1000)
y_values = fx(x_values)

plt.plot(x_values, y_values, label = "3x + sin(x) + exp(x)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  #X-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  #Y-axis
plt.xlabel('x')
plt.ylabel('fx(x)')
plt.title('Plot of 3x + sin(x) + exp(x)')
plt.legend()
plt.show()

# Question 3b
#Bisection Method

def bisection_method(f, a, b, tol, count):
    # check if the root is available between a and b or not
    if np.sign(f(a)) == np.sign(f(b)): #f(a)*f(b) > 0
        return None, None
        
    mid = (a+b)/2
    if np.abs(f(mid)) < tol:
        return mid, count
    elif np.sign(f(mid)) == np.sign(f(a)): #or we can do f(mid)*f(a) > 0
        #if sign of f(mid) and f(a) is same that means the root lies b/w mid and b
        #so we will call this function itself (recursion) with mid instead of a
        return bisection_method(f, mid, b, tol, count+1)
    elif np.sign(f(mid)) == np.sign(f(b)): #f(mid)*f(b) > 0
        #for this case we'll change the value of b instead of a with mid
        return bisection_method(f, a, mid, tol, count+1)
    
#Newton Raphson Method (Recursive)
def newton_raphson(f, df, x1, tol, count):
    #recursion elimination condition
    if count>500:
        return None, None   
    x2 = x1 - f(x1)/df(x1)
    if abs(f(x2)) < tol :
        return x2, count
    else:
        return newton_raphson(f, df, x2, tol, count + 1)

#determine roots using Bisection Method

#from the avobe plotting we can guess the roots
#and also given x0 = 0 and x1 =1
#so lets take a =0 and b =1

a, b = 0, 1
root, count = bisection_method(fx, a, b, tol, 1)
print(f"First Root: {root}, and Iteration count = {count}")

#for another root we can take a = 1.5 and b = 2.5
a, b = 1.5, 2.5
root, count = bisection_method(fx, a, b, tol, 1)
print(f"Second Root: {root}, and Iteration count = {count}")

#determine roots using Newton-Raphson Method

#given x0 =0

root, count = newton_raphson(fx, dfx, 0, tol, 1)

if root is not None:
    print(f"Root by using x0 =0 : {root}, and Iteration count = {count}")
else:
    print("Root not found")