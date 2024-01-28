import numpy as np
import matplotlib.pyplot as plt

def generate_points(a):
    x_coordinates = []
    y_coordinates = []

    for i in range(-a//2, a//2):  
        for j in range(-a//2, a//2):
            x = i + 0.5
            y = j + 0.5
            x_coordinates.append(x)
            y_coordinates.append(y)

    points = list(zip(x_coordinates, y_coordinates))

    return points

def find_area(r):
    points = generate_points(2 * r)
    
    inside_circle = 0
    outside_circle = 0
    on_circumference = 0
    total_points = len(points)

    for x, y in points:
        distance = np.sqrt(x**2 + y**2)
        if distance < r - 1e-3:
            inside_circle += 1
        elif distance > r - 1e-3:
            outside_circle += 1
        else:
            on_circumference += 1

    area = 4 * ((inside_circle + 0.5 * on_circumference) / total_points) * (r**2)

    return area

def plot_diagram(r):

    fig, ax = plt.subplots()
    ax.set_aspect('equal') 
    
    for i in range(-r, r):  
        plt.axhline(i + 0.5, color='gray', linestyle='--', linewidth=0.5) 
        plt.axvline(i + 0.5, color='gray', linestyle='--', linewidth=0.5) 

    circle = plt.Circle((0, 0), r, color='r', fill=False, linewidth=2) 
    ax.add_patch(circle)

    plt.show()

def original_area(r):
    return np.pi * r**2

def error(r):
    return 100 * (np.abs(original_area(r) - find_area(r)) / original_area(r)) 



r = 10
print("Original area:", original_area(r))
print("Calculated area:", find_area(r))
print("Error:", error(r))
plot_diagram(r)
