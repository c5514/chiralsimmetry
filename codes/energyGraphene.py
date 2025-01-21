import matplotlib.pyplot as plt
import numpy as np


def energy(k1, k2, a1, a2, b1, b2):
    return np.sqrt(
        3
        + 2 * np.cos(k1 * a1 + k2 * a2)
        + 2 * np.cos(k1 * b1 + k2 * b2)
        + 2 * np.cos(k1 * (a1 - b1) + k2 * (a2 - b2))
    )


def energy2(k1, k2, a1, a2, b1, b2):
    return -np.sqrt(
        3
        + 2 * np.cos(k1 * a1 + k2 * a2)
        + 2 * np.cos(k1 * b1 + k2 * b2)
        + 2 * np.cos(k1 * (a1 - b1) + k2 * (a2 - b2))
    )


a1 = np.sqrt(3) / 2
a2 = 3 / 2
b1 = -np.sqrt(3) / 2
b2 = 3 / 2

# k1 = np.linspace(-2 * np.sqrt(3), 2 * np.sqrt(3), 100)
k1 = np.linspace(-3, 3, 1000)
# k2 = np.linspace(-2 * np.sqrt(3), 2 * np.sqrt(3), 100)
k2 = np.linspace(-3, 3, 1000)
K1, K2 = np.meshgrid(k1, k2)

# Calculate the energy values
Z1 = energy(K1, K2, a1, a2, b1, b2)
Z2 = energy2(K1, K2, a1, a2, b1, b2)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(K1, K2, Z1, cmap="viridis", edgecolor="none")
ax.plot_surface(K1, K2, Z2, cmap="inferno", edgecolor="none")

# Add labels and title
ax.set_xlabel(r"$k_x$")
ax.set_ylabel(r"$k_y$")
ax.set_zlabel("E")
# Set viewing angle
ax.view_init(elev=15, azim=15)
# Show the plot
plt.savefig("../figures/energyGraphene.pdf", bbox_inches="tight")
plt.show()
