# Make a program for a paint store. The program should ask for the size
# in square meters of the area to be painted. Consider that the ink coverage
# is 1 liter for every 3 square meters and that the paint is sold in cans of
# 18 liters, which cost R $ 80.00. Inform the user of the quantity of cans
# ink to be purchased and the total price.


meters = float(input('Insert the area in square meters: '))

cans = (meters / 3) / 18

if cans != int(cans): cans = round(cans + 0.5)

cost = cans * 80

print(f'\nYou need {int(cans)} cans and will pay {cost:.2f}R$ for it')