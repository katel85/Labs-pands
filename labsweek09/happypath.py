#In this lab we are going to make a function called Fibonacci in a module called myFunctions
# Author Catherine Leddy
import logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):

    if number == 0:
        return []

    if number < 0:
        raise ValueError('number must be > 0')
    
    a = 0
    b= 1
fibonaccisequence = [0]
for i in range(1,number):
    fibonaccisequence.append(b)
    a , b = b, a + b

#logging.debug("%d: %s",number, fibonacciSequence)



