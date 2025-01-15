#Assume that one year has 365.2422 days on average•	Assume that one year has 365.2422 days on average

century = int(input())

century_in_years = century * 100
century_in_days = int(century_in_years * 365.2422)
century_in_hours = century_in_days * 24
century_in_minutes = century_in_hours * 60

print(f'{century} centuries = {century_in_years} years = {century_in_days} days = {century_in_hours} hours = {century_in_minutes} minutes')