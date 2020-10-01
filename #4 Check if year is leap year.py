#Question - Write a program to take year as input an check if it is a leap year or not.

# Solution=

year=int(input("Enter the year"))

if year%4 == 0:
ritlk
	if year%100==0:

		if year%400==0:
			print(f"{year}  is leap year")

		else:
			print(f"{year} is not leap year")

	else:
		print(f"{year} is leap year")

else:
	print (f"{year} is not a leap year")
