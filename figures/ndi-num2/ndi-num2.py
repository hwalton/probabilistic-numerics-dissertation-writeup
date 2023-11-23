import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.patches as mpatches

plt.figure(figsize=(8, 4.8))

# Set global font size
plt.rcParams.update({'font.size': 12})

# Define the range and density of the x-axis
x = np.linspace(-4, 4, 1000)

# Normal distribution values
y = norm.pdf(x)

# Area under the curve for a specific range
x_fill = np.linspace(-2, 1, 500)  # Range for filling under the curve
y_fill = norm.pdf(x_fill)

# Create the plot for the normal distribution
plt.plot(x, y, label='Normal Distribution', color='blue')
plt.fill_between(x_fill, y_fill, alpha=0.5, color='blue', label='Definite Integral')

# Numerical Integration using rectangles
num_rectangles = 6
width = (1 - (-2)) / num_rectangles  # Width of each rectangle
x_rectangles = np.linspace(-2, 1, num_rectangles, endpoint=False)  # Left side of each rectangle

# Draw rectangles with red outline and lighter red fill
for i in range(num_rectangles):
    left_height = norm.pdf(x_rectangles[i])
    right_height = norm.pdf(x_rectangles[i] + width)
    rect_height = max(left_height, right_height)
    plt.gca().add_patch(plt.Rectangle((x_rectangles[i], 0), width, rect_height,
                                      edgecolor='red', facecolor='lightcoral', alpha=0.5))

# Create a custom patch for the legend
rect_patch = mpatches.Patch(facecolor='lightcoral', edgecolor='red', label='Numerical\nApproximation')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Numerical Integration Approximation')
plt.legend(handles=[rect_patch, plt.Line2D([0], [0], color='blue', label='Normal Distribution'),
                    plt.Rectangle((0, 0), 1, 1, color='blue', label='Definite Integral', alpha=0.5)],
           loc='upper right')

# Save the figure
plt.savefig('ndi-num2.png')
plt.show()
