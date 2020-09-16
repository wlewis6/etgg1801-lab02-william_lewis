# ETGG 1801.90
# William Lewis
# Lab 02: Expressions
# Date: 9/13/2020
import random

print("Please note, that due to the color usage, this python script does not look right in the command prompt. Please view this file in something that can interpret Python scripts only. Thank you.")
print(' ___________ ')
print('|\t\t\t|')
print('|\t|  |\t|')
print('|\t\t\t|\n|\tL__⅃\t|')
print('L___________⅃')

print('\033[0;35;48m......................................\n.\033[1;36;48m/\\\033[0;35;48m...........\033[1;33;48mxxxxxxxxxx\033[0;35;48m...........\033[1;36;48m/\\\033[0;35;48m.\n\033[1;36;48m/  \\\033[0;35;48m........\033[0;33;48mxxxxxxxxxxxxxx\033[0;35;48m........\033[1;36;48m/  \\\n\t\\\033[0;35;48m......\033[1;33;48mxxxxxxxxxxxxxxxx\033[0;35;48m......\033[1;36;48m/\t\n\t \\\033[0;35;48m.....\033[0;33;48mxxxxxxxxxxxxxxxx\033[0;35;48m.....\033[1;36;48m/ \t\n', '\b\033[1;34;48mO\033[0;34;48mO '*19, '\033[0;38;48m')

barLength = int(input("How big is the health bar?"))
maxHealth = int(input("What is your maximum health?"))
while True:
    currentHealth = int(input("How much health do you have right now?"))
    if(0<=currentHealth<=maxHealth):
        print("Generating HP Bar...")
        break
    else: print("Invalid Health!")
barSegment = maxHealth / barLength
healthPercentage = currentHealth / maxHealth
barFilled = int(barLength * healthPercentage)
barEmpty = int(barLength - barFilled)
barFilledAscii = '\033[1;31;48m \b||' * barFilled
barEmptyAscii = '::' * barEmpty
print("\033[1;30;48m[",barFilledAscii+barEmptyAscii,"\033[1;30;48m]\033[0;38;48m")
input("Press Enter to continue...")

while True:
    playerName = input('What is your name?')
    while True:
        playerHealth = int(input('How much health do you have?'))
        if(0<playerHealth):
            print("You have", playerHealth, "Health Points.")
            break
        else: print("Invalid Health!")
    while True:
        enemyHealth = int(input('How much health does the enemy have?'))
        if(0<enemyHealth):
            print("The enemy has", enemyHealth, "Health Points.")
            break
        else: print("Invalid Health!")
    barsLength = int(input('How long do you want the health bars to be?'))
    playerDepletion = playerHealth
    enemyDepletion = enemyHealth
    print("Begin Fight!")
    while True:
        playerPercent = playerDepletion / playerHealth
        enemyPercent = enemyDepletion / enemyHealth
        playerBarF = int(barsLength * playerPercent)
        playerBarD = int(barsLength - playerBarF)
        enemyBarF = int(barsLength * enemyPercent)
        enemyBarD = int(barsLength - enemyBarF)
        playerBarFAscii = '\033[1;31;48m \b||' * playerBarF
        playerBarDAscii = '::' * playerBarD
        enemyBarFAscii = '\033[1;32;48m \b||' * enemyBarF
        enemyBarDAscii = '::' * enemyBarD
        print("\033[1;30;48m", playerName, "\b's Health: [",playerBarFAscii+playerBarDAscii,"\033[1;30;48m]\033[0;38;48m")
        print("\033[1;30;48mEnemy Health: [",enemyBarFAscii+enemyBarDAscii,"\033[1;30;48m]\033[0;38;48m")
        while True:
            playerInput = input("Would you like to [A]ttack or [B]lock?")
            if(playerInput=="A"):
                playerDice = random.randint(0,20)
                enemyDepletion = enemyDepletion - playerDice
                if(playerDice==0):
                    print("You missed.")
                else: print("You hit the enemy for", playerDice, "damage.")
                break
            if(playerInput=="B"):
                print("You guard against the enemy's attack!")
                break
            else: print("You can only do A or B.")
        if(enemyDepletion<=0):
            print("You win!")
            print("\n\nGAME OVER.")
            break
        else: print("The skeleton attacks!")
        enemyDice = random.randint(0,20)
        if(playerInput=="B"):
            print("You guard against the attack, lightening the enemy's blow!")
            enemyDice = enemyDice / 2
        else: print("The enemy strikes you with all of it's might!")
        playerDepletion = playerDepletion - enemyDice
        print("The enemy has hit you for", enemyDice, "damage.")
        if(playerDepletion<=0):
            print("The enemy strikes you down!")
            print("You lose!")
            print("\n\nGAME OVER.")
            break
        else: print("Next turn...")
    print("Play again")
    repeatInput = input("Input \"y\" to play again")
    if(repeatInput=="y"):
        print("Restarting...")
    else: break
print("\n\nLAB 02: EXPRESSIONS")
print("Created by William Lewis for the ETGG 1801 class.")
print("ASCII art at top done by me.")
input("\nThe End")