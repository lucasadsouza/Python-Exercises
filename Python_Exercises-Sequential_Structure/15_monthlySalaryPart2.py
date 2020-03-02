# Make a Program that asks how much you earn per hour and the number of hours worked
# in the month. Calculate and show your total salary in that month, knowing that they are
# discounted 11% for Income Tax, 8% for INSS and 5% for the union, make a
# program that gives us:
# A) gross salary.
# B) how much you paid INSS.
# C) how much you paid the union.
# D) the net salary.
# E) calculate the discounts and net salary, according to the table below:
# + Gross Salary: R $
# - IT (11%): R $
# - INSS (8%): R $
# - Union (5%): R $
# = Net Salary: R $
# Note: Gross Salary - Discounts = Net Salary.


salaryHour = float(input('Insert how much you earn by hour: '))
workedHours = float(input('Insert how many time in hours you worked in the month: '))

grossSalary = salaryHour * workedHours
incomeTax = grossSalary * 0.11
inss = grossSalary * 0.08
union = grossSalary * 0.05
netSalary = grossSalary - (incomeTax + inss + union)

print(f'\nYour gross salary is {grossSalary:.2f}R$')
print(f'\nYou paid for INSS {inss:.2f}R$')
print(f'\nYou paid for the Union {union:.2f}R$')
print(f'\nYour net salary is {netSalary:.2f}R$')