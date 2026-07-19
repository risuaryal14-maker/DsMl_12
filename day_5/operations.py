#tuples operations
#1, concatenation()--> combines two tuples and returns a new tuple with all elements from both tuples.
tup1=(1, 2, 3)
tup2=(4, 5, 6)
tup=tup1+tup2
print(tup)

#2, repetition()--> returns a new tuple with the elements of the original tuple repeated a specified number of times.
tup3=(1, 2, 3)
tup4=tup3*3
print(tup4)

#3, membership()--> checks if an element is present in a tuple and returns True or False.
tup5=(1, 2, 3)
print(2 in tup5)
print(4 in tup5)

#4, indexing()--> returns the element at a specified index in a tuple.
tup6=(1, 2, 3)
print(tup6[1])


