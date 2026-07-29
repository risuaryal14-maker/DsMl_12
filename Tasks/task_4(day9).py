
'''
---Number guessing challenge--
Create a program where:
A secret number is stored inside the program.
User keeps entering numbers.
If the number matches, print:
"Correct Guess!"
Use break to stop the loop.
If wrong, print:
"Try Again"'''

guess_number=int(input('guess the number'))
while True:
    print('try again')
    guess_number=int(input('guess the number:'))
    if guess_number==3:
        print('correct guess')
        break
