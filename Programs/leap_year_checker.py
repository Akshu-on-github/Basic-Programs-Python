'''
Author: Abdurahman Ali Mohammed
Leap years are years where an extra, or intercalary, day is added to the end of the shortest month, February. 
The intercalary day, February 29, is commonly referred to as leap day.

Leap years have 366 days instead of the usual 365 days and occur almost every four years.
'''

def isLeapYear(year):
    if (year % 4) == 0: #check if year is divisible by 4
       if (year % 100) == 0:#check if it is divisible by 100
           if (year % 400) == 0:#check if it is divisible by 400
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
       else:
           print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))
    
    
   
 
 
# take an input and pass it to the method
y = input('Enter the year you want to check:')
ans = isLeapYear(int(y))
