# change the precent grade if not a whole number (int) to a grade when rounded up
# Kate Leddy

percentage = float(input("Enter the percentage: ")) 
# changed int to float to round up a decimal number 
if percentage < 0 or percentage > 100:
 
 print ("Please enter a number between 0 and 100")
elif percentage < 40: 
 print ("Fail")
elif percentage < 50: 
 print ("Pass")
elif percentage < 60: 
 print ("Merit1")
elif percentage < 69.5: # change 70 to 69.5 to round up to distiction grade 
 print ("Merit2")
else: 
 print ("Distinction")

 # another way to do it is to round up the number.Need to import math 


