import seaborn as sns
import matplotlib.pyplot as plt

# Basic Histogram
ages = [22, 25, 21, 22, 28, 30, 35, 23, 25, 27, 21, 23, 29, 33, 24, 25, 26]

plt.figure(figsize=(9, 6))
sns.histplot(ages, bins=7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# Hue parameter
tips = sns.load_dataset('tips')

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', hue='day', bins=20)
plt.title('Total Bill Distribution by Day')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()


# KDE parameter

scores = [55, 67, 78, 80, 85, 90, 92, 88, 76, 84, 95, 77, 85, 89, 93]

plt.figure(figsize=(9, 6))
sns.histplot(scores, bins=10, kde=True)
plt.title('Exam Scores Distribution with KDE')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()


# Multiple (“layer”, “dodge”, “stack”, “fill”)
tips = sns.load_dataset('tips')

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', hue='day', multiple='dodge', bins=15)
plt.title('Total Bill Distribution by Day ')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

#Element('bar','steps')
tips = sns.load_dataset('tips')

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', element='poly', bins=15)
plt.title('Total Bill Distribution with Bars')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

# STAT
tips = sns.load_dataset('tips')

# Answer
plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', stat='count', bins=15)
plt.title('Total Bill Distribution with Count')
plt.xlabel('Total Bill ($)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', stat='frequency', bins=15)
plt.title('Total Bill Distribution with Frequency')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', stat='density', bins=15)
plt.title('Total Bill Distribution with Density')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.show()

plt.figure(figsize=(9, 6))
sns.histplot(data=tips, x='total_bill', stat='probability', bins=15)
plt.title('Total Bill Distribution with Probability')
plt.xlabel('Total Bill ($)')
plt.ylabel('Probability')
plt.show()




