import datetime
weekday = datetime.datetime.today().weekday() 
if weekday<5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")  

    

