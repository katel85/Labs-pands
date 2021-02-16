# messing with collatz
# Author Catherine Leddy
# https://stackoverflow.com/questions/33324432/collatz-sequence-python-3


print('This is a Collatz Sequence')
user= int(input('Please enter a positive integer number:'))
def collatz(n): 
    print(n)
    while n != 1: # create a while loop until the  number returned is equal to 1 (loop will run until 1 is returned)
        if n % 2 == 0: # id the number is even the number will be divided by 2 and the number is printed
            n = n // 2
            print(n)
        else:
            n = n * 3 + 1 # if the number is odd it will be multiplied by 3 and 1 added 
            print(n)


collatz(user)





