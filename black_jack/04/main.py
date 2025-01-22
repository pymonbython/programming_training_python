class Person:
    def __init__(self, name) -> None:
        self.imię = name

person = Person('Persona')

print(type(person))
print(person.imię)
