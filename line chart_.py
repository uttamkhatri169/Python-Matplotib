import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 12)  # x values from 0 to 10
y = x ** 3  # y values as the square of x

# Create line chart
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.show()


#Multiple Lines in a Single Plot

x = np.arange(0, 12)
y1 = x ** 2
y2 = x ** 3

plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='x squared')
plt.plot(x, y2, label='x cubed')

plt.legend()
plt.show()


# SUBPLOTS

x = np.arange(0, 12)
y1 = x ** 2
y2 = x ** 3

plt.figure(figsize=(12, 5))
# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('x squared')

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('x cubed')

plt.tight_layout()
plt.show()


# Adding Information to the Chart

x = np.arange(0, 12)
y = x ** 3
plt.figure(figsize=(8, 5))
plt.plot(x, y)

# Add title and labels
plt.title('Square Function')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


# Changing Formatting and Adding Markers
x = np.arange(0, 12)
y = x ** 3

# Create line chart with custom formatting
plt.figure(figsize=(8, 5))
plt.plot(x, y, linestyle='--', color='green', marker='o') 

# Add title and labels
plt.title('Square Function with Custom Formatting')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


