test_info_1 = "Please, write your name: "
test_info_2 = "Write the letters you want to delete from your name?: "
test_info_3 = "Your new name is: "
answer_info_1 = input(f"{test_info_1}")
answer_info_2 = input(f"{test_info_2}")
answer_info_3 = answer_info_1.replace(answer_info_2, "")
result_info = input(f"{test_info_3} {answer_info_3}")


example_str = input("Please, enter your sentence: ")
title_str = example_str.title()
print(title_str)


regular_str = 'Python'
upend_str = regular_str[::-1]
print(upend_str)


entrance_str_1 = input("Please, enter your first comment: ")
entrance_str_2 = input("Please, enter your second comment: ")
if len(entrance_str_1) < len(entrance_str_2):
    print("First comment is short")
else:
    print("First comment is long")


my_str = "I like eat sushi"
quantity_str = 5
result_str = my_str * quantity_str
print(result_str)


button_1 = "Uan --> Usd"
button_2 = "Usd --> Uan"
button_3 = "Uan --> Eur"
button_4 = "Eur --> Uan"
rate_button_1 = 0.026
rate_button_2 = 38.76
rate_button_3 = 0.024
rate_button_4 = 42.47
info_str = input(f"If you want to convert: {button_1} enter '1',"
                 f"{button_2} enter '2',"
                 f" {button_3} enter '3',"
                 f" {button_4} enter '4' ")
info_sum = float(input("Enter the sum of your currency: "))

if info_str == '1':
    print(info_sum * rate_button_1)
elif info_str == '2':
    print(info_sum * rate_button_2)
elif info_str == '3':
    print(info_sum * rate_button_3)
elif info_str == '4':
    print(info_sum * rate_button_4)
else:
    print("Enter valid number for your operation ")
