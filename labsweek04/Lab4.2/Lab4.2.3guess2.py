# guess the number and enter statement to say whether the answer is too high/low
#  Author Catherine Leddy



numbertoguess = -1

guess = int(input ("Please guess a number between -5 and 5:"))
while guess != numbertoguess:
    if guess < numbertoguess:
        print ('Too low')
    else:
        print ('too high')   
    guess = int(input("Please guess again:"))
print ("Well done! Yes the correct answer was" , numbertoguess)


