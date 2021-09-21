##-------------------##
#CP2-F04 Team Programming
#Reid A. Martin & Graden Rusk
##-------------------##



#----Functions start here----#

import random
import time

play = 0
#SirRipher_Patch_1
def dice_roll(x):
    import random
    roll = random.randint(x * 1, x * 6)
    return random.randint(x * 1, x * 6)

def points(x, y):
    win_by = x - y
    return x - y

def welcome():
    print("Hello! and welcome to Reib and Gardens Dice Roller!")
 #   player_select()
    
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
            difference = points(human, robot)
            print(f"You won by {difference} points.")
            repeat()
            
        elif robot > human:
            difference = points(robot, human)
            print(f"You lost by {difference} points.")
            repeat()
            
        else:
            print("How did you manage to tie?!?")
            time.sleep(2)
            print("I want you to try again!")
            dice_start
        
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
    




welcome()
while play == 0:
     dice_start()
