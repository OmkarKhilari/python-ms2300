def f(x):
    return x**2 - x - 2

def df(x):
    return 2*x - 1

def minima_func(x0, alpha=0.5, tol=1e-3):
    # x1 = x0 - alpha*df(x0)
    iter_no = 0
    for i in range(500):
        x1 = x0 - alpha*df(x0)
        iter_no += 1
        if abs(df(x1) - 0) <= tol:
            return x1, iter_no

        x0 = x1

    return None, iter_no    

result = minima_func(5)
minima = result[0]
iterations = result[1]
if minima != None:
    print("Minima:", minima)
    print("No. of Iterations:", iterations)
else:
    print("Minima not found")
