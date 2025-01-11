#  Słowo kluczowe "witch" otwiera nam nowy kontekst, w - write, a - append, r - read.
with open('filename.txt', 'a') as file:
    text = input('Dodaj notatkę: ')
    int = file.write(f'{text}\n')
    print(int)
    # print(len('Szymon Szymurai\n'))

