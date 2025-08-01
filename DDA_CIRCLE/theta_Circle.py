import matplotlib.pyplot as plt
import numpy as np



# Input radius
r = int(input("Enter radius of circle: "))
xc = int(input("Enter x-coordinate of center: "))
yc = int(input("Enter y-coordinate of center: "))

# Generate theta values from 0 to 2*pi
theta = np.arange(0, 2 * np.pi, 1/r)

# Calculate x and y coordinates for the circle
x = xc + r * np.cos(theta)
y = yc + r * np.sin(theta)


# Plot the circle points
plt.plot(x, y, color='b')
plt.scatter(xc, yc, color='r', label='Center')

plt.title("Circle using Parametric (Theta) Method")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()