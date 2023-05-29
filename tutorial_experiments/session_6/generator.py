
def reverse(data):
    print('Reverse called')
    for index in range(len(data)-1, -1, -1):
        yield data[index]


s = [1, 2, 3, 4, 5, 6]

for val in reverse(s):
    print(val)


for val in (x*2 for x in s):
    print(val)

