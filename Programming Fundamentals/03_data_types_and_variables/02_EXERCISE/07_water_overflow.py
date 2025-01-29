TANK_CAPACITY = 255

pours = int(input())

poured_liters = 0

for _ in range(pours):
    current_pour = int(input())



    if poured_liters + current_pour > TANK_CAPACITY:
        print("Insufficient capacity!")

    else:
        poured_liters += current_pour


print(poured_liters)