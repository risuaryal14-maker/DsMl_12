'''with open('file.txt') as f:
    print(f.read())'''


def star(n):
    if n==0:
        return 
    print('*'*n)
    star(n-1)
    star(n+1)
n=int(input('write a number:'))
print(f'star{star(n)}')


def patterns(n):
    if n==0:
        return
    print('*'*n)
    patterns(n-1)
n=int(input('write a number:'))
print(f'patterns{patterns(n)}')