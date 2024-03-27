"""Solution of task 1"""
first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
first_set = set(first_list)
second_set = set(second_list)
intersection_list = list(second_set.intersection(first_set))

print(f"List {intersection_list} contains numbers that are same in both lists {first_list} and {second_list}")


"""Solution of task 2"""
list_one = [1, 100, 0, 500, 201, 300, 7.5, 'abc']
list_two = [500, 7.5, 33, 26, 302, 501]
set_one = set(list_one)
set_two = set(list_two)
difference_list = list(set_one.difference(set_two))

print(f"List {difference_list} contains elements that are absent in list {list_two}")


"""Solution of task 3"""
count_nums = 0
list_nums = []
set_nums = set()
while count_nums < 5:
    input_nums = float(input("Please, enter your number: "))
    count_nums += 1
    list_nums.append(input_nums)
    set_nums.add(input_nums)

if len(list_nums) == len(set_nums):
    print(f"Your entered numbers {list_nums} are unique")
else:
    print(f" Your entered numbers {list_nums} are not unique")


# """Solution of task 4 with using method sorted"""
# my_list_nums = [23, 0, 543, -1, -26, 100, 30]
# my_list_nums_sorted = sorted(my_list_nums)
# minimal_num = my_list_nums_sorted[0]
# print(f"Number {minimal_num} is the minimal number in list {my_list_nums}")


"""Solution of task 4 with using loops"""
my_list_nums = [23, 0, 543, -1, -26, 100, 30]
minimal_num = my_list_nums[0]
for nums in my_list_nums:
        if nums < minimal_num:
            minimal_num = nums

print(f"Number {minimal_num} is the minimal number in list {my_list_nums}")


"""Solution of task 5"""
list_numbers = [78, -10, -500, 45, 0, 25]
sum_numbers = 0
for nums in list_numbers:
    sum_numbers = sum_numbers + nums

print(f" Sum of numbers from list {list_numbers} is {sum_numbers}")
