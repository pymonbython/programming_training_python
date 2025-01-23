"""Card tests"""

import pytest

from card import Card, InvalidColor, InvalidValue

def test_creation():
    """Test if I can create valid card."""
    # given & when
    example_card = Card('hearts', 'Ace')

    # then
    assert example_card.color == chr(ord('\u2661'))
    assert example_card.value == 'Ace'

def test_creation_wrong_value():
    """Test if code raises exception when wrong value."""
    with pytest.raises(InvalidValue) as e:
        # given & when
        Card('hearts', 'A')

        # then
        assert e == 'Invalid card value!'


def test_creation_wrong_color():
    """Test if code raises exception when wrong color."""
    with pytest.raises(InvalidColor) as e:
        # given & when
        Card('xxx', 'Ace')

        # then
        assert e == 'Invalid color!'


def test_card_representation():
    """Test if card has correct card representation."""
    example_card = Card('hearts', 'Ace')

    assert repr(example_card) == f'Ace -> {chr(ord('\u2661'))}'
