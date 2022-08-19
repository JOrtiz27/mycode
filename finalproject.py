#RPG GAME "the messenger"
import time 
import cmd
import sys
import os
import random
import requests 
import json 
from tkinter import *
from tkinter.font import Font
#
#-----------------------------------------------------------------------------------------------------------------------------------
# CMD: module typically involves a set of functions and variables
# SYS: function provides the name of the existing python modules which have been imported.
# OS: creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
# Random: generate random numbers.
# Time allows a function to returns the number of seconds passed since last cmd
# request allow the user to send HTTP requests using Python    
# json is script that allows the user to conduct an (executable) file which is made of text in a programming language, to store and
# transfer the data.
#-----------------------------------------------------------------------------------------------------------------------------------
#displays the situation for the player
print("Welcome player you have been woken up and sent to HQ and recieve orders to travel to the front lines \n  and deliever a time sensitive message to their commander to not attack obj B on friday @0300 as it is a trap by the Russian federation \n and for them to wait till air support that morning  @0500 as they will carpet bomb the objective....what will you do???")
time.sleep(2)
print("      ")
# I am giving the player choices on what to do. 
print(" A. Go awol and join the federation and have your comadres die \n B. Take the orders and steal top secret maps, and then flee to the federation side \n  C. embark on this daring mission and save your fellow Empire brothers for honor and glory")
time.sleep(1)

print("enter your choice here ")
choice = input ().upper()
if (choice == 'A'):
    print("You have been caught by the federation and accused as a spy and is excuted on live TV as propaganda GAME OVER")
    exit()
if (choice == 'B'):
        print("You almost escaped to the Federation but you were followed when you took the maps and was hunted down by the Royal Mithril Battalion and killed off GAME OVER ")
        exit()
if (choice == 'C'):
    print("You rode off with your horse an arrive to your first stop to rest... \n Which is an abandoned town called Rhine \n when suddenly four Russian federalist soldiers attack you")
    time.sleep(2)
    print ("WHAT DO YOU DO NOW? \n A. SHOOT BACK WHERE YOU ARE PIN DOWN \n  B. SPRINT AND SHOOT BEHIND THE NEARBY BARRIER")
time.sleep(1)
print("enter your choice here ")
choice = input ().upper()   
if (choice == 'A'):
    print("you got shot in the head and died, GAME OVER")
    exit()
if (choice == 'B'):
        print("you made it behind a weaken old wall made out of wood \nand with your shotgun you shot at two shooters that rushed you but theres two more left")
        time.sleep(1)
        print("what do you do now? \n A.throw grenades at the two behind the broken down shack and shoot them \n B. throw a smoke grenade and jump on your horse and run away?")
        time.sleep(2)
print("enter your choice here ")
choice = input ().upper()  
if (choice == 'A'):
    print("With you throwing the gernades they left their cover and jump into the open area \n where you then shot the last two with your shotgun ")
    time.sleep(5)
    print("       ")
    print("       ")
    print ("You wraped yourself up and rested for a little bit;\n and now that you have gathered their water and ammo you move to Odesa")
time.sleep(2)
if (choice == 'B'):
    print("you were shot in the back and killed by the enemy sniper while you fled GAME OVER")
    exit()
    time.sleep(5)
    print("   ")
print("WELCOME TO ODESSA")
time.sleep(5)
print("               ")
print("You check your road map list to reveal how long you have left")
time.sleep(5)
#------------------------------------------------------------------------------------------------------------------------------------
#
#Map is my varible that contains three strings
## Here I use the  enumerate function which allows me to make list of my varible "Maps" and number down my strings...
print("   ")
Maps = ["[Checked] --HQ is 10hrs south from Rhine","[Checked] --Rhine is 5 hrs South from Odessa", "[Checked] --Odessa is 20 mins south away from the frontlines and the unit base", "[    ]the frontlines is 1,500 meters east from OBJ B"]
for x, element in enumerate(Maps):
    print(x, element)
# the Enumerte function allows me to eliminate the count function and its formula of count + = 1 
#the count is also another function that works by using integers that keeps track of how long my list is
#count + =1 adds increasing numbers next to strings
#-----------------------------------------------------------------------------------------------------------------------------------
time.sleep(10)
print("After twenty mins of riding on horse you made it to the frontline HQ\n congrats you delivered the message!!! ")
time.sleep(25)
exit()
#----------------------------------------------------------------------------------------------------------------------------------
#
def shownews():
    #below I am creating a response from the api and the .GET function allows me to send arequest to a specified url such as the one below and the .json() allows me to convert it to a json file
    response = requests.get(url,headers=headers).json()
    #.config allowed me  to edit the text as well as  other properties of the Labels
    #This function label.config(text="Headlines: " + response[0]["title"] +"\n"+  "source: " + response[0]["source"] allows me to get a line of headers from news articles and its source and creates a list for me.                     
    label.config(text="Headlines: " + response[0]["title"] +"\n"+  "source: " + response[0]["source"]+"\n"+"\n"+
                        "Headlines: " + response[1]["title"] +"\n"+  "source: " + response[1]["source"]+"\n"+"\n"+
                 "Headlines: " + response[2]["title"] +"\n"+  "source: " + response[2]["source"]+"\n"+"\n"+
                 "Headlines: " + response[3]["title"] +"\n"+  "source: " + response[3]["source"]+"\n"+"\n"+
                 "Headlines: " + response[4]["title"] +"\n"+  "source: " + response[4]["source"]+"\n"+"\n"+
                 "Headlines: " + response[5]["title"] +"\n"+  "source: " + response[5]["source"]+"\n"+"\n"+
                 "Headlines: " + response[6]["title"] +"\n"+  "source: " + response[6]["source"]+"\n"+"\n"+
                 "Headlines: " + response[7]["title"] +"\n"+  "source: " + response[7]["source"]+"\n"+"\n"+
                 "Headlines: " + response[8]["title"] +"\n"+  "source: " + response[8]["source"]+"\n"+"\n")


url = "https://ukraine-war-live2.p.rapidapi.com/news"
# url is where the source is comming from
#The Header displays  my key and what website it is gathered from
headers = {
	"X-RapidAPI-Key": "a781a16467mshac78afc027cfb15p11a1b1jsn079a4432bca8",
	"X-RapidAPI-Host": "ukraine-war-live2.p.rapidapi.com"
}
#the command below allows me to display a text window with its size and title.
window = Tk()
window.geometry("1200x700")
window.title("Barely put together; Ukraine Federation News paper of the war in the frontlines")
#Button function is used to add buttons in a Python application. These buttons can display text or images that convey the purpose of the buttons
# font=( basically displays well my font and size 
button = Button(window,text="Load",font=("BELL MT",20),command=shownews,width=100)
button.pack()
# the label = defines my lables and the  .pack() fill option is used to make a widget fill the entire frame.
label = Label(window,font=("Arial",12),justify=CENTER) #Use LEFT to organze better
label.pack(pady=20)
window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------
# this is displaying a 
#display a short api of the Federation losses  so far aka (real life russiaa) BDA of odessa api from https://russianwarship.rip/api-documentation/v1
#display you journey out of odessa and made it to the front lines and delivered ythe message Mission Accomplished You Won!! 
#time.sleep(2) print("JOB well done") exit()


# The "if" command allows a player to make a choice with conditions attached
# choice === 'input()': <-- This allows me to set a condtion and how to move forward











