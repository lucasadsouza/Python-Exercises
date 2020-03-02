# Taking as input the height (h) of a person, build an algorithm that calculates your
# ideal weight, using the following formulas:
# For men: (72.7 * h) - 58
# For women: (62.1 * h) - 44.7


height = float(input('Insert your height in meters: '))

menWeight = (72.7 * height) - 58
womenWeight = (62.1 * height) - 44.7

print(f'\nThe ideal weight for you if you is a man is {menWeight:.2f}Kg')
print(f'\nThe ideal weight for you if you is a woman is {womenWeight:.2f}Kg')