def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
numbers = [1, 2, 3, 4, 5]
result = list(map(double_even, numbers))
print(result)
