list_some_elements = [23, 0, 56, 100, 50, True, False, 'abc', 10.5]
client_num = int(input("Please, enter your number: "))
dividing_list_num = []
for elements in list_some_elements:
    if type(elements) == int:
        dividing_num = elements // client_num
        dividing_list_num.append(dividing_num)

print(f"After dividing your number {client_num} by numbers from list {list_some_elements} "
      f"you get numbers in list {dividing_list_num}")


unsorted_list = [1, 5, 68, 0]
for num in range(1, len(unsorted_list)):
    if unsorted_list[num] != unsorted_list[num - 1] + 1:
        print(f" First inconsistent number in list {unsorted_list} is {unsorted_list[num]}")
        break


# this is my own solution )) for task 3
list_one_element = [1]
list_two_elements = [1, 2]
list_three_elements = [1, 2, 3]
list_four_elements = [1, 2, 3, 4]
list_five_elements = [1, 2, 3, 4, 5]

for el in list_one_element:
    print(el)
for el in list_two_elements:
    print(el, end=' ')
print()
for el in list_three_elements:
    print(el, end=' ')
print()
for el in list_four_elements:
    print(el, end=' ')
print()
for el in list_five_elements:
    print(el, end=' ')
print()
print()


# I looked up this solution of task 3 in internet, i tried on my own way, but not correct
figure_num = 6
for raw in range(1, figure_num):
    for column in range(1, raw + 1):
        print(column, end=' ')
    print()
