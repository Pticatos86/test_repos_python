from OOP_part_3.class_mammals import Mammals


class Predators(Mammals):
    def __init__(self, name, classification, type_of_animals, __protective_status, habitat, __current_quantity):
        super().__init__(name, classification, type_of_animals, __protective_status, habitat, __current_quantity)
