"""Solution of task 2"""
from Modules_and_packages.mathematics_function import min_fn, max_fn

if __name__ == '__main__':
    test_min = min_fn(100, 25, 0, -10)
    print(f"Minimal value is {test_min}")

    test_max = max_fn(200, -300, 400, 5000)
    print(f"Maximal value is {test_max}")

"""Solution of task 1"""


class MafiaCompany:
    def __init__(self, name_restaurant, city_restaurant, restaurant_address, restaurant_cuisine,
                 restaurant_services, schedule, contacts):
        self.name_restaurant = name_restaurant
        self.city_restaurant = city_restaurant
        self.restaurant_address = restaurant_address
        self.restaurant_cuisine = restaurant_cuisine
        self.restaurant_services = restaurant_services
        self.schedule = schedule
        self.contacts = contacts

    def invite(self):
        return (
            f"Our family restaurant {self.name_restaurant} invites you to visit us at address {self.city_restaurant},\n"
            f"{self.restaurant_address} in hours {self.schedule}")

    def delivery(self):
        return (f"Our family restaurant {self.name_restaurant} offers you next services: {self.restaurant_services}.\n"
                f"Our contacts is {self.contacts}")


class MafiaEmployee:
    def __init__(self, department, job_title, name, surname, age, salary):
        self._department = department
        self._job_title = job_title
        self._name = name
        self._surname = surname
        self._age = age
        self.__salary = salary
        self.__bonus = 10

    def __str__(self):
        return (f"{self.__class__.__name__} worker: works in {self._department} department, "
                f"job title is {self._job_title}, name is {self._name}, surname is {self._surname}, "
                f"age is {self._age}")

    def __add__(self):
        return self

    @property
    def department(self) -> str:
        return self._department

    @property
    def job_title(self) -> str:
        return self._job_title

    @property
    def name(self) -> str:
        return self._name

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def age(self) -> int:
        return self._age

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def change_salary(self, new_salary: int) -> int:
        if not isinstance(new_salary, int):
            raise ValueError("New salary should contains integer")
        self.__salary = new_salary

    @surname.setter
    def change_surname(self, new_surname: str) -> str:
        if not new_surname.isalpha():
            raise ValueError("Name should contains only letters")
        self._surname = new_surname

    def __calculate_bonus(self) -> int:
        return self.__salary * self.__bonus // 100

    def calculate_salary(self) -> int:
        return self.__salary + self.__calculate_bonus()


if __name__ == '__main__':
    restaurant_one = MafiaCompany('restaurant_one', 'Kyiv',
                                  "Bogdan Khmelnitsky street 27/1",
                                  "Italian and Japanese cuisine",
                                  "food delivery, organization of birthdays and holidays, "
                                  "service-'-50% I will pick it myself'",
                                  '10.00 - 22.00', '+380968888888')
    restaurant_two = MafiaCompany('restaurant_two', 'Dnipro',
                                  "Volodymyr Monomakh street 2 K",
                                  "Italian and Japanese cuisine",
                                  "food delivery, organization of birthdays and holidays,"
                                  "service-'-50% I will pick it myself'",
                                  '10.00 - 22.00', '+380967777777')
    print(f"Greeting to our guests - {restaurant_one.invite()}")
    print(f"Greeting to our guests - {restaurant_two.invite()}")

    print(f"Additional proposition to our guests - {restaurant_one.delivery()}")
    print(f"Additional proposition to our guests - {restaurant_two.delivery()}")
