def sum_numbers() -> int:

    numbers_sum = number_one + number_two

    return numbers_sum

def subtract() -> int:

    numbers_sum = sum_numbers()

    subtract_sum = numbers_sum - number_three

    return subtract_sum

def add_and_subtract(num_one, num_two, num_three) -> int:

    return num_one + num_two - num_three



number_one = int(input())
number_two = int(input())
number_three = int(input())

result = add_and_subtract(number_one, number_two, number_three)
print(result)