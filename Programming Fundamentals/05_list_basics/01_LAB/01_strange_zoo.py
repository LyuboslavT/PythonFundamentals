my_list = []

for _ in range(3):
    list_element = input()
    my_list.append(list_element)



my_list[0], my_list[1], my_list[2] = my_list[2], my_list[1], my_list[0]

print(my_list)
