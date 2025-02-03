title = "Flintstone Family Members"
print(title.center(40))

numspaces = (40 - len(title)) // 2
if numspaces > 0:
    title = (" " * numspaces) + title + (" " * numspaces) 

print(title)
