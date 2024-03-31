"""Solution task 1"""
check_name = input("Please, enter your name:  ").title()
roles_dict = {
    'admin': ['George', 'Ruslan', 'Valeriy', 'Irina'],
    'maintainer': ['Julia', 'Alex'],
    'manager': ['Piter', 'Max', 'Sophia'],
    'developer': ['Natali', 'Nikita', 'Diana']
}

for role, list_names in roles_dict.items():
    if check_name in list_names:
        print(f"Hello {role}")
        break
    else:
        print("Hello guest!")

"""Solution task 2"""
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': 'Os'}
initial_str = 'https://www.youtube.com/watch?'

for key, value in params.items():
    initial_str += f"{key}={value}&"

result = initial_str.strip('&')

print(f"Adding a string to the dictionary: {result}")

"""Solution task 3"""
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=Os'
dict_count = {}

for element in result_link:
    if element in result_link:
        dict_count[element] = result_link.count(element)

print(f"How many times an element is repeated in a line {dict_count}")
