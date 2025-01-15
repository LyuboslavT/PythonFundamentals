n = int(input())

for i in range(1, n):
    for j in range(n - i):
        print('', end= ' ')
    for j in range(1, i):
        print('*', end='')
    for i in range(i, 0, -1):
        print('*', end= '')

    print()

for k in range(n, 0, -1):
    for j in range(n - k):
        print('', end= ' ')
    for j in range(1, k):
        print('*', end='')
    for i in range(0, k):
        print('*', end= '')

    print()