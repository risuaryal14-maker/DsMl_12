''' ----DICTONARIES IN PYTHON----"""
1, Using curly brackets: The dictionaries are created by
enclosing the comma-separated Key: Value pairs inside the
{} curly brackets. The colon ":" is used to separate the key
and value in a pair.

2, Using dict() constructor: Create a dictionary by passing the
comma-separated key: value pairs inside the dict().

3, Using sequence having each item as a pair (key-value'''


'''----key values and pairs rules----
1, Values can be any type.
2, Multiples key can have the same value.
3, keys must be unique.
4, keys don't need to be string'''

## create a dictionary using dict{}
print(1)
dict1={'name':'rickson', 'college':'islington','num':9800000000}
print(dict1)

# create a dictionary using dict()
print(2)
person=dict({'name':'risu', 'address':'kathmandu', 'house.no':3480})
print(person)

# create a dictionary from sequence having each item as a pair
print(3)
person2=dict([('name','rickson'),('college','islington'),('address','nepal')])
print(person2)

#create dictionary with value as a list
print(4)
person3={'name':'rickson', 'telephone':[980000001, 9800000002, 9800000003]}
print(person3)

# access value using key name in []
print(4)
dict2={'name':'rickson', 'college':'islington','num':9800000000}
print(dict2['name'])

# get key value using key name in get()
print(5)
dict3={'name':'rickson', 'college':'islington','num':9800000000}
print(dict3.get('num'))

# Modifying Element--> Change a dictionary value by using its key and assigning a new value.
print(6)
dict4={'name':'rickson', 'college':'islington','num':9800000000}
dict4['num']=9765432101
print(dict4)
print(dict4.get('num'))




