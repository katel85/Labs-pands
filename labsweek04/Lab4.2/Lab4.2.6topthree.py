#  write program that generates 10 random numbers (0-100) prints them out and then prints out the top three
# Catherine Leddy

import random

howMany = 10
topHowMany = 3
rangeFrom =0
rangeto =100

numbers = []

for i in range (0,10):
    numbers.append(random.randint(rangeFrom,rangeto))

print("{} random numbera\t {}".format (howMany,numbers))

topOnes = numbers.copy()
topOnes.sort (reverse = True)
print ('the top {} are \t\t {}'.format (topHowMany, topOnes [0:topHowMany]))





