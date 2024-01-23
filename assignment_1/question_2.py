# Question 1a

import random as rand
import matplotlib.pyplot as plt
import numpy as np

def generate_rolls(steps):
    rolls = []
    for i in range(steps):
        result_on_rolling = rand.randrange(1, 7, 1)
        rolls.append(result_on_rolling)
    return rolls


def probability_for_every_face(steps):
    count = [0, 0, 0, 0, 0, 0]
    probability_arr = []
    rolls = generate_rolls(steps)

    for i in rolls:
        count[i - 1] += 1
        probability_arr.append([j / sum(count) for j in count])

    return np.array(probability_arr)  # Convert to NumPy array

def plot_probabilities(steps):
    probabilities = probability_for_every_face(steps)

    for i in range(6):
        plt.plot(probabilities[:, i], label=f'Face {i + 1}')

    plt.legend()
    plt.show()

steps = 10000
probabilities = probability_for_every_face(steps)
convergence = np.argmax(np.abs(probabilities[:, -1] - 1/6) < 1e-3)

print(f"Convergence occurs at step: {convergence}")
plot_probabilities(steps)
