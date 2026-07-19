'''SET
1, Unordered collection of unique elements
2, Mutable
3, A set is a collection of unique elements that can be modified after creation.
4, Sets are defined using curly braces {} or the set() constructor.
5, Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.'''

set1={'rickson', 9, 5 ,6}
print(type(set1))
print(set1)

set2=set(('rickson', 3, 5, 6))
print(type(set2))
print(set2)

#set operations in python

#1, union()--> comibines two sets and returns a new set with all unique elements from both sets.
a={1, 2, 3}
b={3, 4, 5}
print(a|b)                           #both syntax works for union() method
print(a.union(b))

#2, intersection()--> returns a new set with elements that are common to both sets.
c={1, 2, 3}
d={2, 3, 5}
print(c&d)                           #both syntax works for intersection() method
print(c.intersection(d))

#3, difference()--> returns a new set with elements that are in the first set but not in the second set.
e={1, 2, 3}
f={2, 3, 5}
print(e-f)                           #both syntax works for difference() method
print(e.difference(f))

#4, symmetric_difference()--> returns a new set with elements that are in either of the sets but not in both.
g={1, 2, 3}
h={2, 3, 5}
print(g^h)                           #both syntax works for symmetric_difference() method
print(g.symmetric_difference(h))

#5, membership()--> checks if an element is present in a set and returns True or False.
i={1, 2, 3}
print(5 in i)
print(2 in i)

#subset()--> checks if a set is a subset of another set and returns True or False.
j={1, 2, 3}
k={1, 2, 3, 4, 5}
print(k<=j)                           #both syntax works for subset() method
print(j.issubset(k))

t=(1, 2, 3)
t2=(3, 4, 5)
print(t<t2)