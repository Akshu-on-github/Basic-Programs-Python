'''
Question- Write a program to obtain principal amount , rate of interest from user and compile
simple interest
'''
#solution-
amt=int(input("Enter principal amount"))
rate=int(input("Enter rate"))
time=int(input("Enter time"))
si=(amt*rate*time)/100
print ("Simple interest is =",si)