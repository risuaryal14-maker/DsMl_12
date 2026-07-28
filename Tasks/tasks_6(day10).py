'''
Q1, Write a function area(length, breadth) that returns the
area of rectangle.
Q2,Write a Python program using User Defined Function
(UDF) that:
Takes two numbers from the user
Takes an operator sign (+, -,*, /)
Performs the selected operation
Displays the result'''

#question no.1
def area(a,b):
    call=(a+b)
    return call
result=area(8,7)
print('area of rectange is:',result)


#question no.2

def calculator(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    else:
        print('you enter invalid operators')

first=float(input('enter the first number:'))
second=float(input('enter the second number:'))
operator=input("enter the operator: +,-,*,/")
result=calculator(first, second, operator)
print('result:',result)
     