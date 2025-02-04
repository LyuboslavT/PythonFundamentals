def even_nums(num):
    return num % 2 == 0  # Returns True if even, False otherwise

numbers = list(map(int, input().split()))  # Convert input strings to integers

even_numbers = list(filter(even_nums, numbers))  # Filter even numbers

print(even_numbers)


# numbers = input().split()
#
# numbers_list = []
# even_numbers = []
#
# for character in numbers:
#     numbers_list.append(character)
#
#     if int(character) % 2 == 0:
#         even_numbers.append(int(character))
#
#
# print(even_numbers)