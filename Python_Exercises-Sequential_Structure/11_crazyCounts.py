# Make a Program that asks for 2 integers numbers and a real number. Calculate and show:
# A) the product of double the first with half the second.
# B) the sum of triple the first with the third.
# C) the third one raised to the cube.


firstInt = int(input('Insert the first integer number: '))
secondInt = int(input('Insert the second integer number: '))
floatNum = float(input('Insert the float number: '))

aCount = (firstInt * 2) * (secondInt / 2)
bCount = (firstInt * 3) + floatNum
cCount = floatNum**3

print(f'\nthe product of double the first with half the second is {aCount}')

print(f'\nthe sum of triple the first with the third is {bCount:.2f}')

print(f'\nthe third one raised to the cube is {cCount:.2f}')