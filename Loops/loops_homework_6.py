list_some_elements = [23, 0, 56, 100, 50, True, False, 'abc', 10.5]
client_num = int(input("Please, enter your number: "))
dividing_list_num = []
for elements in list_some_elements:
    if type(elements) == int:
        if elements % client_num == 0:
            dividing_list_num.append(elements)

print(f"After dividing your number {client_num} by numbers from list {list_some_elements} "
      f"you get numbers in list {dividing_list_num}")


unsorted_list = [1, 5, 68, 0]
for num in range(1, len(unsorted_list)):
    if unsorted_list[num] != unsorted_list[num - 1] + 1:
        print(f" First inconsistent number in list {unsorted_list} is {unsorted_list[num]}")
        break
    else:
        print("The list contains consecutive numbers")


figure_num = 6
for raw in range(1, figure_num):
    for column in range(1, raw + 1):
        print(column, end=' ')
    print()
