n = int(input())
word = input()

strig_list = []

for _ in range(n):
    current_string = input()
    strig_list.append(current_string)

print(strig_list)

filtered_list = []

for string in strig_list:

    if word in string:
        filtered_list.append(string)
print(filtered_list)