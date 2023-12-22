def factorial(n):
    if n == 0:
      return 1
    else:
      fac = 1
      while n >= 1: 
        fac *= n # same as &#39;fac = fac * n&#39;
        n -= 1
      return fac
if __name__ =='__main__':
    n = int(input("Find factorial of: "))
    fac = factorial(n)
    print("Factorial of {} is {} ".format(n,fac))