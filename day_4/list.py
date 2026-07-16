'''Ordered and mutable collection
Allows duplicate values
Stores mixed data types
Example:
numbers = [1, 2, 3]
numbers.append(4)'''

#LISTS
lst=[1, 2, 3,'rickson', 3.5,[4, 5]]
print(lst)
print(len(lst))


#slicing in lists
#[START:STOP:STEP]

lst2=[3, 1, 5,'risu', 5.5,[3, 7]]
print(lst[0:4:3])

#LIST OPERATIONS
#append()--> adds an element to the end of the list
lst3=[1, 2, 3]
lst3.append(4)
print(lst3)

#extend()--> adds multiple elements to the end of the list
lst4=[1, 2, 3]
lst4.extend([4, 5, 6])
print(lst4)

#insert()--> adds an element at a specific index
lst5=[1, 2, 3]
lst5.insert(1, 4)
print(lst5)

#remove()--> removes the first occurrence of an element
lst6=[1, 2, 3, 4, 5]
lst6.remove(3)
print(lst6)

#pop()--> removes and returns the element at a specific index
lst7=[1, 2, 3, 4, 5]
lst7.pop()
print(lst7)

#clear()--> removes all elements from the list
lst8=[1, 2, 3, 4, 5]
lst8.clear()
print(lst8)

#count()--> returns the number of occurrences of an element
lst9=[1, 2, 3, 4, 5, 3]
count=lst9.count(3)
print(count)

#index()--> returns the index of the first occurrence of an element
lst10=[1, 2, 3, 4, 5]
index=lst10.index(3)
print(index)

#reverse()--> reverses the order of elements in the list
lst11=[1, 2, 3, 4, 5]
lst11.reverse()
print(lst11)

#sort()--> sorts the elements of the list in ascending order
lst12=[5, 2, 3, 1, 4]
lst12.sort()
print(lst12)
