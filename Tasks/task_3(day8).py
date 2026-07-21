'''
1,Check if a number is positive and even.
2,Check if a user is not logged in.
3,Check if age is between 18 and 60 using and.
4,Check if a day is Saturday or Sunday using or.'''

user_id=input('write user id:')
if user_id== 'risu12':
    print('correct!!')
else:
    print('excess denied!!')
password=input('write password:')
if password=='risu@123':
    print('correct, the user is loged in.')
else:
    print('incorrect password, the user is not logged in.')

print('question no.1')
#check if a number is positive or not..
num=int(input('write a number:'))

if num>0 and num%2==0:
    print('the given number is positive and even')
elif num<0:
    print('the given number is negative')
elif num%2==1:
    print('the given number is odd')
else:
    print('wrong out')

print('question no2.')
#check if a user is loged in or not
log=input('write if the user is login:')
if log=='true':
    print('use is login')
elif log=='false':
    print('user is not login')
else:
    print('wrong input')

print('question no.3')
#check wheather the user is between 18 and 60..
age=int(input('write the age to check:'))
if age>=18 and age<=60:
    print('granted, you are between 18 to 60')
else:
    print('wrong input')

print('question no.4')
#check wheather the day is sunday or saturday..
day=input('write the day')
if day=='sunday' or day=='saturday':
    print('yes,today is sunday or saturday')
else:
    print('wrong input')