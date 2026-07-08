"""Create a Python program using at least 10 string methods from the table above and show
their outputs with examples. Try methods like upper(), split(), replace(), find(), and strip().
Take a sentence from the user and perform different string operations on it such as
converting case, counting words, checking digits/alphabet, and replacing words. Print all
results clearly with labels"""

text='rickson aryal'
print(f"Original text: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Stripped: {text.strip()}")
print(f"Split: {text.split()}")
print(f"Replace: {text.replace('rickson', 'Rickson')}")
print(f"Find: {text.find('aryal')}")