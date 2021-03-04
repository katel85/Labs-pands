# Write a program that will keep displaying menu until the user chooses to quit. Call a function for A called do add()
# call a function for V if the user chooses to view called do view().
# Catherine Leddy

def displaymenu () :
 print("what would you like to do?")    
 print("\t(a) Add a new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("type one letter (a/v/q):").strip()
 return choice

def doAdd() :
    print("in adding")
def doView() :
    print("in viewing")

choice=displaymenu()
while(choice != 'q') :
    if choice =='a':
        doAdd()
    elif choice =='v':
        doView()
    elif choice !='q':
        print('\n\nPlease select either a,v or q')
    
    choice=displaymenu()
