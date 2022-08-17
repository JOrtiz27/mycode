#RPG GAME "the messanger"
import time 
import cmd
import textwrap
import sys
import os
import random

# CMD: module typically involves a set of functions and variables
# Textwrap: Wraps the single paragraph in text (a string) so every line is at most width characters long.
# SYS: function provides the name of the existing python modules which have been imported.
# OS: creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
# Random: generate random numbers.
# Time allows a function to returns the number of seconds passed since last cm
print("Welcome player you have been woken up and sent to HQ for your orders once there you recieve orders to travel to the front lines and  meet up with Kilo.co and deliever a time sensitive message to their commander to not attack obj Bravo on friday @0300 as it is a trap by the federation and for them to wait till air support that morning  @0500 as they will carpet bomb the objective....what will you do???")
time.sleep(2)

# I am giving the player choices on what to do. 
print(" A. Go awol and join the federation and have your comadres die or B. Take the orders and steal top secret maps, and then flee to the federation side or  C. embark on this daring mission and save your fellow Empire brothers for honor and glory")
time.sleep(2)
print("enter your choice here ")
choice = input ()
if (choice == 'A'):
    print("You have been caught by the federation and accused as a spy and is excuted on live TV as propaganda GAME OVER")
    exit()
if (choice == 'B'):
        print("You almost escaped to the Federation but you were followed when you took the maps and was hunted down by the Royal Mithril Battalion and killed off GAME OVER ")
        exit()
if (choice == 'C'):
    print("You rode off with your horse an arrive to your first stop. Which is an abandoned town called Rhine to rest....suddenly you are  ambushed by a solo recon team of four federalist soldiers ")
    time.sleep(2)

print ("YOU SUDDENLY JUMPED OFF YOUR HORSE TO COVER....WHAT DO YOU NOW?  A. SHOOT BACK WHERE YOU ARE PIN DOWN OR  B. SPRINT AND SHOOT BEHIND THE NEARBY BARRIER")
time.sleep(2)
print("enter your choice here ")
#-
#-Next scenerio
#-
choice = input ()
if (choice == 'A'):
    print("you got shot in the head and died, GAME OVER")
    exit()
if (choice == 'B'):
        print("you made it behind a weaken old wall made out of wood  and with your M1897 shotgun you shot at two shooters that rushed you but there two more left")
        time.sleep(2)
        print("what do you do now A. book it for the trees and conduct gurilla warfare by shooting and throwing grenades at the other two behind the broken down shack or B. throw a grenade and jump on your horse and run away?")
        choice = input ()
        print("enter your choice here ")
if (choice == 'A'):
    print("you were shot on the arm while you jumped behind a tree however with you throwing the gernades they left their cover and jump into    the open area where you then shoot the two with your shotgun ")
    time.sleep(2)
    print ("You wraped yourself up and rested for a little bit; and now that you have gathered their water and ammo you move to Odesa")
    time.sleep(2)
if (choice == 'B'):
    print("you were shot in the back and killed by the enemy sniper while you fled GAME OVER")
    exit()
    time.sleep(3)
print("WELCOME TO ODESA")
time.sleep(2)
print("You check your map to reveal your current location")
time.sleep(2)

import sys

# this is displaying a 
bitmap = """"
....................................................................
   **************   *  *** **  *      ******************************
  *********(frontlines)* ** (Obj bravo) * *****<*Federation>******************* *
 **      *****************     |  ******************************
          ***(odesa)******** | |        **  * **** ** ************** *
        *(Rhine)*****       |     *******   **************** * *
            ********        |   ***************************  *
   *        * **** ***      |   *************** ******  ** *
               <Republic> * |        ***************<Han's land>"*** ***  *
                 ******     |    *************    **   **  *
                 ********    |    *************    *  ** ***
                   ********  |       ********          * *** ****
                   *********  |       ******  *        **** ** * **
                   *********  |    ****** * *           *** *   *
              <  land ofFran>* ||||       ***** **             *****   *
                     *****  |          **** *            *****<republic>***
                    *****   |          ****              *********
                    ****    |          **                 *******   *
                    ***     |                                 *    *
                    **     *|<--sea embrago                  *
...................................................................."""

print('You only have half a day journey left be wary of the coastal areas they are going to be heavily watch and bombed by the federation navy')
print('Enter the message to display with the bitmap.')
message = input('> ')
if map == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.






# The "if" command allows a player to make a choice with conditions attached
# choice === 'input()': <-- This allows me to set a condtion and how to move forward












