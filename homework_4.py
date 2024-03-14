answer_info_1 = input("Please, write your name: ")
answer_info_2 = input("Write the letters you want to delete from your name: ")
result_info = answer_info_1.replace(answer_info_2, "")
print(f"Your result is: {result_info} ")


example_str = input("Please, enter your sentence: ")
title_str = example_str.title()
print(f"Result is {title_str}")


regular_str = 'Python'
print(regular_str)
upend_str = regular_str[::-1]
print(f"Result is {upend_str}")


str_1 = input("Write your first string: ")
str_2 = input("Write your second string: ")
result = str_1 == str_2
print(f"String {str_1} and string {str_2} have equal result {result}")


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
