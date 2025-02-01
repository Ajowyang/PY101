def greetings(list, dict):
	name =" ".join(list)
	print(dict.get('title'))
	return f'Hello, {name}! Nice to have a {dict.get("title")} {dict.get("occupation")} around.'


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
