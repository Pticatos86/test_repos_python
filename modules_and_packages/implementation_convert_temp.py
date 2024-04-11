from modules_and_packages.mathematics_function import convert_temp

if __name__ == '__main__':
    result_conversion = convert_temp(100, 'F')
    print(f"Result of converting is {result_conversion}")

test_temp = convert_temp(100, 'C')
print(f"Your result is {test_temp}")
