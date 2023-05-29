from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    def print(self):
        print(f'Hello, {self.first_name}')

x = Person('Koushik', 'Kothagal', 40)

x.first_name = 'Foo'
print(x)
x.print()


