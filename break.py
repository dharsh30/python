s ='cakes'
for letter in s:
    print(letter)
    if letter == 'e'or letter == 's':
     break
print("Out of for loop")
print()

for i in range(1, 6):
    for j in range(3, 5):
        if j%i == 0:
            break
        print(i, j)