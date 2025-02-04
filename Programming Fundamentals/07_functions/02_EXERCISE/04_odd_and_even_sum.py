digits = []
even_digits = []
odd_digits = []

def odd_even(odd_sum, even_sum) -> str:

    for current_digit in number:

        if int(current_digit) % 2 == 0:
            even_digits.append(int(current_digit))

        else:
            odd_digits.append(int(current_digit))

    even_sum = sum(even_digits)
    odd_sum = sum(odd_digits)

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

number = input()

result = odd_even(even_digits, odd_digits)
print(result)