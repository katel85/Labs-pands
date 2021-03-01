# messing with the labtask for week 05
# Author Catherine Leddy

import pandas as pd 

def check_weekday(date):
    res=len(pd.bdate_range(date,date))

    if res == 0 :
        print("It is the weekend, yah")
    else:
        print ("Yes, unfortunately today is a weekday")




date = "2021-02-20"
check_weekday(date)

date = "2021-02-17"
check_weekday (date)






