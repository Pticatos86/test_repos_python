from modules_and_packages.utils import validate_datatype


def convert_celsius_to_fahrenheit(value_celsius: int) -> float:
    validate_value = validate_datatype(value_celsius, int)
    return ((validate_value * 9) / 5) + 32


def convert_fahrenheit_to_celsius(value_fahrenheit: int) -> float:
    validate_value = validate_datatype(value_fahrenheit, int)
    return ((validate_value - 32) * 5) / 9


def add_num(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def minus_num(num_1: int, num_2: int) -> int:
    return num_1 - num_2


def multiply_num(num_1: int, num_2: int) -> int:
    return num_1 * num_2


def divide_num(num_1: int, num_2: int):
    if num_2 != 0:
        return num_1 / num_2
    else:
        raise ValueError("Division by zero prohibited")


def convert_temp(value_temp: int, unit_temp='F' or 'C') -> float:
    """

    :param value_temp: integer value temperature
    :param unit_temp: you need to enter unit temperature: Fahrenheit ('F') or Celsius ('C') for your value temperature
    :return: result of converting specified parameters
    """

    if unit_temp == 'C':
        return convert_celsius_to_fahrenheit(value_temp)

    elif unit_temp == 'F':
        return convert_fahrenheit_to_celsius(value_temp)
    else:
        raise ValueError("Invalid value, you need enter unit temp value 'F' or 'C'")
