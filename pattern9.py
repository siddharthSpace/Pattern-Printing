rows = 5

for i in range(rows): # upper pyramid range
    for s in range(rows - i - 1): # for printing spaces
        print(" ", end="")
    for j in range(2 * i + 1):# starts printing
        print("*", end=" ")
    print()

for i in range(rows - 1): # lower pyramid 
    for s in range(i + 1): # spaces printing
        print(" ", end="")
    for j in range(2 *(rows - i - 1)- 1): #stars printing in downword
        print("*", end=" ")
    print()