from OOP_part_3.class_mammals import Mammals
from OOP_part_3.class_predators import Predators

if __name__ == '__main__':
    brown_bear = Predators('brown bear', 'mammals', 'predator',
                           'endangered species', 'Carpathian region', 300)

    long_eared_hedgehog = Mammals('long_eared_hedgehog', 'mammals', 'chordates',
                                  "endangered species", "steppes of Lugansk and Donetsk regions",
                                  20)

    print(f"Description of animal - {brown_bear}")

    print(f"Description of animal - {long_eared_hedgehog}")

    print(f"Implementation of abstractmethod is {long_eared_hedgehog.survive_animals()}")

    brown_bear.change_animals_quantity = 100

    print(f"Number of {brown_bear.name} has decreased. Current quantity is {brown_bear.current_quantity}")

    print(f"Protection animals: {brown_bear.protect_animals()}")


