print("Half pyramid pattern of stars (*):")
n= int(input("Enter the number of rows: "))
for i in range (n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

    #activity 2
rows = int(input("Enter the number of rows: "))
number = 1
print("floyd's triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()

    # activity 3
rowSize = int(input("Enter the number of rows: "))
if rowSize % 2 == 0:
    haflDiamRow = int(rowSize / 2)
else:
    haflDiamRow = int(rowSize / 2) + 1
space = haflDiamRow - 1
for i in range(1, haflDiamRow + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2*i - 1):
        print(end=str(num))
        num = num + 1
    print()
space = 1
# loop lower triangle
for i in range(1, haflDiamRow):
    for j in range(1, space + 1):
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2 * (haflDiamRow - i)):
        print(end=str(num))
        num = num + 1
    print()