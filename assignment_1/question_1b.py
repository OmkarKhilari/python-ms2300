import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(r, total_points):
    x = np.random.uniform(-r, r, total_points)
    y = np.random.uniform(-r, r, total_points)
    
    points = list(zip(x, y)) # Using tuple to store coordinates
    
    return points

def find_area(r, total_points):
    points = generate_random_points(r, total_points)
    
    inside_circle = 0
    outside_circle = 0
    
    for x, y in points:
        distance = np.sqrt(x**2 + y**2)
        if distance <= r:
            inside_circle += 1
        else:
            outside_circle += 1
    
    area = (inside_circle / total_points) * (r**2) * 4
    
    return area

def original_area(r):
    return np.pi * r**2

def error(r, points):
    return 100 * (np.abs(original_area(r) - find_area(r, points)) / original_area(r)) 

def plot_diagram(r, points):
    circle = plt.Circle((0, 0), r, color='r', fill=False, linestyle='solid',linewidth=2)
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal') 
    ax.add_patch(circle)
    
    x, y = zip(*generate_random_points(r, points)) # Unpacking tuple made in generate points

    plt.scatter(x, y, color='b', marker='.')

    plt.show()

r = 39
points = 1000
print("Original area:", original_area(r))
print("Calculated area:", find_area(r, points))
print("Error:", error(r, points))

plot_diagram(r, points)
