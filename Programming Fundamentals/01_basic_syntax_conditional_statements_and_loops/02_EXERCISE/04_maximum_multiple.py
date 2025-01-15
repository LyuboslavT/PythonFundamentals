divisor = int(input())
boundary = int(input())

current_num = 0

for num in range(boundary, divisor + 1, -1):

    if num % divisor == 0:
        current_num = num
        break

print(current_num)