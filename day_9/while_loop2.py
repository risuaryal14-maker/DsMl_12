#counting number
print('frist----------->')
n=0
while n<10:
    n=n+1
    print(n)

#steps number
print('second--------->')
n=0
while n<10:
    n=n+2
    print(n)

#break Statement
print('third-------------->')
num1=1
while num1<10:
    if num1==5:
        break
    print(num1)
    num1 += 1
print('loop ended')

#continue statement
print('forth--------->')
num2=0
while num2<5:
    num2 +=1
    if num2==3:
        continue
    print(num2)
print('loop ended')

#pass statement
print('fifth--------->')
num3=0
while num3<5:
    num3 +=1
    if num3==3:
        pass
    print(num3)
print('loop ended')