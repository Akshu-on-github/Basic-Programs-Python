'''
Question - Write a program that reads a number of seconds and prints it in form : mins and seconds .
Example - 200 seconds are printed as 3 mins and 20 seconds.
'''
# Solution-

totalsec=int(input("Enter the number of seconds"))

seconds=totalsec%60
minutes=totalsec//60

if minutes>=60:
	hours=minutes//60
	minutes=minutes%60
	print ("hours",hours,"minutes",minutes,"seconds",seconds)
else:
	print("minutes",minutes,"seconds",seconds)
