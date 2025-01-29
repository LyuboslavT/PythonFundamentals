string = input()
n = int(input())

repeated_string = lambda x, y: x * y
result = repeated_string(string, n)
print(result)