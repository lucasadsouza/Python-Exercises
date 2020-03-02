# Make a Program that asks for the 4 bimonthly notes and shows the average.


firstBim = float(input('Insert your first bimonthly note: '))
secondBim = float(input('Insert your second bimonthly note: '))
thirdBim = float(input('Insert your third bimonthly note: '))
fourthBim = float(input('Insert your fouth bimonthly note: '))

average = (firstBim + secondBim + thirdBim + fourthBim) / 4

print(f'\n{average}')