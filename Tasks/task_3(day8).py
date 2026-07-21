'''
1,Check if a number is positive and even.
2,Check if a user is not logged in.
3,Check if age is between 18 and 60 using and.
4,Check if a day is Saturday or Sunday using or.'''

num=int(input('write a number:'))
if num>0 and num%2==0:
    print('the given number is positive and even')
elif num<0:
    print('the given number is negative')
elif num%2==1:
    print('the given number is odd')
else:
    print('wrong out')
    
