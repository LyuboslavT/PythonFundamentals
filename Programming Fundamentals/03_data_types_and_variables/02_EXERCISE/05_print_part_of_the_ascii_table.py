# # print(chr(60))
# # print(chr(61))
# # print(chr(62))
# # print(chr(63))
# # print(chr(64))
# # print(chr(65))
# <
# =
# >
# ?
# @
# A


start_index = int(input())
end_index = int(input())

char_list = []
ascii_range = ''

for i in range(start_index, end_index + 1):
    current_index = chr(i)
    char_list.append(current_index)
    ascii_range = " ".join(char_list)



print(ascii_range)