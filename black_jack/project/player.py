from card import Card
from exceptions import GameOverException

class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card: Card):
        self.cards.append(card)

    def calculate_points(self):
        points = 0

        # How many acers do we have?
        number_of_aces = len([card for card in self.cards if card.value == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            points = 10        

        # for card in self.cards:
        #     try:
        #         points += int(card.value)
        #     except ValueError:
        #         points += 10

        for card in self.cards:
            if card.value == 'Ace':
                points += 1
            elif card.value in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += int(card.value)

        if points > 21:
            raise GameOverException('Number of points exceeded.')

        return points
