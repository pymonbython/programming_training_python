# def say_hello(first_name='Name'):
#     return f'Hello {first_name}'

# say_hello_to_name = say_hello('Name')

# print(say_hello_to_name)

# say_hello = lambda first_name='Name': f'Hello {first_name}'

# say_hello_to_name = say_hello()

# print(say_hello_to_name)
# names = ['Alina', 'Name']

# names_starts_with_a = filter(lambda name: name[0].lower() == 'a', names)
# print(list(names_starts_with_a))

# lista = filter(lambda number: number%2, [1, 2, 3, 4, 5, 6, 7])
# print(list(lista))


# class Person:
#     pass


# class Alan(Person):
#     pass

# from typing import Union


# def foo(x: Union[int, float]):
#     pass

# foo(5)
# foo(5.5)


def suma(a, b, *args):
    print(args)
    return a + b

# wynik = suma(2, 4)
# print(wynik)

# wynik = suma(b=2, a=4)
# print(wynik)

# filter_even('1','2','3','4','5','6','7','8','9')
# wynik = suma(2, 4, 5, 6, 7, 8)
# print(wynik)

def filter_even(*args):
    evens = filter(lambda number: int(number)%2 == 0, args)
    print(list(evens))

# filter_even(*'1,2,3,4,5,6,7,8,9'.split(','))


def foo2(*args, name = 'Name'):
    print(args)
    print(name)

# foo2(2, 3, 4, name='Name2')

def foo3(*args, **kwargs):
    print(args)
    print(kwargs)

# foo3(1,2,3,4,5, name='Name', surname='Surname')


class User:
    def __init__(self, name):
        self.name = name
        # self.age = 34

user = User('Name')

# print(user.name)
# print(getattr(user, 'name'))

def foo4(filed_name):
    print(getattr(user, filed_name, None))

# filed_name = input('Filed name? ')
# foo4(filed_name)

fruits = ['lemon', 'orange', 'apple', 'peach']
length = [len(fruit) for fruit in fruits]

# print(length)

# length = map(lambda fruit: len(fruit), fruits)

# print(*length)

sorted_fruits = sorted(fruits, key=len, reverse=True)
# print(sorted_fruits)


def do_something(name, surname, foo=None):
    print(name, surname)
    foo(name)

def foo6(name, surname):
    print(name + '--*--' +surname)

# do_something('Name', 'Surname', foo6)
# do_something('name', 'surname')


# do_something('name', 'surname', foo=lambda name: name+ 's')

from enum import Enum
from enum import IntEnum, auto

class Move(Enum):
    UP = auto()
    DOWN = 2
    LEFT = 'string'
    RIGHT = 4

# for n in Move:
#     print(n.value)

def add_numbers(a, b):
    return a +b 

val1 = 3
val2 = 4

action = 'dodaj'

action_mapper = {
    'dodaj': add_numbers,
    'odejmij': lambda a, b: a -b,
    'pomnóż': lambda a, b: a * b,
    'podziel': lambda a, b: a /b
}


print(action_mapper[action](val1, val2))


