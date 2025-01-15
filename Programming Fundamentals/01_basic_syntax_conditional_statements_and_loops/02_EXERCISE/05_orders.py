order_count = int(input())

total_price = 0
price_per_order = 0

for order in range(order_count):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue

    elif days < 1 or days > 31:
        continue

    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    price_per_order = price_per_capsule * capsules_needed_per_day * days


    total_price += price_per_order

    print(f"The price for the coffee is: ${price_per_order:.2f}")

print(f'Total: ${total_price:.2f}')