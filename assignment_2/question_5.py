import matplotlib.pyplot as plt
import numpy as np

def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

corner_points = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
origin = (0, 0)

n_points = 10000

x_values = np.random.uniform(-2, 2, n_points)
y_values = np.random.uniform(-2, 2, n_points)
random_points = np.column_stack((x_values, y_values))

points_closer_to_origin = [point for point in random_points if all(distance(point, origin) < distance(point, corner) for corner in corner_points)]

points_closer_to_origin_array = np.array(points_closer_to_origin)

plt.figure(figsize=(8, 8))
plt.plot(*zip(*corner_points), 'o', label='Corner Points')
plt.plot(origin[0], origin[1], 'r*', markersize=10, label='Origin')
plt.scatter(points_closer_to_origin_array[:, 0], points_closer_to_origin_array[:, 1], s=1, color='blue', label='Random Points Closer to Origin')
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.grid(True)
plt.legend()
plt.title('Locus of Random Uniform Points Closer to the Origin')
plt.xlabel('X')
plt.ylabel('Y')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
