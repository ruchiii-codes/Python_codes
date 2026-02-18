rows = [3, 4, 3]
i = 0

while i < len(rows):
    j = 0
    while j < rows[i]:
        print("*", end="")
        j += 1
    print()
    i += 1