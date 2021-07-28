def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input('Enter word to check for palindrome: ')
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
