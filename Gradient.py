import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 6, 10, 13, 11])

# Initial parameters
b0 = 3.0
b1 = 2.0
alpha = 0.1
n_iter = 5
n = len(x)

# Store parameters per iteration (including iteration 0)
params = [(b0, b1)]

def compute_gradients(b0, b1, x, y):
    y_hat = b0 + b1 * x
    e = y_hat - y
    sum_e = np.sum(e)
    sum_ex = np.sum(e * x)
    return sum_e, sum_ex

# Run gradient descent
for _ in range(n_iter):
    sum_e, sum_ex = compute_gradients(b0, b1, x, y)

    # Mean updates
    b0 = b0 - alpha * (sum_e / n)
    b1 = b1 - alpha * (sum_ex / n)

    params.append((b0, b1))

# Plot data points
plt.scatter(x, y, color='orange', marker='x', s=80)

# Color list (enough for many iterations)
colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']

# Draw regression line for each iteration
x_line = np.linspace(1, 5, 200)

for i, (b0, b1) in enumerate(params):
    y_line = b0 + b1 * x_line
    plt.plot(x_line, y_line, color=colors[i % len(colors)],
             label=f"Iter {i}")

# Labels & title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Descent Line Updates per Iteration")
plt.legend()
plt.grid(True)

plt.show()