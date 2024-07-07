import seaborn as sns
import matplotlib.pyplot as plt

# BOXPLOT

tips = sns.load_dataset('tips')
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.show()

# boxplot with showmeans
titanic = sns.load_dataset('titanic')
sns.boxplot(data=titanic, x='class', y='fare', showmeans=True, meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black", "markersize": "10"})
plt.show()

# custom orders
penguins = sns.load_dataset('penguins')
custom_order = ['Chinstrap', 'Gentoo', 'Adelie']
sns.boxplot(data=penguins, x='species', y='body_mass_g', order=custom_order)
plt.show()

# with split function
sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker', dodge=True)
plt.show()


# VIOLIN PLOT

iris = sns.load_dataset('iris')
sns.violinplot(data=tips, x='day', y='total_bill', hue='time')
plt.show()

# custom order
penguins = sns.load_dataset('penguins')
custom_order = ['Gentoo', 'Adelie', 'Chinstrap']
sns.violinplot(data=penguins, x='species', y='flipper_length_mm', order=custom_order)
plt.show()

# split violin plot
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
plt.show()

