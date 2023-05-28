# Exercise 2: List Operations

# Create a Python program that has a list of numbers (for example: [5, 10, 15, 20, 25]). The program should do the following:

# Print the list.
# Add a number to the end of the list.
# Remove a number from the list.
# Print the length of the list.
# Print the first item in the list.
# Print the last item in the list.


numberList = [n for n in range(5, 26, 5)]

# Print the list.
print(numberList)

# Add a number to the end of the list.
numberList.append(30)
print(numberList)


# Remove a number from the list.
numberList.remove(25)
print(numberList)

# Print the length of the list.
print(len(numberList))

# Print the first item in the list.
print(numberList[0])

# Print the last item in the list.
print(numberList[-1])
