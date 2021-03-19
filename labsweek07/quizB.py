# the with statement will automatically close the file
# when it is finished with it

with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)
#with open("test-b.txt", "w") as f2: # open file again
 #   data = f2.write("another line\n")
  #  print (data)

# in the first program when the text file is created called test-b and the input data = f.write"test b\n' creates
# 7 chars. when the file is opened again and named f2 the date is updated to f2.write("another line\n").
# Both files were also opened with "w" allowing the programmer to read in data.
#  The amount of chars here has now changed to 13. so the program when run will print out
# 7
# 13
#    


