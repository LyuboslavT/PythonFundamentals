n = int(input())

numbers = []


for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

filtered_list = []

if command == 'even':

    for num in numbers:

        if num % 2 == 0:
            filtered_list.append(num)

elif command == 'odd':

    for num in numbers:

        if num % 2 != 0:
            filtered_list.append(num)

elif command == 'positive':

    for num in numbers:

        if num >= 0:
            filtered_list.append(num)

elif command == 'negative':

    for num in numbers:

        if num < 0:
            filtered_list.append(num)

print(filtered_list)