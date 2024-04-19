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
