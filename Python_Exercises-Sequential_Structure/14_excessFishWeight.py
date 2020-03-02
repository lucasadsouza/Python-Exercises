# João Papo-de-Pescador, a good man, bought a microcomputer to control
# the daily income of your work. Every time he brings a weight of fish
# greater than that established by the fishing regulations of the state of São Paulo (50 kilos)
# You must pay a fine of R$ 4.00 per excess kilo. John needs you to do a
# program that reads the weight variable (fish weight) and calculates the excess. Record to
# variable exceeding the amount of kilos beyond the limit and in the fine variable the value
# of the fine that João must pay. Print the program data with the appropriate messages.


weight = float(input('Insert the weight of the fish: '))

if weight > 50:
    excess = weight - 50
    fineValue = excess * 4

    print(f'\nThere is an excess of {excess}Kg.')
    print(f'\nYou will pay {fineValue:.2f}R$ fine.')

else:
    print("\nYour fish didn't excess the limit.")
