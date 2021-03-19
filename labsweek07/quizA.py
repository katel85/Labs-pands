# the with statement will automatically close the file
# when it is finished with it


with open("test-a.txt") as f:
 data = f.read()
 print (data)

 #Traceback (most recent call last):
 # File ".\quiz.py", line 5, in <module>
 #   with open("test-a.txt") as f:
 #FileNotFoundError: [Errno 2] No such file or directory: 'test-a.txt'
 # there is no file called test-a.text so it can't find the file or print the data
