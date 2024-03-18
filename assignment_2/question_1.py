import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    return (3*x - 1.4) * np.sin(18*x)

x = np.linspace(0, 1.22, 400)

y = f(x)

def find_minima(interval, f):
    results = []
    for start in np.linspace(interval[0], interval[1], 100):
        res = minimize(f, start, bounds=[interval])

        if not any(abs(res.fun - r.fun) < 1e-5 for r in results):
            results.append(res)
    return results

minima_results = find_minima((0, 1.22), f)

print("Minimas found:")
for result in minima_results:
    print(f"x = {result.x[0]:.5f}, f(x) = {result.fun:.5f}")

global_min = min(minima_results, key=lambda x: x.fun)

print(f"Global minimum at x = {global_min.x[0]:.5f}, f(x) = {global_min.fun:.5f}")

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = (3x - 1.4)sin(18x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x)')
plt.legend()
plt.grid(True)
plt.show()
