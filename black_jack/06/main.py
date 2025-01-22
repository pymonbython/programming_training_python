# class Car:
#     def __init__(self, brand, capacity) -> None:
#         self.brand = brand
#         self.engine = self.Engine(capacity)

    

#     class Engine:
#         def __init__(self, capacity) -> None:
#             self.capacity = capacity


# car = Car('Honda', 2.2)


class Student:
    def __init__(self, first_name, last_name, semester):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester

    # String
    def __str__(self):
        return f'My name is {self.first_name} and I\'m a student on {self.semester}. semester.'
    
    # Reperezentacja
    def __repr__(self):
        return f'Student: #{self.first_name}'

    
    def __eq__(self, value):
        return all([
            self.first_name == value.first_name,
            self.last_name == value.last_name,
            self.semester == value.semester
        ])


baska = Student('Barbara', 'B', 4)
barbara = Student('Barbara', 'B', 4)
# john = Student('John')

# students = [baska, john]

# print(students)
print(baska == barbara)
