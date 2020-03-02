# Taking as input data a person's height,
# build an algorithm that calculates your ideal weight, using the following formula:
# (72.7 * height) - 58


height = float(input('Insert your height in meters: '))

weight = (72.7 * height) - 58

print(f'\nYour ideal weight is {weight:.2f}Kg')