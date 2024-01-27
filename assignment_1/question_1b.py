import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(r, total_points):
    random_x = np.random.uniform(0, r, total_points)
    random_y = np.random.uniform(0, r, total_points)
    
    points = list(zip(random_x, random_y))
    
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

def error(r,points):
    return 100 * (np.abs(original_area(r) - find_area(r,points))/original_area(r)) 


r = 50
points = 100000
print(original_area(r))
print(find_area(r,points))
print(error(r, points))


