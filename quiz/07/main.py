def sum_two_numbers(a:int, b:int) -> int:
    return a + b


# 1. given, 2. when, 3. then
def test_sum_two_numbers():
    # given // Warunki wejściowe (dane wejściowe) Są zadeklarowane wewnątrz funkcji testującej.
    a = 2
    b = 3

    # when // Podejmowana akcja.

    result = sum_two_numbers(a, b)

    # then // Jaki ma być rezultat wykonanej akcji.

    # operator (operator wyrażenie (ture or false)) assert wyrzuca nam błąd, catch łapie wyrzucony błąd. Poniżej wyrzucamy błąd. Jeśli wyrzucony błąd nie zostanie przechwycony przez operator catch, to wówczas interpreter Pyythona zakończy działanie programu, zwracając błąd (drukując w konsoli) wyrzucony przez operator assert.

    assert result == 5
    
# sum_two_numbers(2, 3)

# Pytest (zew. pakiet skryptów Pythona) wyszukuje w ramach danego pliku wszystkie funkcjie z przedrostkiem "test_".

# Moduł Pytest uruchamiamy w terminalu za pomocą komendy python3 -m pytest wskazujemy_ścieżkę_do_pliku
