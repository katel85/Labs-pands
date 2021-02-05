# program that prints out random numbers between 1 and 10
# author Catherine Leddy
# ref https://www.w3schools.com/Python/module_random.asp
# ref https://www.w3schools.com/Python/ref_random_choice.asp

import random

number = random.randrange(1,10)
print ('here is a random number {}'.format (number))

number2 = random.randint (21,48)
print ('here is another random number {}'.format (number2))

# trying to do a list of fruit to choose from but couldn't get the formatting right so copied from python w3 school 

mylist = ['apple','orange','banana','pear']
print (random.choice(mylist))












