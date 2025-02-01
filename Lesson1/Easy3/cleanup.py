def clean_up(str):
	result = ''
	for i in range(0, len(str)):
		if str[i].isalpha():
			result += str[i]
		else:
			if not result or result[len(result) - 1] != " ":
				result += " "
	return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
