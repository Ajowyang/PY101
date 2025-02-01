num1 = float(input("Enter the first number: "))
num2 = float(input("enter the second number: "))

def arith(num1, num2):
	print(f'{num1} + {num2} = {num1 + num2}')
	print(f'{num1} - {num2} = {num1 - num2}')
	print(f'{num1} * {num2} = {num1 * num2}')
	print(f'{num1} / {num2} = {num1 / num2}')
	print(f'{num1} // {num2} = {num1 // num2}')
	print(f'{num1} % {num2} = {num1 % num2}')
	print(f'{num1} ** {num2} = {num1 ** num2}')
arith(num1, num2)
