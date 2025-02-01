num = int(input('Please enter an integer greater than 0: '))
sum_or_prod = input('Enter "s" to compute the sum, or "p" to compute the product. ')

def compute_sum(n):
	result = 0
	for i in range(1, n + 1):
		result += i
	return result
def compute_prod(n):
	result = 1
	for i in range (1, n + 1):
		result *= i
	return result

positive = (True if num > 0 else False)

if sum_or_prod == 's' and positive:
	print(f'The sum of the integers between 1 and {num} is {compute_sum(num)}.')
elif sum_or_prod == 'p' and positive:
	print(f'The product of the integers between 1 and {num} is {compute_prod(num)}.')
else:
	print('Error! Unknown operation or negative number!')
