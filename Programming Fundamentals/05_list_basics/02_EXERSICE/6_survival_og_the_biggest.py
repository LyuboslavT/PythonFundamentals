numbers = input().split()
numbers_to_remove = int(input())

list_of_numbers = []
result = []

for num in numbers:
    current_number = int(num)
    list_of_numbers.append(current_number)

for deleted_number in range(numbers_to_remove):
    smallest = min(list_of_numbers)
    list_of_numbers.remove(smallest)

for num in list_of_numbers:
    result.append(str(num))

print(', '.join(result))