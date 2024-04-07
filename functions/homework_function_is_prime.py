"""Solution of task 2"""


def is_prime(number):
    if number not in range(2, 1001):
        return f"your entered number is out of range(2, 1000)"

    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True


def check_correct_input_number():
    while True:
        test_number = input(
            "Please, enter any number in range from 2 to 1000 to check whether it is prime or composite: ")
        try:
            checked_number = int(test_number)

        except ValueError:
            print("You entered incorrect value. You should enter integer number.")

        else:
            print(f"You entered: {checked_number}")
            break

    return checked_number


def run_prime_program():
    input_user_num = check_correct_input_number()
    finally_result = is_prime(input_user_num)
    print(f"Is your entered number - prime?: {finally_result} ")

    return finally_result


program_prime_is_running = True
while program_prime_is_running:
    run_prime_program()
    user_answer = input("Do you want to continue? Enter: yes/no: ")
    if user_answer != 'yes':
        program_prime_running = False
        break
