str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def last_char_exclam(str):
    if str[len(str) - 1] == "!":
        return True
    return False

print(last_char_exclam(str1))
print(last_char_exclam(str2))
