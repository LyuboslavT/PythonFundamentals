name = input()

result = ''

while name != 'Welcome':

    if name == 'Welcome!':
        print("Welcome to Hogwarts.")
        break


    for length in range (len(name) + 1):

        if length < 5:
            result = f"{name} goes to Gryffindor."

        elif length == 5:
            result = f"{name} goes to Slytherin."

        elif length == 6:
            result = f"{name} goes to Ravenclaw."

        elif length > 6:
            result = f"{name} goes to Hufflepuff."

    if name == 'Voldemort':
        print("You must not speak of that name!" )
        break

    print(result)

    name = input()

