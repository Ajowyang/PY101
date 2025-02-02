str = "tHE mUNSTERS ARE CREEPY AND SPOOKY."


print(str.swapcase())

char_set = set(str)
for char in char_set:
    if char == char.lower():
       str =  str.replace(char, char.upper())
    else:
       str =  str.replace(char, char.lower())

print(str)
