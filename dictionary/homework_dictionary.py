"""Solution task 1"""
check_name = input("Please, enter your name:  ").title()
roles_dict = {
    'admin': ['George', 'Ruslan', 'Valeriy', 'Irina'],
    'maintainer': ['Julia', 'Alex'],
    'manager': ['Piter', 'Max', 'Sophia'],
    'developer': ['Natali', 'Nikita', 'Diana']
}
list_system_names = []
system_role = ''

for roles, list_names in roles_dict.items():
    for names in list_names:
        list_system_names.append(names)
        if check_name in names:
            system_role = roles
        else:
            pass
"""I think for correcting end current loops should be block else,
but I don`t know what to write in this block else.
Is it correct if i write else: pass?"""

if check_name in list_system_names:
    print(f"Hello {system_role}")
else:
    print("Hello guest")

"""Solution task 2"""
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': 'Os'}
initial_str = 'https://www.youtube.com/watch?'

params_list = []
for key, value in params.items():
    params_list.append(key + '=' + value)

params_string = '&'.join(params_list)
print(f"Result link is {initial_str + params_string}")

"""Solution task 3"""
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=Os'
result_dict = {}

key_one = 'w'
value_one = result_link.count(key_one)
result_dict[key_one] = value_one

key_two = 'a'
value_two = result_link.count(key_two)
result_dict[key_two] = value_two

key_three = 't'
value_three = result_link.count(key_three)
result_dict[key_three] = value_three

print(f"Result dictionary from link {result_link} is {result_dict}")
