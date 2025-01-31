import pytest

from main import (
    HasNumberValidator,
    HasSpecialCharactersValidator,
    HasLowerCharacterValidator,
    HasUpperCharacterValidator,
    LengthValidator,
    HaveIBeenPwndValidator,
    PasswordValidator,
    ValidationError
)


def test_password_validator_positive():
    validator = PasswordValidator('test8899#A')
    assert validator.validate() is True


# def test_password_validator():
#     validator = PasswordValidator('test8899#')
#     with pytest.raises(ValidationError) as e:
#         validator.validate()
#         assert 'Text must contain upper letter!' in str(e.value)
    

def test_have_i_been_pwnd_validator(requests_mock):
    response = '0522362627E12FA5332B9BB7046BF3073B2:6\n07E1AF8698EFAA439006310FDD573D63362:3'
    requests_mock.get('https://api.pwnedpasswords.com/range/CEBF1', text=response)
    validator = HaveIBeenPwndValidator('abrakadabra2')
    assert validator.validate() is False


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
