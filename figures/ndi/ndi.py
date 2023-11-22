import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.figure(figsize=(8, 4.8))

# Define the range and density of the x-axis
x = np.linspace(-4, 4, 1000)

# Normal distribution values
y = norm.pdf(x)

# Area under the curve for a specific range
x_fill = np.linspace(-2, 1, 500)  # Adjust -4 and 1 to your range
y_fill = norm.pdf(x_fill)

# Create the plot
plt.plot(x, y, color='blue', label='Normal Distribution')
plt.fill_between(x_fill, y_fill, alpha=0.5, color='blue', label='Definite Integral')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Definite Integral of the Normal Distribution')
plt.legend()

# Save the figure
plt.savefig('ndi.png')
plt.show()
