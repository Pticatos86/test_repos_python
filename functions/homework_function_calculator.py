"""Solution of task 1"""


def check_user_operation():
    user_message = input("Please, choose and enter one of the following symbols (+, -, *, /): ")
    correct_symbols = ['+', '-', '*', '/']

    while user_message not in correct_symbols:
        print("You entered incorrect symbols.Try again: ")

        user_message = input("Please, choose and enter one of the following symbols (+, -, *, /): ")

    else:
        print(f"You entered operation is {user_message}")

    return user_message


def check_correct_input_num_one():
    while True:
        number_one = input('Please, enter your first number: ')
        try:
            checked_number_one = float(number_one)

        except ValueError:
            print("You entered incorrect value. You should enter number: ")

        else:
            print(f"You entered: {checked_number_one}")
            break

    return checked_number_one


def check_correct_input_num_two():
    while True:
        number_two = input("Please, enter your second number: ")
        try:
            checked_number_two = float(number_two)

        except ValueError:
            print("You entered incorrect value. You should enter number: ")

        else:
            print(f"You entered: {checked_number_two}")
            break

    return checked_number_two


def add_num(num_1, num_2):
    return num_1 + num_2


def minus_num(num_1, num_2):
    return num_1 - num_2


def multiply_num(num_1, num_2):
    return num_1 * num_2


def divide_num(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        print("Division by zero prohibited")


def calculate_numbers(num_1, num_2, operation):
    result = None
    if operation == '+':
        result = add_num(num_1, num_2)
    elif operation == '-':
        result = minus_num(num_1, num_2)
    elif operation == '*':
        result = multiply_num(num_1, num_2)
    elif operation == '/':
        result = divide_num(num_1, num_2)

    else:
        print("incorrect operation")

    return result


def run_calculator():
    user_operation = check_user_operation()
    number_1 = check_correct_input_num_one()
    number_2 = check_correct_input_num_two()
    run_result = calculate_numbers(number_1, number_2, user_operation)

    print(f"Your result is {run_result}")

    return run_result


program_calculator_is_running = True
while program_calculator_is_running:
    run_calculator()
    answer = input("Do you want to continue? Enter: yes/no ")
    if answer != 'yes':
        program_is_running = False
        break
