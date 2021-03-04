# how to write the additional do view program
# Catherine Leddy


def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
    displayModules(currentStudent["modules"])
