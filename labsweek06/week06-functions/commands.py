# write a function that prints out a meno of coammands we can perform. Function should return the users choice
# Catherine Leddy

def displaymenu () :
 print("what would you like to do?")    
 print("\t(a) Add a new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("type one letter (a/v/q):").strip()
 return choice


choice = displaymenu ()
print("you choose{}".format(choice))

# issue initially with synthax. The print allignment was not correct under the def function. Ensure alignment
# correct or else synthax errors will occur

