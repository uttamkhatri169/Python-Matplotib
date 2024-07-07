# SCATTERPLOT

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width')
plt.show()


# HUE parameter 
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.show()

# Size,style
tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', size='size', style='smoker')
plt.show()

#custom palette
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', palette='coolwarm')
plt.show()

# Custom Markers
titanic = sns.load_dataset('titanic')
sns.scatterplot(data=titanic, x='age', y='fare', hue='embarked', style='pclass', markers=True)
plt.show()

# With Alpha
sns.scatterplot(data=titanic, x='age', y='fare', hue='survived', alpha=0.6)
plt.show()


