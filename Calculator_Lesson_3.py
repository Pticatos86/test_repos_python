action = input("Choose your action (+, -, *, /): ")
if action not in ('+', '-', '*', '/'):
    quit()
num_1 = float(input("Number_1 = "))
num_2 = float(input("Number_2 = "))
if action == '+':
    print(num_1 + num_2)
elif action == '-':
    print(num_1 - num_2)
elif action == '*':
    print(num_1 * num_2)
elif action == '/':
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Division by zero")
