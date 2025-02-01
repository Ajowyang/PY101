def multisum(num):
	result = 0
	for i in range(1, num + 1):
		if i % 5 == 0 or i % 3 == 0:
			result += i
			
	return result

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
