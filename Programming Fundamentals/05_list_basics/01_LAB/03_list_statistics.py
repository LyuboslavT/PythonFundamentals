from logging import currentframe

n = int(input())

positive_number_list = []
negative_number_list = []

for _ in range(n):
    current_input = int(input())

    if current_input >= 0:
        positive_number_list.append(current_input)

    else:
        negative_number_list.append(current_input)

print(positive_number_list)
print(negative_number_list)
print(f"Count of positives: {len(positive_number_list)}")
print(f"Sum of negatives: {sum(negative_number_list)}")