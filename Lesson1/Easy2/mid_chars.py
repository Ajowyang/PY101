def center_of(str):
	
	if len(str) % 2 == 1:
		return str[len(str) // 2 ]
	else:
		return str[len(str) // 2 - 1 : len(str) // 2 + 1]

print(center_of('I Love Python!!!'))    # True
print(center_of('Launch School'))        # True
print(center_of('Launchschool'))        # True
print(center_of('Launch'))              # True
print(center_of('Launch School is #1'))  # True
print(center_of('x'))                    # True
