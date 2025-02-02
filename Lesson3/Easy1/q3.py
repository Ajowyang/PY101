famous_words = "seven years ago..."

result1 = "Four score and " + famous_words

def prepend_to_str(str1, str2):
	return str1 + str2

result2 = prepend_to_str("Four score and ", famous_words)

result3 = print(f"Four score and {famous_words}")

print(result1)
print(result2)
