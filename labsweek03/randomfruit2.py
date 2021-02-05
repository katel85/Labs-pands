#changing the formatting of the random fruit line from square brackets to round brackets


import random
fruits = ('Kiwi', 'Orange', 'Banana', 'Pear', 'Pineapple')
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

