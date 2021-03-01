#program that stores a student name and a list of her courses and
#grades in a dict, the program should then print out her data.
#The number of course she has could change

student = {
"name":"Kate",
"modules": [
{
"courseName":"ProgrammingandScripting",
"grade": 95
},
{
"courseName":"Computing",
"grade":99
}
]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

# 2 parameters in this dictionary 1. name 2. modules (this has two keys so it is put into a list inside the dict
# the first print takes the student name out of the dictionary to print 
# the for loop then takes out the course names and the grades assigned from the dict 2nd parameter.
