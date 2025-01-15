string = input()

current_string = ''

while string != 'End':

    if string != 'SoftUni':

        for char in string:
            char *= 2
            print(char, end= '')
        print()
    string = input()
