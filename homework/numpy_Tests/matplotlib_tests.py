import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 16, 24, 36, 42]
y2 = [15, 77, 88, 99, 132]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.set_facecolor("lightgray")

 
ax1.plot(x, y, color='green', linestyle=':', marker='X', label='My Data')
ax2.plot(x, y2, color="red", linestyle="--", marker="X", label="The Data")
ax3.plot(x, y, label="First", color="purple")
ax3.plot(x, y2, label="Second", color="blue")


ax1.set_xlabel("X-Axis HERE")
ax1.set_ylabel("Y-Axis HERE")
ax1.set_title("THIS IS THE TITLE")
ax1.legend()
ax1.set_facecolor("yellow")

ax2.set_xlabel("X-Axis HERE")
ax2.set_ylabel("Y-Axis HERE")
ax2.set_title("THIS IS THE TITLE")
ax2.legend()

ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.set_title('Multiple Lines on a Graph')
ax3.legend()

plt.tight_layout()

plt.show()