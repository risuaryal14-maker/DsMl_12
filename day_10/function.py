'''----function types--
--user-defined function
--built-in function'''
#user defined function
print('first--------->')
def sum(a,b):
    return a+b
print(sum(9,7))

#no parameters, no return
print('second---->')
def greet():
    print('hello world')
greet()

#no parameters, has return
print('third---->')
def get_pi():
    pi=3.14
    return pi
value = get_pi()
print('value of pi:',value)


# has parameters, no return
print('fifth---->')
def greet(name):
    print(f'hello,{name}')
greet('rickson')

#has parameters, has return
print('sixth--------->')
def add(a,b):
    sum=a+b
    return sum
#function calll
result=add(3,5)
print(f'total sum:{result}')


#defult arguments
print('seventh----->')
def greet(name,ending='thank you'):
    print(f'good day,{name}')
    print(ending)
greet('rickson')
greet('rohan','thanks')
