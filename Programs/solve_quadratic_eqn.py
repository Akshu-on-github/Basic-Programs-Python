# Assuming the quadraic equation is in the form ax**2 + bx + c = 0

#mporting related modules
import math

#taking input from user
a = int(input("Enter the coefficient of x**2 i.e. value of a:   "))
b = int(input("Enter the coefficient of x i.e. value of b:  "))
c = int(input("Enter the value of constant i.e. c:  "))

#displaying the equation
print("\nGiven equation is ", a , "x**2 + ", b , "x + ", c ," = 0")

#calculating the discrimant value
d = (b**2) - (4*a*c)
square_root = math.sqrt(abs(d)) 
#finding the roots of eqn
r1 = round((-b + square_root)/(2*a))
r2 = round((-b - square_root)/(2*a))

#printing the roots and thier nature
if d == 0 :
    print("\nThe roots are real and equal")
    print("The roots are ",r1," and ",r2)
elif d > 0 :
    print("\nThe roots are real and unequal")
    print("The roots are ",r1," and ",r2 )
if d < 0 :
    print("\nThe roots are imaginary")
    print( "The roots are ",r1," and ",r2 )

# Sample Output:
# Enter the coefficient of x**2 i.e. value of a:   1
# Enter the coefficient of x i.e. value of b:  5
# Enter the value of constant i.e. c:  10

# Given equation is  1 x**2 +  5 x +  10  = 0

# The roots are imaginary
# The roots are  -1  and  -4

