# Another way to set the program for name,module and grade.
# Catherine Leddy

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
def doAdd(students):
    print("do add")
def doView(students):
    print("do View")
def doNothing(dumby):
    pass

choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing 
}

Students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        choiceMap[choice]( Students)
    else: 
        print("\n\nplease select either a,v or q")
choice=displayMenu()

