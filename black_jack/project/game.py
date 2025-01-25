from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print('Co chcesz zrobić?')
        print('[0] - dobieram kartę')
        print('[1] - pasuję')
        return input('...: ')

    def _get_card(self, user):
        card = self.deck.hit()
        user.take_card(card)
        
    def _user_plays(self):
        user = Player()
        for _ in range(2):
            self._get_card(user)

        while True:
            print(user.cards)
            print(user.calculate_points())

            choice = self._print_menu()

            if choice == '0':
                self._get_card(user)
            elif choice == '1':
                return user.calculate_points()
            else:
                print('Dokonanie nieprawdiłowego wyboru.')

    def _croupier_playes(self, user_points):
        croupier = Player()
        while croupier.calculate_points() < user_points:
            croupier.take_card(self.deck.hit())

        print('Croupier points: ' + str(croupier.calculate_points()))
        return croupier.calculate_points()


    def play(self):
        try:
            user_points = self._user_plays()
        except GameOverException as e:
            raise GameOverUserException from e
        try:
            croupier_points = self._croupier_playes(user_points)
        except GameOverException as e:
            raise GameOverCroupierException from e
        
        print(f'Koniec gry, wygrana croupiera. Croupier points: {croupier_points}. User points: {user_points}.')
