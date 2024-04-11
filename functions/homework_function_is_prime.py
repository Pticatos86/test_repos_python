"""Solution of task 2"""

number = int(input("Enter number: "))


def is_prime(number: int):
    if number not in range(2, 1001):
        raise ValueError(f"{number} is not a valid number. Please, try any number in range from 2 to 1000.")

    for num in range(2, number + 1):
        if number % num == 0 and num != number:
            return False

    return True


result = is_prime(number)
print(f"Is your number prime?: {result}")
