start_value = input().split(" ")

absolute_value = []

for number in start_value:
    absolute_value.append(abs(float(number)))

print(absolute_value)