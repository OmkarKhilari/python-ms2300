# xn = xn-1 – f(xn-1)/f'(xn-1)
# used to find the solution to non-linear polynomial equations


def func(x):
    return x**3 - x**2 - 1

def func_dash(x):
    return 3*(x**2) - 2*x

def solver(x1, tol):
    for i in range(500):
        x2 = x1 - func(x1)/func_dash(x1)
        if abs(func(x2)) < tol:
            print('found root')
            return x2
        x1 = x2
    print('root not found')

tol = 1e-6
# solver(input("Enter x1: "), tol)
x1 = 6
res = solver(x1, tol)
print(res)

    


    