def is_happy_year(year):
    return len(set(str(year))) == len(str(year))

def next_happy_year(year):
    year += 1

    while not is_happy_year(year):
        year += 1

    return year

year_input = int(input())
result = next_happy_year(year_input)
print(result)