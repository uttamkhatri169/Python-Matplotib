import matplotlib.pyplot as plt

x = [10,13,20,6,12]
y = [12,9,19,22,23]

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

# Scatter Plot with Additional Parameters

x = [10,13,20,6,12]
y = [12,9,19,22,23]

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', marker='*', s=100)  
plt.show()

# Scatter Plot with Multiple Datasets

x1 = [1, 2, 3, 4, 5]
y1 = [10, 9, 8, 7, 6]
x2 = [2, 3, 4, 5, 6]
y2 = [5, 6, 7, 8, 9]

plt.figure(figsize=(8, 5))
plt.scatter(x1, y1, color='blue', label='Dataset 1')
plt.scatter(x2, y2, color='green', label='Dataset 2')

plt.legend()
plt.show()

# Scatter Plot with Titles and Labels

x = [10,13,20,6,12]
y = [12,9,19,22,23]
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='purple')

plt.title('Basic Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()


# Scatter Plot with Color Mapping

x = [10,13,20,6,12]
y = [12,9,19,22,23]
colors = [100, 200, 300, 400, 500]

# Create scatter plot with color mapping
plt.figure(figsize=(8, 5))
scatter = plt.scatter(x, y, c=colors, cmap='viridis', s=100) 
# Add color bar
plt.colorbar(scatter)

plt.title('Scatter Plot with Color Mapping')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()



# HISTOGRAM

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 10, 900)  

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data)

plt.show()

# Histogram with Custom Number of Bins

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=20)
plt.show()

# Histogram with Titles and Labels

data = np.random.normal(0, 10, 900)
plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, color='skyblue')

plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# Multiple Histograms in One Plot

data1 = np.random.normal(0, 10, 900)
data2 = np.random.normal(3, 10, 900)
plt.figure(figsize=(10, 6))
plt.hist(data1, bins=20, alpha=0.5, label='Mean 0, Std 1', color='blue')
plt.hist(data2, bins=20, alpha=0.5, label='Mean 3, Std 1', color='orange')

plt.title('Overlayed Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data
data1 = np.random.normal(0, 10, 900)
data2 = np.random.normal(3, 10, 900)

# Create figure with subplots
plt.figure(figsize=(12, 10))

# First subplot
plt.subplot(2, 1, 1)
plt.hist(data1, bins=20, color='green')
plt.title('Histogram of Data with Mean 0')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Second subplot
plt.subplot(2, 1, 2)
plt.hist(data2, bins=20, color='purple')
plt.title('Histogram of Data with Mean 3')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Display
plt.show()


