from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    @abstractmethod
    def validate():
        pass

class Validator(ValidatorInterface):
    # system spełniania wymagań
    # tworzenie zestawu wymaganych metod, które ktoś inny musi zaimplementować w swojej klasie by być zgodny z naszmi wymaganiami.
    def validate():
        pass

validator = Validator()

