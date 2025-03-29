string = input().split()

repeated_string = [word * len(word) for word in string]

repeated_string = "".join(repeated_string)

print(repeated_string)