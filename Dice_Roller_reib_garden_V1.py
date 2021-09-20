##-------------------##
#CP2-F04 Team Programming
#Reid A. Martin & Graden Rusk
##-------------------##



#----Functions start here----#

import random
import time

#SirRipher_Patch_1
def dice_roll(x):
    import random
    roll = random.randint(x * 1, x * 6)
    return random.randint(x * 1, x * 6)

def win(x, y):
    win_by = x - y
    return x - y

def lose(x, y):
    lose_by = x - y
    return x - y

def welcome():
    print("Hello! and welcome to Reib and Gardens Dice Roller!")
    dice_start()
    
def dice_start():
    try:
        dice_1 = int(input("How many Dice are you using to lose? "))
        ###
        human = dice_roll(dice_1)
        print(f"You got {human}.")
        ###
        robot = dice_roll(dice_1)
        print(f"The Robot got {robot}.")
        
    except:
        print("Please type a number.")
        dice_start()

def welcome():
    print("Hello! and welcome to Reib and Gardens Dice Roller!")

def player_select():
    rorg = 0
    print(f"Who do you want to play as?\nGarden or Reib?")
    player = input(">>> ")
    if player == 'graden'or player =='garden' or player == 'gar' or player == 'Graden' or player ==  'GRADEN' or player == 'Garden' or player == 'GARDEN' or player == 'Gar' or player == 'GAR' or player == 'dumbbum' or player == 'g' or player == 'G' or player == '1':
        rorg = 1
        print(f"You have chosen Graden...\nIf you didn't...\n\nshut up.")
    else:
        rorg = 2
        print("You have chosen Reid.")
        time.sleep(1)
        print("if you didn't...")
        time.sleep(2)
        print("i don't care.")
