def sum_numbers(a, b):
    print(f'Suma wynosi: {a + b}')
    # return a + b


def calculate_brutto(netto, vat=0.23):
    return netto * vat + netto


print(calculate_brutto(100))

zmienna = calculate_brutto(100)
