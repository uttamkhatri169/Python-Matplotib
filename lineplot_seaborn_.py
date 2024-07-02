import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#lineplot from a dataframe

data = {
    'fruits': ['Mango', 'Banana', 'Cherries', 'Apple', 'Orange', 'Dates'],
    'Sales': [200, 210, 190, 300, 320, 350]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.lineplot(x='fruits', y='Sales', data=df)
plt.title('fruits Sales Over Time')
plt.xlabel('fruits')
plt.ylabel('Sales')
plt.show()


# Line Plot from Lists

time = [1, 2, 3, 4, 5, 6]
temperature = [30, 32, 33, 31, 29, 35]

plt.figure(figsize=(8, 5))
sns.lineplot(x=time, y=temperature, markers=True, dashes=True)
plt.title('Temperature Over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.show()


# Line Plot with a Dataset
tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.lineplot(x='size', y='total_bill', hue='day', data=tips)
plt.title('Total Bill Over Time by Day')
plt.xlabel('Party Size')
plt.ylabel('Total Bill ($)')

plt.legend(title='Day')
plt.show()


# Line Plot with Multiple Lines

tips = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))
sns.lineplot(x='size', y='total_bill', data=tips, label='Total Bill', linestyle='-', marker='o')
sns.lineplot(x='size', y='tip', data=tips, label='Tip', linestyle='--', marker='x')
plt.title('Total Bill and Tip Over Time')

plt.legend(title='Legend')
plt.show()


# Line Plot with Customized Ticks and Grid

fruits =['Mango', 'Banana', 'Cherries', 'Apple', 'Orange', 'Dates']
prices = [200, 210, 190, 300, 320, 350]

plt.figure(figsize=(12, 6))
sns.lineplot(x=fruits, y=prices)
plt.title('Fruits Prices Over a Week')
plt.xticks(['Mango', 'Banana', 'Apple', 'Dates'])  
plt.grid(True)
plt.show()
