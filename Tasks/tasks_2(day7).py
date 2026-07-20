'''
--Create a dictionary to store student name, age, and faculty.
--Add a new key called phone to an existing dictionary.
--Update the value of age in a dictionary.
--Remove a key named city from a dictionary using del.
--Check whether the key email exists in a dictionary'''

person={'name':'rickson', 'age':23, 'faculty':'ai'}
print(person)

person['phone']=9800000000
print(person)

person['age']=19
print(person)

person['city']='kathmandu'
print(person)

del person['city']
print(person)