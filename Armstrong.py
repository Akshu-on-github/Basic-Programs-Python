# Armstrong number: A three-digit number whose sum of the cubes of its digits is equal to the number itself
# Function to check if the given number is an Armstrong number
def checkArmstrong(num):
   sum = 0
   temp = num
   while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
   if num == sum:
      print(num, "is an Armstrong number")
   else:
      print(num, "is not an Armstrong number")

# Input & function call
num = int(input("Please enter the number to be checked: "))
checkArmstrong(num)
