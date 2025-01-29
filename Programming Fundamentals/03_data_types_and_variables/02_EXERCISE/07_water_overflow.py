TANK_CAPACITY = 255

pours = int(input())

poured_liters = 0

for _ in range(1, pours + 1):
    current_pour = int(input())


    TANK_CAPACITY -= current_pour

    if current_pour > TANK_CAPACITY:
        print("insufficient capacity!")
        continue

    poured_liters += current_pour

print(poured_liters)