string = input().split()

list_numbers = []

for current_number in string:
    opposite_number = int(current_number) * -1
    list_numbers.append(opposite_number)

print(list_numbers)