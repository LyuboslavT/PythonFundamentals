string_count = int(input())

result = ''

for current_string in range(string_count):

    string = input()

    if ',' in string or '.' in string or '_' in string:
        result = f'{string} is not pure!'

    else:
        result = f'{string} is pure.'

    print(result)