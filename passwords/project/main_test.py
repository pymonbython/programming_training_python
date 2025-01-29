from main import (
    HasNumberValidator,
    HasSpecialCharactersValidator,
    HasLowerCharacterValidator,
    HasUpperCharacterValidator,
    LengthValidator
)

def test_if_has_number_validator():
    # given
    positive_validator = HasNumberValidator('abrakadabra2')

    # when
    is_valid = positive_validator.validate()

    # 
    assert is_valid is True

def test_if_has_special_character_validator():
    # given
    positive_validator = HasSpecialCharactersValidator('abrakadabra2!$')

    # when
    is_valid = positive_validator.validate()

    # 
    assert is_valid is True

def test_if_has_upper_character_validator():
    # given
    positive_validator = HasUpperCharacterValidator('Abrakadabra2!$')

    # when
    is_valid = positive_validator.validate()

    # 
    assert is_valid is True

def test_if_has_lower_character_validator():
    # given
    positive_validator = HasLowerCharacterValidator('abraKadabra2!$')

    # when
    is_valid = positive_validator.validate()

    # 
    assert is_valid is True

def test_if_has_correct_length_validator():
    # given
    positive_validator = LengthValidator('abraKadabra2!$', 8)

    # when
    is_valid = positive_validator.validate()

    # 
    assert is_valid is True
