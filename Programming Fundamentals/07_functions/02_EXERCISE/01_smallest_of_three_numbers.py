


def smallest_number() -> int:

    smallest = min(number_one, number_two, number_three)

    return smallest

number_one = int(input())
number_two = int(input())
number_three = int(input())


result = smallest_number()
print(result)