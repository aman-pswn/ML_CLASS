import numpy as np
import matplotlib.pyplot as plt

# Loss surface: L = w1^2 + w2^2
w1 = np.linspace(-5, 5, 50)
w2 = np.linspace(-5, 5, 50)
W1, W2 = np.meshgrid(w1, w2)

L = W1*2 + W2*2   # simple convex surface

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W1, W2, L)

ax.set_xlabel("w1")
ax.set_ylabel("w2")
ax.set_zlabel("Loss")

plt.show()