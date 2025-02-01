def get_suffix(num):
	str_num = str(num)
	last_two = num % 100
	match last_two:
		case 11 | 12 | 13:
			return 'th'
	match str_num[-1]:
		case '1':
			return 'st'
		case '2':
			return 'nd'
		case '3':
			return 'rd'
		case _:
			return 'th'

def century(yr):
	century = yr // 100
	if yr % 100 >= 1:
		century += 1
	
	result = str(century) + get_suffix(century)
	return result

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

