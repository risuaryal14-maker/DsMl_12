#all this assigements are done with user-defined function
'''
#write the greatest number using python
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
a=int(input('write a number for a:'))
b=int(input('write a number for b:'))
c=int(input('write a number for c:'))
print(f'the greatest number is:{greatest(a,b,c)}')

#wite a formuola to calculate fahrenheit to celsius.
def f_to_c(f):
    return 5*(f-32)/9
f=int(input('write the fahreheit to convert into celcius:'))
c= f_to_c(f)
print(f'{round(c,2)}°C')


#wite a recursive function to calculate the sum
def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n
n=int(input('write a number:'))
print(f'the total sum of recursive:{sum(n)}')


#make a funtion to print first n lines
def patterns(n):
    if n==0:
        return
    print('*'*n)
    patterns(n-1)
n=int(input('write a number:'))
print(f'patterns{patterns(n)}')

#write a python function to create inches into cms.
def convert(inches):
    return inches*2.53
inches=float(input('write the inches to convert into cms:'))
c=convert(inches)
print(f'the conversion of inches into cms is:{round(c,2)}')


#removing name from list and strip
def remove(lst,name):
    for item in lst:
        lst.remove(name)
        return lst
lst=['rohan', 'sita', 'gita', 'an']

print(remove(lst,'an'))'''

#write a python function program to multiply the given number

def mul(n):
    for i in range(0, 11):
        print(f'{n} X {i}= {n*i}')
mul(5)