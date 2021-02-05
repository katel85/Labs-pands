# program reads in 2 numbers and outputs the interger answer and the remainder
# Author Catherine Leddy
# ref https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
# ref https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division



x = int(input( 'enter first number:'))
y = int(input('enter the number you would like to divide by:'))
answer=int(x//y)
remainder = x%y 

print ('{} divided by {} is {} and the remainder is {}'.format (x, y, answer, remainder))






