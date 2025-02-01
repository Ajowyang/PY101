import datetime

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

year = datetime.date.today().year

print(f"It's {year}. You will retire in {year + (retire_age - age)}.")
print(f"You only have {retire_age - age} years of work to go!" )

