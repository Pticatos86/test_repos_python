test_word = input("Enter Palindrome word: ")
palindrome_word = test_word[::-1]
if palindrome_word == test_word:
    print(f"Your entered word {test_word} is Palindrome")
else:
    print(f"Your entered word {test_word} is not Palindrome")

current_list = ['Hillel', 'AQA', 'TEST']
new_str = ','.join(current_list)
print(f"List {current_list} has been converted to a string {new_str}")
new_list = new_str.split(',')
print(f"String {new_str} was listed again in list {new_list}")

list_unsorted = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
list_sorted = list_unsorted.copy()
list_sorted.sort(key=str.upper)
print(f"Unsorted list {list_unsorted} has been sorted in list {list_sorted}")

list_of_num_and_other_list = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
value_from_list = list_of_num_and_other_list[-1][3][0]
# print(value_from_list)
# print(type(value_from_list))
print(f"From list {list_of_num_and_other_list} has been taken value {value_from_list} and created new list "
      f"{[value_from_list]}")

sushi_menu_rolls_list = ['vegetarian_rolls', 'philadelphia_rolls', 'dragon_rolls', 'chief_rolls']
print(f"List {sushi_menu_rolls_list} is sorted {sushi_menu_rolls_list == sorted(sushi_menu_rolls_list)}")
