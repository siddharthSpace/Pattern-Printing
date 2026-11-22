

for i in range(5): #defind rows
    for s in range(5 - i - 1): # for spaces
        print(" ", end="")
    for j in range(2 * i + 1): # odd number stars
        print("*", end=" ")
    print()

