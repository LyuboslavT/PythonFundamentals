word = input()

for letter in range (len(word) - 1, -1, -1):
    print(word[letter], end='')

