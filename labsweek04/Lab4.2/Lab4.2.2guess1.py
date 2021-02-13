# guess the number from the user until it gets it right
# Author Catherine Leddy

numbertoguess = -1
guess = int(input ("Please guess a number between -5 and 5:"))
while guess != numbertoguess:
    print ( "Wrong!")
    guess = int (input( "Please guess again:"))

print ( "Well done! Yes the correct answer was" , numbertoguess)


