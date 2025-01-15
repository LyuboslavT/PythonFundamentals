# num1, num2, num3 = int(input()), int(input()), int(input())
#
# print(max(num1, num2, num3))

num1 = int(input())
num2 = int(input())
num3 = int(input())

largest_number = 0

if num1 >= num2 and num1 >= num3:
    largest_number = num1

elif num2 >= num1 and num2 >= num3:
    largest_number = num2

else:
    largest_number = num3

print(largest_number)