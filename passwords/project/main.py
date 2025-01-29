from abc import ABC, abstractmethod
from typing import List


class Validator(ABC):
    @abstractmethod
    def __init__(self, string):
        pass

    @abstractmethod
    def validate():
        pass


class HaveIBeenPwndValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text
        self.is_valid = None

        self.validate(self.text)

    def validate(self, text: str = None) -> bool:
        pass


class HasLowerCharacterValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text
        self.is_valid = None

        self.validate(self.text)

    def validate(self, text: str = None) -> bool:
        pass


class HasUpperCharacterValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text
        self.is_valid = None

        self.validate(self.text)

    def validate(self, text: str = None) -> bool:
        pass


class HasNumberValidator(Validator):
    def __init__(self, text: str) -> None:
        self.text = text

    def validate(self) -> bool:
        for n in range(0, 10):
            if str(n) in self.text:
                return True
            
        return False


class HasSpecialCharactersValidator(Validator):
    def __init__(self, text:str ) -> None:
        self.text = text

    def validate(self) -> bool:
        temp_list = []
        for character in self.text:
            temp_list.append(not character.isalnum())
            # if not character.isalnum():
            #     return True
        
        print('ok')


class LengthValidator(Validator):
    def __init__(self, text) -> None:
        self.text = text

    def validate(self) -> bool:
        pass


class PasswordValidator(Validator):
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

    def validate(self, password: str = None) -> bool:
        for validator in self.validators:
            validator_obj = validator(self.password)
            validator_obj.validate()


# validator = PasswordValidator('abrakadabra')
