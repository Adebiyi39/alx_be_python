# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Intialized row counter
row = 0

# Draw the pattern
while row < size:
    # print each row using a for loop
    for _ in range (size):
        print("*", end="")
        print() # Move to the next line
        row += 1

