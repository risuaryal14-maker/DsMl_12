'''---ATM Menu System----
Create a simple ATM menu.
Menu:
1. Check Balance
2. Deposit
3. Exit'''
balance=5000
    
print('--welcome to ATM---')
print('press 1\n --to check balance')
print('press2\n ---to check deposit')
print('press3\n ---to exit')
while True:
    press=int(input('press the number:'))

    #invalid 
    if press<1 or press>3:
        print('invalid number')
        continue
    #check balance
    if press==1:
        print('balance:',balance)
    #deposit
    elif press==2:
        amt=int(input('enter the amount:'))
        balance= amt+balance
        print('update balance', balance)

    elif press==3:
        print('Thanks for visiting us')
        break
