"""Solution of task 1"""
from modules_and_packages.mathematics_function import add_num, minus_num, multiply_num, divide_num
from modules_and_packages.utils import validate_datatype, check_user_operation


def calculate_numbers(num_1, num_2, operation):
    if operation == '+':
        result = add_num(num_1, num_2)
    elif operation == '-':
        result = minus_num(num_1, num_2)
    elif operation == '*':
        result = multiply_num(num_1, num_2)
    elif operation == '/':
        result = divide_num(num_1, num_2)

    else:
        raise ValueError("Incorrect operation")

    return result


def run_calculator(number_one, number_two, operation):
    operation = check_user_operation(operation)
    number_one = validate_datatype(number_one, int)
    number_two = validate_datatype(number_two, int)
    run_result = calculate_numbers(number_one, number_two, operation)

    return run_result


# run program
user_operation = input("Please, choose and enter one of the following symbols (+, -, *, /): ")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

finish_result = run_calculator(number_1, number_2, user_operation)
print(f'You result is {finish_result}')
