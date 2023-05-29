class MyStudentNames:
    def __init__(self, list):
        self.names = list
        self.index = len(list)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index = self.index - 1
            return self.names[self.index]


s = [1, 2, 3, 4, 5, 6]
obj = MyStudentNames(s)

iterator_obj = iter(obj)

for val in obj:
    print(val)


