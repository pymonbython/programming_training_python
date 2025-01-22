class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        return f'Hi! My name is {self.first_name} {self.last_name}'


class InvalidSemestr(Exception):
    pass


class Student(Person):
    def __init__(self, first_name, last_name, semester):
        super().__init__(first_name, last_name)
        self.semester = semester
    
    def promote(self):
        self.semester +=1 

    def degrade(self):
        if self.semester == 1:
            raise InvalidSemestr('Student jest na 1. semestrze.')
        
        self.semester -= 1


class Worker(Person):
    def __init__(self, first_name, last_name, hourly_rate):
        super().__init__(first_name, last_name)
        self.hourly_rate = hourly_rate
        self.time = 0

    def register_time(self, time):
        self.time += time

    def get_paid(self):
        time = self.time
        self.time = 0
        return time * self.hourly_rate

try:
    antek = Student('Anthony', 'x', 1)
    antek.degrade()
    print(antek.semester)
except InvalidSemestr as e:
    print(e)
