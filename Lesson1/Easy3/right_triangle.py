def triangle(num):
	for i in range(0, num):
		num_spaces = num - (i + 1)
		num_stars = i + 1
		print(" " * num_spaces + "*" * num_stars)

triangle(5)
triangle(9)

