class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def print_name(self):
        print(f'{self.first_name} {self.last_name}')

class Programmer(Person):
    def __init__(self, first_name, last_name, fav_language):
        Person.__init__(self, first_name, last_name)
        self.fav_language = fav_language
    def print_name_and_language(self):
        print(f'{self.first_name} {self.last_name} loves {self.fav_language}')


x = Programmer('Koushik', 'Kothagal', 'Java')
x.print_name_and_language() # Calls method of the derived class
x.print_name() # Resolves to the parent class

print(f'Is class type? {isinstance(x, Programmer)}')
print(f'Is subclass? {issubclass(Programmer, Person)}')


