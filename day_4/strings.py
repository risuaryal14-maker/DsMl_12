"""STRINGS
- Strings are a sequence of characters enclosed in single or double quotes.
- Strings are immutable, meaning they cannot be changed after they are created.
"""
text= 'rickson'
print(type(text)
)
#indexing is used to access individual characters in a string.
text2= 'rickson' 
print(text[2]) 

#slice() method is used to extract a portion of a string.
text3= 'rickson'
print(text3[0:-2])

#print() method is used to print the output to the console.
text4= 'my name is rickson aryal'
print(text4)

#replace() method is used to replace a substring with another substring in a string.
text5= 'I hate myself.'
print(text5.replace('hate','love'))

#concatenation is used to combine two or more strings into a single string.
print(text4+", "+text5)

