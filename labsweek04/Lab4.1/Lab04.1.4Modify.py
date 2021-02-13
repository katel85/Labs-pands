# How would you use a while loop to modify 1 so that it keeps prompting the
# user for a number until the user enters -1

val= input (" enter a number between -2 and 3 : ")
while val != '-1':
    print ('you said:'+ val) 
    val = input("(enter correct number to quit):")
print ('correct the answer was -1')


# used the loop video and test while to get this to enter -1 and the program will stop.
# this is using a while loop
