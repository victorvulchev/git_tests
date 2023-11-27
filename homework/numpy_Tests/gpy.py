import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a 2x2 grid for the subplots with specific width ratios
fig, axes = plt.subplots(2, 2, gridspec_kw={'width_ratios': [1, 1]})

# Create the top-left subplot
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('Plot 1')

# Create the top-right subplot
axes[0, 1].plot(x, y2)
axes[0, 1].set_title('Plot 2')

# Create the bottom subplot that spans both columns
axes[1, 0].plot(x, y1 + y2)
axes[1, 0].set_title('Combined Plot')

# Remove the empty top-right subplot
fig.delaxes(axes[1, 1])

# Adjust spacing between subplots
plt.tight_layout()

plt.show()