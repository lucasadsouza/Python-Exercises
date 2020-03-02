# Make a Program that asks for the temperature in degrees Celsius,
# transform it and show it in degrees Farenheit.


celsius = float(input('Insert the temperature in Celsius: '))

farenheit = (celsius * 1.8) + 32

print(f'\n{celsius:.2f}°C in Farenheit is {farenheit:.2f}°F')