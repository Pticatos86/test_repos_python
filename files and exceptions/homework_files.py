"""Solution of task 1"""
import os

print(os.getcwd())
first_file_path = '../files and exceptions/first.txt'
second_file_path = '../files and exceptions/second.txt'

with open(first_file_path, 'w') as file_one:
    file_one.write("I am a little python teapot,\nShort and stout.\nHere is my handle,\nHere is my spout:)")

with open(first_file_path, 'r') as file_one:
    with open(second_file_path, 'w') as file_two:
        file_two.writelines(file_one)

with open(second_file_path, 'r') as file_two:
    print(f"Copied text from file first.txt to file second.txt is:\n{file_two.readlines()}")

# print(file_one.closed)
# print(file_two.closed)

"""Solution of task 2"""
import csv

with open('names.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    with open('email.csv', 'w', newline='') as new_scv_file:
        fieldnames = ['email']
        writer = csv.DictWriter(new_scv_file, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()

        for line in reader:
            del line['first_name']
            del line['last_name']
            writer.writerow(line)

with open('email.csv', 'r') as new_csv_file:
    print(f"Result email column in file email.csv is:\n{new_csv_file.readlines()}")

"""Solution of task 3"""
key_request = input("Please, enter your key dictionary: ")

assert key_request == key_request.lower(), "You must enter key in lower case"

course = {
    'title': 'AQA',
    'language': 'Python',
    'level': 'PRO',
    'frame': 'pytest'}

try:
    result_search = course[key_request]

except KeyError:
    result_search = "your entered key does not exist"

print(f"Your result is - {result_search}")
