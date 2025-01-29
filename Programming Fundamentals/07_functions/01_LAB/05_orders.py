def calculating_orders(product, quantity):
    if product == "coffee":
        price = 1.50
        return quantity * price

    elif product == "water":
        price = 1.00
        return quantity * price

    elif product == "coke":
        price = 1.40
        return quantity * price

    elif product == 'snacks':
        price = 2.00
        return quantity * price


input_product = input()
input_quantity = int(input())

result = calculating_orders(input_product, input_quantity)
print(f'{result:.2f}')