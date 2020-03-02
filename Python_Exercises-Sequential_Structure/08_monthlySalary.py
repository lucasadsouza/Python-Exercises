# Make a Program that asks how much you earn per hour and the number of hours worked in the month.
# Calculate and show your total salary for that month.


salaryHour = float(input('Insert how much you earn per hour: '))
workedHours = float(input('How many hours you worked in the month: '))

total = salaryHour * workedHours

print(f'\nYou will earn {total:.2f}$')