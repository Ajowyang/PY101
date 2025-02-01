def short_long_short(str1, str2):
	short = (str1 if len(str1) < len(str2) else str2)
	long = (str1 if len(str1) > len(str2) else str2)
	return short + long + short

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
