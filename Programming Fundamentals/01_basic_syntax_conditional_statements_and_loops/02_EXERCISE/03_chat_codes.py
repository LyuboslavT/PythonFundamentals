message_count = int(input())

code_message = ''

for messages in range(1, message_count + 1):
    current_messages = int(input())

    if current_messages == 88:
        code_message = 'Hello'

    elif current_messages == 86:
        code_message = 'How are you?'

    elif current_messages < 88:
        code_message = 'GREAT!'

    elif current_messages > 88:
        code_message = 'Bye.'

    print(code_message)