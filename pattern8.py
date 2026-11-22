

for i in range(5): # defined range 
    for s in range(i): # for spaces
        print(" ", end="")
    for j in range(2 *(rows-i)-1): #odd number star printing
        print("*", end="")
    print()