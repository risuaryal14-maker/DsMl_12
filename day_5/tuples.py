'''--TUPLES--
Ordered and immutable collection
Allows duplicate values
Stores mixed data types
'''

#TUPLES
tup=(1, 2, 3,'rickson', 3.5,(4, 5))
print(type(tup[4:5]))
print(tup)

#Tuples functions in python
 
#len()--> returns the number of elements in a tuple
tup1=(1, 2, 3, 4, 5)
print(len(tup1))

#max()--> returns the largest element in a tuple
tup2=(1, 2, 3, 9, 4, 5, 9.1)
print(max(tup2))

#min()--> returns the smallest element in a tuple
print(min(tup2))

#sum()--> returns the sum of all elements in a tuple
print(sum(tup2))

#any()--> returns True if any element in a tuple is True
tup3=(0, 0, 0, 1)
print(any(tup3))

#all()--> returns True if all elements in a tuple are True
tup4=(1, 2, 3, 'rickson', 3.5)
print(all(tup4))

#sorted()--> returns a sorted list of elements in a tuple
tup5=(3, 1, 4, 2)
print(sorted(tup5))
