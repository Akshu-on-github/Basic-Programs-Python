'''Question- write a program to obtain temperature of 7 days and then display average temperature of
the week'''
# Solution
temp=[]
days=("Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday")
for j in range(7):
	print ("Enter the max terperature of",days[j])
	temperature=int(input())
	temp=temp+[temperature]
print("average temperature is =",(sum(temp)/7))
