import random
name = input("Enter Name: ")
name = name if name else "Teddy"

print(f'{name} is {random.randint(20, 100)} years old!')
