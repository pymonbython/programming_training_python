# CONTEXT MANAGER

my_file = open('text.txt', 'r+')

# for line in my_file:
#     print(line)

# print(line)
# print(my_file)
# print(my_file.closed)
# print('\n')

# with open('text.txt', 'r') as my_file:
#     for line in my_file:
#         print(line)

# print(line)
# print(my_file)
# print(my_file.closed)

# ODCZYTYWANIE PLIKU TEKSTOWEGO

# with open('text.txt') as file:
#     for line in file:
#         print(line.strip())

# print('\n')

# with open('text.txt', encoding='utf-8') as file:
#     print(file.readline())
#     print(file.readline())

# ZAPIS DO PLIKU TEKSTOWEGO

# with open('text.txt', mode='a') as file:
#     note = input('Podaj notatkę: ')
#     file.write(note + '\n')
#     file.writelines(['1', '2', '3', '3'])

# ODCZYT I ZAPIS DO PLIKU JEDNOCZEŚNIE

with open('text.txt') as input_file, open('wynik.txt', 'w') as output_file:
    for line in input_file:
        try:
            value = int(line.strip())
        except Exception:
            continue

        if value % 3 == 0:
            output_file.write(str(value) + '\n')
