def print_in_box(str):
	print('+--' + ('-' * len(str)) + '+')
	print('|  ' + (' ' * len(str)) + '|')
	print('| ' + str + ' |')
	print('|  ' + (' ' * len(str)) + '|')
	print('+--' + ('-' * len(str)) + '+')
	
print_in_box('')
print_in_box('To boldly go where no one has gone before.')
