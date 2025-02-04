number = input().split()

digits = []

for char in number:
    digits.append(int(char))

print(f"The minimum number is {min(digits)}")
print(f"The maximum number is {max(digits)}")
print(f"The sum number is: {sum(digits)}")