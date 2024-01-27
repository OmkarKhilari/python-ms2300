import matplotlib.pyplot as plt
import numpy as np

def simulate_dice_rolls(num_rolls):
    rolls = np.random.randint(1, 7, size=num_rolls)
    return rolls

def calculate_joint_probability(rolls):
    joint_prob = np.zeros((num_rolls - 1, 6, 6))
    for t in range(1, num_rolls):
        for i in range(1, 7):
            for j in range(1, 7):
                count = np.sum((rolls[:t] == i) & (rolls[1:t+1] == j))
                joint_prob[t-1, i-1, j-1] = count / t
    return joint_prob

def plot_joint_probability(num_rolls, joint_prob):
    plt.figure(figsize=(10, 8))
    for i in range(1, 7):
        for j in range(1, 7):
            plt.plot(range(1, num_rolls), joint_prob[:, i-1, j-1], label=f'({i},{j})', marker='o')

    plt.xlabel('Number of Rolls')
    plt.ylabel('Joint Probability')
    plt.title('Joint Probability P(X, Y) as a function of Number of Rolls')
    plt.legend()
    plt.grid(True)
    plt.show()

# Set the number of dice rolls
num_rolls = 1000

# Simulate dice rolls
rolls = simulate_dice_rolls(num_rolls)

# Calculate joint probability
joint_prob = calculate_joint_probability(rolls)

# Plot joint probability
plot_joint_probability(num_rolls, joint_prob)
