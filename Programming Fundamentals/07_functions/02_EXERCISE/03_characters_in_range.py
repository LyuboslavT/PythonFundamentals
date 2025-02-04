string_list = []

def character_in_range(symbol_one, symbol_two) -> str:

    symbol_one = ord(first_symbol)
    symbol_two = ord(second_symbol)

    for character in range(symbol_one + 1, symbol_two, 1):
        string_list.append(character)


    return chr(string_list)

first_symbol = input()
second_symbol = input()

result = character_in_range(symbol_one=first_symbol, symbol_two=second_symbol)
print(" ".join(result))