numbers = [1, 2, 3, 4, 3, 1, 7, 10, 17, 12]

numbers.sort() # What is the arg to sort?

# print(numbers)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for what_is_this in knights.items():
    print(type(what_is_this))

for tup in enumerate(['1', '2', '3']):
    print(type(tup))

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for val in zip(questions, answers):
    print(type(val))

# print(reversed(questions))
# print(questions)

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

filtered_data = [n for n in raw_data if not math.isnan(n)]

# print(filtered_data)

print((1, (1, 2)) < (1, 2))