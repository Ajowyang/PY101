def is_color_valid(color):
    return True if color == "blue" or color == "green" else False

#or we could go
#return color == "blue" or color == "green"
#return color in ["blue", "green"]    

print(is_color_valid("green"))
print(is_color_valid("red"))
