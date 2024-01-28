# Question 2a

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

    return np.array(probability_arr)  

def plot_probabilities(steps):
    probabilities = probability_for_every_face(steps)

    for i in range(6):
        plt.plot(probabilities[:, i], label=f'Face {i + 1}')

    plt.title('Probability Plot')
    plt.xlabel('Steps')
    plt.ylabel('P(x)')
    plt.legend()
    plt.show()

# def see_convergence(tol=1e-3):
#     min_average_difference = np.inf    
#     convergence = 0

#     for i in range(len(probabilities)):
#         average_difference = np.mean(np.abs(1/6 - probabilities[i, :]))

#         if average_difference < min_average_difference:
#             min_average_difference = average_difference
#             convergence = i

#         if average_difference < tol:
#             break

#     return convergence

def see_convergence(tol = 1e-3):
    min_difference = np.inf    
    convergence = 0

    for i in range(len(probabilities)):
        difference = np.mean(np.abs(1/6 - probabilities[i, :]))

        if difference < min_difference:
            min_difference = difference
            convergence = i + 1

        if difference < tol:
            break    

    return convergence



steps = 10000
probabilities = probability_for_every_face(steps)

# print(probabilities)
convergence = see_convergence()

print(f"Convergence occurs at step: {convergence}")
plot_probabilities(steps)
