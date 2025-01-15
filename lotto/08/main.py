
# Module docstring
"""
Moduł matematyczny operacji dodawania dwóch liczb.

Ten moduł zawiera funkcję sumującą dwie liczby.

Przykład:
    my_sum(2, 3) -> 5

Autor: Szymurai
"""

def my_sum(number1, number2):
    #  Function docstring
    """Sum given numbers

    Args:
        number1 (int): first number to sum
        number2 (int): second number to sum

    Returns:
        int: sum of two given numbers
    """
    return number1 + number2

SCORE = my_sum(2, 3)

print(SCORE)
