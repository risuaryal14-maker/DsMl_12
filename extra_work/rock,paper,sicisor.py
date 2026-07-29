import random
lst=['rock','paper','scissior']
computer= random.randint(0,2)
human=int(input('pick the number, 0 for rock, 1 for paper and 2 for scisior:'))
if human<0 or human>2:
    print('error')
elif human==0 and computer==2:
    print('human wins')
elif human>computer:
    print('human wins')
elif computer==0 and human==2:
    print('human wins')
elif computer>human:
    print('computer wins')
elif human==computer:
    print('draw')
print('human chooses:',lst[human])
print('computer chooses:',lst[computer])


