#In this lab we are going to make a function called Fibonacci in a module called myFunctions
# Author Catherine Leddy

def fibonacci(number):
    return []



return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'


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






