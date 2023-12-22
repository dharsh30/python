nos=int(input('enter the number'))
count=0
max=int(input('enter the number'))
while count < nos - 1:
    n=int(input('enter the number'))
    if n > max:
        max=n
    count = count + 1
print('max number is',max)