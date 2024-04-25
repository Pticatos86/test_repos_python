from OOP_part_3.class_animals import Animals


class Mammals(Animals):

    def __init__(self, name, classification, type_of_animals, __protective_status, habitat, __current_quantity):
        super().__init__(name, classification, type_of_animals, __protective_status, habitat, __current_quantity)

    def survive_animals(self):
        return f"I survive like {self.__class__.__name__}"
