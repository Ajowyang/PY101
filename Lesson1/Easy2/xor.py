def xor(a, b):
	if (not a) and b:
		return True
	elif (not b) and a:
		return True
	else:
		return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
