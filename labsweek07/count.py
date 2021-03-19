

#with open ('count.txt', 'x') as f:
#    print ('create a file')
     
filename = "count.txt"
def readNumber():
 with open(filename) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
print (num)
   
