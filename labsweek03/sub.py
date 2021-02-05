#program to subtract one number for another
# author Catherine Leddy
# ref https://www.w3schools.com/python/python_numbers.asp

x = 10.1
y = 4
answer= (x-y)

print ("{} minus {} is {}".format (x, y, answer))

# completely changed format of x and y and got corret answer did not use input or int like in example in lab 2.3 

a = int (input ('Enter first number:'))
b = int (input ('Enter second number here:'))
answer2= a-b 

print ("{} minus {} is {}".format (a, b, answer2))

# After realising I should have followed the example with the words exactly as in example lab 2.3 
# I got the correct output. I was following the lab instructions incorrectly. I did not realise I was asking 
# for the numbers in the output. I was just looking for the correct answer in the output as above.

a = float (input ('Enter first number:'))
b = int (input ('Enter second number here:'))
answer2= a-b 

print ("{} minus {} is {}".format (a, b, answer2))

# the format was changed in a to float in order to accomadate the decimal place



 









