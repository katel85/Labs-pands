# program takes in a float and outputs and int rounded down
# Catherine Leddy
# ref https://www.w3schools.com/python/python_math.asp

import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))

