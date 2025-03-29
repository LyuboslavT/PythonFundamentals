string = input()

letters = ''
digits = ''
chars = ''

for char in string:

    if char.isdigit():
        digits += char

    elif char.isalpha():
        letters += char

    else:
        chars += char

print(digits)
print(letters)
print(chars)