n=int(input('enter number'))
m=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if m == rev:
    print('it is palindrome')
else:
        print('it is not palindrome')

