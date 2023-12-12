import numpy as np
import matplotlib.pyplot as plt

# Set the size of the image
fig, ax = plt.subplots(figsize=(16, 9))

# Create a grid of lines
x, y = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
ax.plot(x, y, color='black', linewidth=2)

# Add some random laser beams
for i in range(10):
    x1, y1 = np.random.uniform(-1, 1, 2)
    x2, y2 = np.random.uniform(-1, 1, 2)
    ax.plot([x1, x2], [y1, y2], color='magenta', linewidth=4)

# Add some text
ax.text(0, 1.2, 'SCHOOL PICTURE DAY', fontsize=50, fontweight='bold',
        ha='center', va='center', color='white', backgroundcolor='black')

# Set the axis limits and turn off the axis
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Save the image
plt.savefig('school_picture_background.png', dpi=300, bbox_inches='tight')
 