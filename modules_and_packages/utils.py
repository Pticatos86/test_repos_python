def validate_datatype(variable, expected_type):
    if isinstance(variable, expected_type):
        return variable
    else:
        raise ValueError(f"Expected datatype for variable {variable} is {expected_type}")


def check_user_operation(operation: str, correct_symbols=('+', '-', '*', '/')) -> str:
    if operation not in correct_symbols:
        raise ValueError(f"invalid operation {operation}, you should enter symbols {correct_symbols}")
    return operation
