# this program will print out random fruit from a list 
# Author Catherine Leddy

import random
fruits = ['Kiwi', 'Orange', 'Banana', 'Pear', 'Pineapple']
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

