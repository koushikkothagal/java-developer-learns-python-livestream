squares = []

for x in range(10):
    squares.append(x**2)

# print(squares)

# print(list(map(lambda x: x + 1, [2, 3, 4])))

def foo(x):
    return x**2

# print([[x, x+1] for x in range(10)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

