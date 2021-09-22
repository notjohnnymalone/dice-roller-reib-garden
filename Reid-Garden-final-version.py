##-------------------##
#CP2-F04 Team Programming
#Reid A. Martin & Graden Rusk
##-------------------##



#----Functions start here----#

import random
import time


#SirRipher_Patch_1
def dice_roll(x):
    roll = random.randint(x * 1, x * 6)
    return random.randint(x * 1, x * 6)



def welcome():
    print("Hello! and welcome to Reib and Gardens Dice Roller!")

    
def dice_start():
    if player_select() == 1:
        player = "Garden"
        computer = "Reib"
    
    else:
        player = "Reib"
        computer = "Garden"
    try:
        dice_1 = int(input(f"How many Dice are you going to use? \n>>> "))
        ###
        human = dice_roll(dice_1)
        print(f"{player} got {human}.")
        ###
        robot = dice_roll(dice_1)
        print(f"{computer} got {robot}.")
        if human > robot:
            print(f"{player}(you) won!")
            print("You won by", human - robot)
        elif human < robot:
            print(f"{computer} won, you lost")
            print("You lost by", robot - human)
        elif human == robot:
            print("You tied.")
            time.sleep(1)
            print("thats dumb.")
    except:
        print("Please type a number.")
        dice_start()


def player_select():
    rorg = 0
    print(f"Who do you want to play as?\nGarden or Reib?")
    player = input(">>> ")
    if player == 'graden'or player =='garden' or player == 'gar' or player == 'Graden' or player ==  'GRADEN' or player == 'Garden' or player == 'GARDEN' or player == 'Gar' or player == 'GAR' or player == 'dumbbum' or player == 'g' or player == 'G' or player == '1':
        print(f"You have chosen Graden...\nIf you didn't...\n\nshut up.")
        return (rorg + 1)
    else:
        rorg = 2
        print("You have chosen Reid.")
        time.sleep(1)
        print("if you didn't...")
        time.sleep(2)
        print("i don't care.")
        return (rorg + 2)
    
def repeat():
    print("Do you want to try again?")
    rep_inp = input(">>> ")
    if rep_inp == "yes" or rep_inp == "y":
        print("Alright! Here we go!")
    elif rep_inp == "no" or rep_inp == "n":
        print("Thanks for playing!")
        time.sleep(2)
        print("you poor loser")
        time.sleep(2)
        quit()
    else:
        print("yes or no dummy")
        time.sleep(1)
        repeat()

##main code

welcome()

while 1:
    dice_start()
    repeat()