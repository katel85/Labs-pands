#In this lab we are going to make a function called Fibonacci in a module called myFunctions
# Author Catherine Leddy

def fibonacci(n):
    return []



#if __name__ == '__main__':
# tests will go here
  # print ("all good")

try:
    fibonacci(-1)
except ValueError:
# we want this exception to be thrown
# so this is an example where we want to do nothing
    pass
else:
# if the exception was not thrown we should throw
# Assertion error
    assert False, 'fibonacci missing ValueError'
# or
#raise AssertionError("fibonacci no valueError ")