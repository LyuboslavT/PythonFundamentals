def check_palindromes(numbers_str):
    numbers = numbers_str.split(", ")

    for num in numbers:
        num = int(num)
        print(str(num) == str(num)[::-1])


numbers_input = input()
check_palindromes(numbers_input)
