import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



# BARPLOT

tips = sns.load_dataset('tips')
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', hue='time')
plt.title('Total Bill by Day and Time')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()


# for a Particular Month

data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'January_Temperature': [30, 60, 20, 55, 65]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='City', y='January_Temperature')
plt.title('Average Temperature in January by City')
plt.xlabel('City')
plt.ylabel('Temperature (°F)')
plt.show()


#  Custom Estimator
import numpy as np 
tips = sns.load_dataset('tips')
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.median)
plt.title('Median Total Bill by Day')
plt.show()


# Horizontal Bar Plot

titanic = sns.load_dataset('titanic')
plt.figure(figsize=(10, 6))
sns.barplot(data=titanic, x='age', y='class', orient='h')
plt.title('Average Age by Class')
plt.xlabel('Average Age')
plt.show()



# HEATMAP

data = {
    'Monday': [200, 150, 250],
    'Tuesday': [220, 180, 230],
    'Wednesday': [210, 160, 240],
    'Thursday': [230, 170, 220],
    'Friday': [250, 200, 270]
}
df = pd.DataFrame(data, index=['Product A', 'Product B', 'Product C'])
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Weekly Sales Data')
plt.xlabel('Day')
plt.ylabel('Product')
plt.show()


# Custom Tick Labels

data = {
    'January': [30, 60, 20, 55, 65],
    'February': [32, 62, 22, 57, 67],
    'March': [45, 65, 35, 70, 75]
}
df = pd.DataFrame(data, index=['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt='.1f', cmap='viridis')
plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('City')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()

