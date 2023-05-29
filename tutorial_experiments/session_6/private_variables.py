class Person:
    def __init__(self, first_name, last_name):
        self.__foo = 20
        self.first_name = first_name
        self.last_name = last_name
    def print_name(self):
        print(f'{self.first_name} {self.last_name}')


class Programmer(Person):
    def __init__(self, first_name, last_name, fav_language):
        Person.__init__(self, first_name, last_name)
        self.__foo = 30
        self.fav_language = fav_language
    def print_name_and_language(self):
        print(f'{self.first_name} {self.last_name} loves {self.fav_language}')



x = Person('Koushik', 'Kothagal')
print(x.__dict__)
x = Programmer('Koushik', 'Kothagal', 'Java')
print(x.__dict__)