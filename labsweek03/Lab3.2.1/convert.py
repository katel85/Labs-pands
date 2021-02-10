# program takes in a float amount in dollars and outputs abs amount in cent
# Author Catherine Leddy
# ref https://learnandlearn.com/python-programming/python-reference/python-abs-function
# ref https://www.w3schools.com/python/python_datatypes.asp



number = float(input("Enter a number:"))
absoluteValue = abs(int(number*100))
print('The absolute value of {} is {}'.format(number, absoluteValue))

# task 1 is number must be defined as float becasue of decimal point.
# Task 2 to convert the dollars to cents we must multiple the value by 100 which will be an int
# Task 3 in order for the program to give out 599 instead of -599 we must but abs in front of (int(number*100))