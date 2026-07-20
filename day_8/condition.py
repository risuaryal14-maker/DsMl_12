'''
--Conditions are specific criteria that must be met for
a set of instructions to be executed.

--For example, in the real world, people dance when
there is music.

--The presence of music is a condition and when it is
true, people will dance.

--Similarly, in python programming, we use
conditions to determine which set of instructions to
execute
#if else
age=16
if age>=18:
    print('you are able to drive')
else:
    print('you are not able to drive')




#if elif and else conditions
age=int(input('write your age:'))
if age>=18 and age<=26:
    print('adult')
elif age<17:
    print('teen')
elif age>=26 and age<=60:
    print('old')
else:
    print('too old')

#nested statement in conditions
name=input('write your name:')
age= int(input('write your age:'))
if age>=18:
    print('do you have citizenship card?',name)
    ans=input('yes or no?:')
    if ans=='yes':
        print('you are able to vote',name)
    elif ans=='no':
        print('sorry you are not able to vote',name)
    else:
        print('error--it seems you chooes different key')
elif age<=17:
    print('you are not able to vote')
else:
    print('error--it seems you chooes different key')

#Ternary Operator in Python
num=int(input('write a number to check odd or even:'))
print('even'if num%2==0 else 'odd')


#any() Function with if

students=[30,20,40]
if any(student>=40 for student in students):
    print('at least one student passed')'''

persons=['rita', 'sita', 'git ', 'maya']
if any(person=='isha' for person in persons):
    print('one name is right')
else:
    print('wrong name')