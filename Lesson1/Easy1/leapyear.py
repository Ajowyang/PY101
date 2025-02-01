def is_leap_year(yr):
	if yr < 1752:
		return (yr % 4 == 0)

	elif yr >= 1752:
		if yr % 400 == 0:
			return True
		elif yr % 100 == 0 and yr % 400 != 0:
			return False
		elif yr % 4 == 0 and yr % 100 != 0:
			return True
		else:
			return False

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
