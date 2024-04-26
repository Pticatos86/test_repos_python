from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, name, classification, type_of_animals, protective_status, habitat, current_quantity):
        self.name = name
        self.classification = classification
        self.type_of_animals = type_of_animals
        self.__protective_status = protective_status
        self.habitat = habitat
        self.__current_quantity = current_quantity

    def __str__(self):
        return (f"{self.name} {self.__class__.__name__}, belongs to class {self.classification},"
                f" type is {self.type_of_animals}, habitats in {self.habitat},"
                f" protective status is {self.__protective_status}, approximate quantity is {self.__current_quantity}")

    @abstractmethod
    def survive_animals(self) -> str:
        pass

    @property
    def protective_status(self) -> str:
        return self.__protective_status

    @property
    def current_quantity(self) -> int:
        return self.__current_quantity

    @protective_status.setter
    def change_protective_status(self, new_protective_status: str) -> str:
        self.__protective_status = new_protective_status

    @current_quantity.setter
    def change_animals_quantity(self, new_quantity: int) -> int:
        self.__current_quantity = new_quantity

    def protect_animals(self) -> str:
        return (f"animal - {self.name} of class {self.classification}, type {self.type_of_animals} "
                f"that habitats in {self.habitat} is protected by the state")
