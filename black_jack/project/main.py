from game import Game
from exceptions import GameOverUserException, GameOverCroupierException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('Wygrana gracza!')
except GameOverUserException:
    print('Wygrana croupiera!')