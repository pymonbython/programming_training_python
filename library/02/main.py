# with open('text.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)


# class MyContextManager:
#     def __init__(self):
#         print('in init')

#     def __enter__(self):
#         print('in enter')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('in exit')
#         print(exc_val)
#         print(exc_tb)
#         print(exc_type)


# with MyContextManager() as my_context:
#     print(my_context)
#     print('do job')
#     raise KeyError('Test text')

# f = open('text.txt')

# lines =f.readlines()
# print(lines)

# f.close()

class MyContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.f = None

    def __enter__(self):
        self.f = open(self.file_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with MyContextManager('text.txt') as f:
    lines = f.f.readlines()
    print(lines)
