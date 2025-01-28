

number_of_lines = int(input())

total_sum = 0

for char in range(number_of_lines):
    current_char = ord(input())

    total_sum += current_char

print(f'The sum equals: {total_sum}')