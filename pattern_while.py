def print_pattern(n):
    i=0
    j=0
    while i<=n:
        while j <=i:
            print('*',end='')
            j+=1
        j=0
        i+=1
        print('')
if __name__ == '__main__':
    n=5
    print_pattern(5)
        