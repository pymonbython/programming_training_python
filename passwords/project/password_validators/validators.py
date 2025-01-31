"""Collection of password validators."""

from abc import ABC, abstractmethod
from hashlib import sha1
from typing import List

import requests


class ValidationError(Exception):
    """Exception for validation error."""


class Validator(ABC):
    """Interface for validators"""
    @abstractmethod
    def __init__(self, string):
        """Force to implement __init__ method with string argument."""

    @abstractmethod
    def validate(self):
        """Force to implement validate method."""


class HaveIBeenPwndValidator(Validator):
    """Validator that checks if password is not leak."""
    def __init__(self, password) -> None:
        self.password = password

    def validate(self) -> bool:
        """Checks if password is valid.

        Raises:
            ValidationError: passsword is not valid because it is present in some leak.

        Returns:
            bool: password is safe.
        """
        hash_of_password = sha1(self.password.encode('utf-8')).hexdigest().upper()
        response = requests.get('https://api.pwnedpasswords.com/range/' + hash_of_password[:5])
        for line in response.text.splitlines():
            found_hash, _ = line.split(':')
            if found_hash == hash_of_password[5:]:
                raise ValidationError('This password is a leaked password! Choose another one!')

        return False


class HasNumberValidator(Validator):
    """Validator checking if string has number."""
    def __init__(self, text: str) -> None:
        self.text = text

    def validate(self) -> bool:
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there is no number in text.

        Returns:
            bool: has number in text.
        """
        for number in range(0, 10):
            if str(number) in self.text:
                return True

        raise ValidationError('Text must contain number!')


class HasSpecialCharactersValidator(Validator):
    """Validator that checks if special character apppears in text."""
    def __init__(self, text:str ) -> None:
        self.text = text

    def validate(self) -> bool:
        """Checks if text is valid.

        Raises:
            ValidationError: text is not valid because there is no special character in text.

        Returns:
            bool: has special character in text.
        """
        if any([not character.isalnum() for character in self.text]):
            return True

        raise ValidationError('Text must contain special characters!')


class HasUpperCharacterValidator(Validator):
    """Validator that checks if at least one upper letter apppears in text."""
    def __init__(self, text) -> None:
        self.text = text

    def validate(self) -> bool:
        """Checks if text is valid.

        Raises:
            ValidationError: text is not valid because there is no at least one upper letter in text.

        Returns:
            bool: has at least one upper letter in text.
        """
        if any([character.isupper() for character in self.text]):
            return True

        raise ValidationError('Text must contain upper letter!')


class HasLowerCharacterValidator(Validator):
    """Validator that checks if at least one lower letter apppears in text."""
    def __init__(self, text) -> None:
        self.text = text

    def validate(self) -> bool:
        """Checks if text is valid.

        Raises:
            ValidationError: text is not valid because there is no at least one lower letter in text.

        Returns:
            bool: has at least one lower letter in text.
        """
        if any([character.islower() for character in self.text]):
            return True

        raise ValidationError('Text must contain lower letter!')


class LengthValidator(Validator):
    """Validator that checks if password is lenght enough;"""
    def __init__(self, text, min_length: int = 8) -> None:
        self.text = text
        self.min_length = min_length

    def validate(self) -> bool:
        """Checks if text is valid.

        Raises:
            ValidationError: text is not valid because it is to short.

        Returns:
            bool: text is long enough.
        """
        if len(self.text) >= self.min_length:
            return True

        raise ValidationError('Text is too short!')


class PasswordValidator(Validator):
    """Validator that checks if password is safe."""
    def __init__(self, password: str) -> None:
        self.password: str = password
        self.validators: List = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharactersValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIBeenPwndValidator
        ]

    def validate(self) -> bool:
        """Checls if password is valid.

        Returns:
            bool: returns True if password passed all password validation requirements.
        """
        for validator in self.validators:
            validator = validator(self.password)
            validator.validate()

        return True
