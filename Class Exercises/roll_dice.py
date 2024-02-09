from dice_roller_classes import Die,Dice

def main():
    print('The Dice Roller program')
    num_dice = int(input('Enter the number of dice to roll: '))

    dice = Dice()
    for i in range(num_dice):
        die = Die()
        dice.addDie(die)

    choice = 'y'
    while choice.lower() == 'y':
        dice.rollAll()

        print('Your Roll: ',end = "")
        for die in dice.list_die:
            print(die.value,end = " ")
        print()

        choice = input('Roll the dice again? (y/n): ')
    print('Bye!')

main()