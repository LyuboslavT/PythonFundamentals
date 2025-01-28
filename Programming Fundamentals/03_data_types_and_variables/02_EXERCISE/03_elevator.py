import math

n = int(input())
p = int(input())

courses_needed = math.ceil(n / p)
counter = 0

# for course in range(courses_needed):
#     counter += 1
#
#
#
# print(counter)

print(courses_needed)