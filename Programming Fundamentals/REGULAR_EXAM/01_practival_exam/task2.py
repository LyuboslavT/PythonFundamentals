import re
n = int(input())

pattern = r"^!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[A-Za-z]{8,})\]$"

for _ in range(n):
    l = input()

    match = re.match(pattern, l)

    if match:
        command = match.group("command")
        message = match.group("message")
        ascii_value = [str(ord(char)) for char in message]
        print(f'{command}: {" ".join(ascii_value)}')

    else:
        print("The message is invalid")