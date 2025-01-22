class Student:
    def __init__(self, name):
        self.imię = name
        self.semestr =1
        print('Gratuluję! Stworzyłeś nowego studenta o imieniu: ' + self.imię)


    def say_hello(self):
        print(f'Hello my name is: {self.imię}')
        print(f'I am on {self.semestr} semester')

    
    def promote(self):
        if self.semestr > 9:
            print('You are graduated.')
        else:
            self.semestr += 1

# student = Student('Baśka')
# student.say_hello()


class Person:
    name = 'Coś'
    surname = "Coś innego"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print(name)

    @staticmethod
    def print_name(person):
        print(person.name, person.surname)

# person = Person("test", "test2")
# person.name = "Coś zupełnie innego."
# print(person.name)
# person.print_name(person)

class Product:
    def __init__(self, name, netto, vat):
        self.name = name
        self.netto = netto
        self.vat = vat


    def calc_brutto(self):
        return self.netto + self.netto * self.vat
    

bread = Product('Bread', 4, .23)
# print(bread.calc_brutto())


class Aquarium:
    def __init__(self, width, height, depth) -> None:
        self.capacity = self._count_capacity(width, height, depth)


    
    def __str__(self):
        return f'Jestem studentem jestem {str(self.capacity)}'


    @staticmethod
    def _count_capacity(width, height, depth):
        return width * height * depth


aquarium = Aquarium(100, 80, 40)

# print(aquarium.capacity)
# print(aquarium)
# print(str(aquarium))

aquarium_2= Aquarium(10, 20, 30)
print(aquarium_2._count_capacity(10, 40, 50))

