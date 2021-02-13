# write program to randomly generate a guess on the number 
# Author Catherine Leddy

numbertoguess = 2

import random

print (random.randint (0,100))
while random != numbertoguess:
    if random < numbertoguess:
        print ('Too low')
    else:
        print ('too high')   
    random = int(input("Please guess again:"))
print ("Well done! Yes the correct answer was" , numbertoguess)


