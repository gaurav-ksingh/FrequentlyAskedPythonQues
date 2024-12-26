#method1: find reverse of string
s=input("enter a string:")
print(s[:]) #abcde
print(s[0:5]) # abcde
print(s[0:5:1])
print(s[::])
revstr=(s[::-1]) #reverse string

if revstr==s:
    print("palindrome")
else:
    print("not palindrome")

