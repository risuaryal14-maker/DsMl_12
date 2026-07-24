print('frist:')
fruits=['bananna','apple', 'orange', 'mango']
for fruit in fruits:
    print(fruit)

#highest score couting with loops
print('second:')
lst=[1,3,23,465,78,9,45,78,346,778,9677] 
max_number=0
for number in lst:
   if number>max_number:
        max_number=number
print(max_number)

#range 
print('third:')
for i in range(1, 10):
    print(i)

#step range [start:end:step]
print('fourth:')
for i in range(1,11,3):
    print(i)

#addint 1 to 100
print('fifth')
sum=0
for i in range(1,101):
    sum+=i
print(sum)