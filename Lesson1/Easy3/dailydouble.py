def crunch(str):
	result = str[0] if str else ''
	for i in range(1, len(str)):
		if result[len(result) - 1] != str[i]:
			result += str[i]
	return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
