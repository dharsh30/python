import random
n=random.randint(1,10)
guess=0
while guess != n:
    guess=int(input('guess a no'))
    if guess<n:
        print('smaller')
    elif guess>n:
        print('larger')
    else:
        print('correct guess')