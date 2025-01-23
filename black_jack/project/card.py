"""BlackJack ASCII Python game"""

class InvalidColor(Exception):
    """Exception when color is invalid."""


class InvalidValue(Exception):
    """Exception when value is invalid."""


class Card:
    """Card abstraction"""

    possible_colors = {
        'spades': '\u2664',
        'hearts': '\u2661',
        'diamonds': '\u2662',
        'clubs': '\u2667'
    }

    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, color: str, value: str) -> None:
        if color not in self.possible_colors:
            raise InvalidColor('Invalid color!')
        self.color = self.possible_colors[color]
        if value not in self.possible_values:
            raise InvalidValue('Invalid card value!')
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value} -> {self.color}'
