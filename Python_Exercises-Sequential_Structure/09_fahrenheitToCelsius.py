# Make a Program that asks for the temperature in degrees Farenheit,
# transform and show the temperature in degrees Celsius.


farenheit = float(input('Insert the temperature in Farenheit: '))

celsius = ((farenheit - 32) * 5) / 9

print(f'\n{farenheit:.2f}°F in Celcius is {celsius:.2f}°C')