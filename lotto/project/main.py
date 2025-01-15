"""Totolotek symulation

Returns:
    float: how many money have you spend to win in Totolotek.
"""

import random

my_numbers = set([9, 13, 21, 7, 3])
all_possible_numbers = range(1, 50)
PRICE = 3


def draw_numbers(range_of_numbers: range) -> set:
    """Draw random 6 numbers from array of possible numbers.

    Returns:
        set: collection with 6 different numbers from range 1 to 49.
    """
    return set(random.sample(list(range_of_numbers), k=6))


def play_unitl_you_win(numbers: set, draw_ai_numbers) -> float:
    """Keep drawing random collections of numbers until you win.

    Args:
        numbers (set): collection of user choice numbers.
        draw_ai_numbers (function): algorithm responsible for drawing ai numbers.

    Returns:
        int: number of attempts to win.
    """
    if not isinstance(draw_ai_numbers, set):
        draw_ai_numbers = set(draw_ai_numbers)

    ai_numbers = draw_ai_numbers(all_possible_numbers)
    counter = 1

    while numbers != ai_numbers:
        ai_numbers = draw_ai_numbers(all_possible_numbers)
        counter += 1

    return counter


if __name__ == '__main__':
    COUNTER = play_unitl_you_win(my_numbers, draw_numbers)
    TOTAL_PRICE = COUNTER * PRICE
    print(f'{TOTAL_PRICE:,}' + ' zł')
