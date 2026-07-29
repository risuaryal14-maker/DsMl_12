def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n=int(input('write a number:'))
print('the factorial number of',n,f'is:{factorial(n)}')