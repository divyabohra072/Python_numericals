#Write a program to count how many positive, negative, and zero values are present in a list.

#Code
print("Divya Bohra, 2581130")
numbers = [10, -5, 0, 22, -1, 0, -8, 15]

positive_count = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"List: {numbers}")
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zero values: {zero_count}")
