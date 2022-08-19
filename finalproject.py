#RPG GAME "the messenger"
"RPG game|Joseph|joey_2025@hotmail.com"
import time 
import cmd
import sys
import os
import random
import requests 
#
#-----------------------------------------------------------------------------------------------------------------------------------
# CMD: module typically involves a set of functions and variables
# SYS: function provides the name of the existing python modules which have been imported.
# OS: creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
# Time allows a function to returns the number of seconds passed since last cmd
# request allow the user to send HTTP requests using Python    
#random generates random numbers
#-------------------------------------------------------------------------------------------------------------------------
#displays the situation for the player
print("\nWelcome player you have been woken up and sent to HQ and recieve orders to travel to the front lines\nand deliever a time sensitive message to their commander to not attack obj B on friday @0300\nas it is a trap by the Russian federation\nand for them to wait till air support that morning @0500 as they will carpet bomb the objective....what will you do???")

time.sleep(2)
print("      ")

# I am giving the player choices on what to do. 

print("A. Go awol and join the federation and have your comadres die\nB. Take the orders and steal top secret maps, and then flee to the federation side\nC. embark on this daring mission and save your fellow Empire brothers for honor and glory")
time.sleep(1)

print("enter your choice here ")
choice = input ().upper()
if (choice == 'A'):
    print("You have been caught by the federation and accused as a spy and is killed on live TV as propaganda GAME OVER")
    exit()
elif (choice == 'B'):
        print("You almost escaped to the Federation but you were followed when you took the maps and was hunted down by the Royal Mithril Battalion and killed off GAME OVER ")
        exit()
elif (choice == 'C'):
    print("You rode off with your horse an arrive to your first stop to rest...\nWhich is an abandoned town called Rhine\nwhen suddenly four Russian federalist soldiers attack you")
else:
    print("the correct answer was C, moving on\nYou rode off with your horse an arrive to your first stop to rest...\nWhich is an abandoned town called Rhine\nwhen suddenly four Russian federalist soldiers attack you")
    time.sleep(2)
print ("WHAT DO YOU DO NOW?\nA. SHOOT BACK WHERE YOU ARE PIN DOWN\nB. SPRINT AND SHOOT BEHIND THE NEARBY BARRIER")
time.sleep(1)

print("enter your choice here ")
choice = input ().upper()   
if (choice == 'A'):
    print("you got shot in the head and died, GAME OVER")
    exit()
elif (choice == 'B'):
        print("you made it behind a weaken old wall made out of wood \nand with your shotgun you shot at two shooters that rushed you but theres two more left")
        time.sleep(2)
else:
        print("the correct answer was B\n and that you made it behind a weaken old wall made out of wood \nand with your shotgun you shot at two shooters that rushed you but theres two more left")
        time.sleep(2)
#------------new situation transitions in-----------------------------------------------------
print("what do you do now? \n A.throw a grenade and shoot them if they jump out into the open\n B.throw a smoke grenade and run away")

time.sleep(1)

print("enter your choice here ")

choice = input ().upper()  
if (choice == 'A'):
    print("With you throwing the grenades they left their cover and jump into the open area \n where you then shot the last two with your shotgun ")

elif (choice == 'B'):
    print("you were shot in the back and killed by the enemy sniper while you fled GAME OVER")
    exit()
else:
    print("the correct answer was A.\n now that you threw grenades the two other soldier left their cover and jump into the open area \n where you then shot the last two with your shotgun ")
    time.sleep(2)

#------------new situation transitions in-----------------------------------------------------
print ("You wraped yourself up and rested for a little bit;\n and now that you have gathered their water and ammo you  move to Odesa")

print("   ")

print("WELCOME TO ODESSA")

time.sleep(6)
print("               ")
print("You check your road map list to reveal how long you have left")
time.sleep(10)
#--------------------------------------------------------------------------------------------------------------------------
#Map is my varible that contains three strings
## Here I use the  enumerate function which allows me to make list of my varible "Maps" and number down my strings...
Maps = ["[Checked] --HQ is 10hrs south from Rhine","[Checked] --Rhine is 5 hrs South from Odessa", "[Checked] --Odessa is 20 mins south away from the frontlines and the unit base", "[    ]the frontlines is 1,500 meters east from OBJ B"]
for x, element in enumerate(Maps):
    print(x, element)
# the Enumerte function allows me to eliminate the count function and its formula of count + = 1 
#the count is also another function that works by using integers that keeps track of how long my list is
#count + =1 adds increasing numbers next to strings
#-----------------------------------------------------------------------------------------------------------------------------------
time.sleep(6)
print("After twenty mins of riding on your horse; you made it to the frontline's HQ\n congrats you delivered the message!!! ")
time.sleep(10)
exit()
#-----------------------------------------------------------------------------------------------------------------------
#
