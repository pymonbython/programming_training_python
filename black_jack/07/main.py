# a = input('Podaj liczbę A: ')
# b = input('Podaj liczbę B: ')

# try:
#     result = int(a) / int(b)
#     print('Wynik to: ' + result)
# except (ValueError, ZeroDivisionError):
#     print('Podaj tylko liczbę int().')
# except ZeroDivisionError:
#     print('Nie można dzielić przez 0.')

# a = []
# b = {}

# try:
#     print(a[3])
#     print(b['dwa'])
# except (KeyError, IndexError):
#     print('Taka wartość nie istnieje.')



try:
    print('Try block.')
    raise ValueError
    print('Try block 2.')
except ValueError:
    print('Łapiemy error.')
finally:
    print('Finally block.')
