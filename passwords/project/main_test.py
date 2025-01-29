from main import HasNumberValidator, HasSpecialCharactersValidator

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
