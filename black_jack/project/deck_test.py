from deck import Deck
from card import Card

def test_creation():
    # when
    deck = Deck()

    # then
    assert len(deck.cards) == 52


def test_deck():
    # when
    my_deck = Deck()
    cards = [(card.value, card.color) for card in my_deck.cards]

    for color_value in Card.possible_colors.values():
        cards_in_color = [card for card in cards if card[1] == color_value]
        assert len(cards_in_color) == 13


def test_shuffle():
    my_deck = Deck()
    cards = my_deck.cards[:]
    my_deck.shuffle()
    shuffle_cards = my_deck.cards

    assert cards != shuffle_cards


def test_deck_hit():
    my_deck = Deck()
    last_card = my_deck.cards[-1]
    hitted_card = my_deck.hit()

    assert last_card == hitted_card


def test_deck_count_cards():
    my_deck = Deck()
    deck_len = len(my_deck.cards)
    hitted_card = my_deck.hit()
    new_deck_len = len(my_deck.cards)

    assert deck_len - 1 == new_deck_len
    assert hitted_card not in my_deck.cards
