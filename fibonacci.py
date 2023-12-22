def fibonacci(n_term):
    n1 = 0
    if n_term == 1:
        print(n1)
    else:
        count=0
        n2=1
        while count <n_term:
            print(n1)
            temp=n2
            n2=n1+n2
            n1=temp
            count+=1
if __name__ == '__main__':
    n_term = int(input('Find Fibonacci of how many terms: '))
    fibonacci(n_term)
    
    
    
    
    
            