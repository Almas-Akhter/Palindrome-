s=input("Enter a string:")

W=""

for i in s[::-1]:

    w = w+i

if (s==w):

    print(s, 'is a Palindrome string')

else:

    print(s, 'is NOT a Palindrome string')
