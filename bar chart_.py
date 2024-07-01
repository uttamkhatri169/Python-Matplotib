import matplotlib.pyplot as plt
import numpy as np

fruit = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon', 'muskmelon','Dates']
sizes = [5, 35, 20, 25, 15,40,60]

# Create bar chart
plt.figure(figsize=(9, 6))
plt.bar(fruit, sizes)
plt.show()


# Two Bar Charts in One Plot

fruit = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon', 'muskmelon','Dates']
sizes_a = [5, 35, 20, 25, 15,40,60]
sizes_b = [39, 28, 35, 27, 10, 11, 34]

plt.figure(figsize=(9, 6))
plt.bar(fruit, sizes_a, label='Store A')
plt.bar(fruit, sizes_b, label='Store B')
plt.legend()
plt.show()

# Adding More Details

fruit = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon', 'muskmelon','Dates']
sizes_a = [5, 35, 20, 25, 15,40,60]
sizes_b = [39, 28, 35, 27, 10, 11, 34]
plt.figure(figsize=(9, 6))
plt.bar(fruit, sizes_a, label='Store A')
plt.bar(fruit, sizes_b, label='Store B')

# Add title and labels
plt.title('Weekly Sales Comparison')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Items Sold')
plt.legend()
plt.show()


# Line Chart + Bar Chart

fruit = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon', 'muskmelon','Dates']
sizes = [5, 35, 20, 25, 15,40,60]
cumulative_sales = np.cumsum(sizes)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
ax1.bar(fruit, sizes, color='skyblue', label='Daily Sales')
ax1.set_xlabel('Days of the Week')
ax1.set_ylabel('Number of Items Sold', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Line chart
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(fruit, cumulative_sales, color='orange', marker='o', label='Cumulative Sales')
ax2.set_ylabel('Cumulative Sales', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Add title
plt.title('Daily and Cumulative Sales Over a Week')
plt.show()


#Controlling Overlapping of Bar Charts

fruit = ['Apples', 'Bananas', 'Cherries', 'Mangos', 'Watermelon', 'muskmelon','Dates']
sizes_a = [5, 35, 20, 25, 15,40,60]
sizes_b = [39, 28, 35, 27, 10, 11, 34]
# Define bar width and positions
bar_width = 0.35
x = np.arange(len(fruit))  

# Create bar chart with side-by-side bars
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, sizes_a, width=bar_width, label='Store A', color='blue')
plt.bar(x + bar_width/2, sizes_b, width=bar_width, label='Store B', color='orange')

plt.title('Weekly Sales Comparison')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Items Sold')
plt.xticks(ticks=x, labels=fruit)
plt.legend()
plt.show()


