# program reads in a string and strips leading or trailing spaces
# programs converts all letters to lower case
# program outputs the length of the original string and the normalized one
# Author Catherine Leddy
# ref https://stackoverflow.com/questions/26574191/how-to-capitalize-a-string-in-python


rawString= input ('please enter a string:')
normalizedString = rawString.strip().lower()

lenghtOfRawString= len(rawString)
lenghtOfNormalized= len(normalizedString)

print("That String normalised is :{}".format(normalizedString))
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalized ))

# messing with different string methods:

NewString= input ('please enter a string:')
NewNormalizedString = NewString.upper()

print("That String encoded and capitalized is {}".format(NewNormalizedString))











