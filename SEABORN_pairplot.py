
import seaborn as sns
import matplotlib.pyplot as plt

#PAIRPLOT

penguins = sns.load_dataset('penguins')
sns.pairplot(data=penguins, hue='species', palette='Set2')
plt.show()

# Pairplot with Specific Variables

tips = sns.load_dataset('tips')
sns.pairplot(data=tips, vars=['total_bill', 'tip', 'size'])
plt.show()

# Pairplot with Custom X and Y Variables

mpg = sns.load_dataset('mpg')
sns.pairplot(data=mpg, x_vars=['mpg', 'horsepower'], y_vars=['weight', 'displacement'])
plt.show()

# Pairplot with Custom Palette

sns.pairplot(data=iris, hue='species', palette='coolwarm')
plt.show()








