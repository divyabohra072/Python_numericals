#Write a program to input a list and check whether a given element exists in the list or not.

#Code
user_input = input("Enter list elements separated by spaces: ")
my_list = user_input.split()

target = input("Enter the element you want to search for: ")

if target in my_list:
    print(f"Yes! '{target}' exists in the list.")
else:
    print(f"No, '{target}' was not found.")
print("Divya Bohra, 2581130")
