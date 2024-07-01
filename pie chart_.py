import matplotlib.pyplot as plt

toys= ['Car', 'Bike', 'Teedy', 'Aeroplane', 'Dianasour']
prices= [50, 35, 20, 25, 15]

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(prices, labels=toys)
plt.show()



#adding colors by you choice
toys= ['Car', 'Bike', 'Teedy', 'Aeroplane', 'Dianasour']
prices= [50, 35, 20, 25, 15]
colors = ['red', 'yellow', 'pink', 'blue', 'green']

plt.figure(figsize=(6, 6))
plt.pie(prices, labels=toys, colors=colors)
plt.show()


# exploding the parts

toys= ['Car', 'Bike', 'Teedy', 'Aeroplane', 'Dianasour']
prices= [50, 35, 20, 25, 15]
colors = ['red', 'yellow', 'pink', 'blue', 'green']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(prices, labels=toys, colors=colors, explode=explode)
plt.show()


#shadow and startangle

toys= ['Car', 'Bike', 'Teedy', 'Aeroplane', 'Dianasour']
prices= [50, 35, 20, 25, 15]
colors = ['red', 'yellow', 'pink', 'blue', 'green']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.figure(figsize=(6, 6))
plt.pie(prices, labels=toys, colors=colors, explode=explode, shadow=True, startangle=90)
plt.show()


#styled pie chart

toys= ['Car', 'Bike', 'Teedy', 'Aeroplane', 'Dianasour']
prices= [50, 35, 20, 25, 15]
colors = ['red', 'yellow', 'pink', 'blue', 'green']
explode = (0, 0.2, 0.1, 0.1, 0)

plt.style.use('ggplot') 

plt.figure(figsize=(6, 6))
plt.pie(prices, labels=toys, colors=colors, explode=explode, shadow=True, startangle=90)
plt.legend(toys, loc='upper left', bbox_to_anchor=(1, 0.8))
plt.show()



