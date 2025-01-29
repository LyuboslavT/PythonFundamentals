string_list = input().split(' ')

rounded_list = []

for element in string_list:
    int_element = float(element)
    rounded_list.append(round(int_element))

print(rounded_list)