# The with statement will automatically close the file
# when it is finished with it

with open("test-d.txt", "w") as f:
 data = f.write("test d\n") # returns the number of chars written
 print (data)
with open("test-d.txt", "a") as f2: # open file again
 data = f2.write("another line\n")
 print (data)

 # this code is similiar to code in quizB apart from the fact that the second line of code wants to append (add)
 # to the data that is already in the test-d.txt file.

 