# Make a program that asks for the size of a file to download (in MB)
# and the speed of an Internet link (in Mbps), calculate and report the time
# approximate file download using this link (in minutes).


size = float(input('Insert the file size: '))
speed = float(input('Insert the speed of an internet link in Mbps: '))

if size != int(size): size = round(size + 0.5)

time = (size / speed) / 60

print(f'\napproximate time to download this file: {time:.2f} minutes')