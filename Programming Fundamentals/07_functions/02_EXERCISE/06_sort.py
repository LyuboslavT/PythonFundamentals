int_list = []

numbers = input().split()

for digit in numbers:
    int_list.append(int(digit))

sorted_list = sorted(int_list)

print(sorted_list)