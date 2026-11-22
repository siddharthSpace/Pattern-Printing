# Question 3: Inverted Right-Angled Triangle
# Expected output:

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()