#!/usr/bin/python3


def showInstructions():
  #print a main menu and the commands
  print('''
Wecolme You have been woken up and sent to HQ once there you are given orders to deliver a message to the front lines Charlie.co to not procceed with the attack on obj kilo since it is a trap by the federation and wait for airsupport as they will carpet bomb the object kilo

Commands:
  go [direction]
  get [item]
  fire [damage]
''')
def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
#the above print command displays to the player of where he is at and what he has
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

                  'Empire HQ': {
                  'north' : 'the Empire HQ' 
                  'south' : 'The kitchen of horrors',
                  'east'  : 'bloody Room',
                  'item'  : 'sword of life'
                },

            'The kitchen of horrors' : {
                  'north' : 'Hall of doom',
                  'item'  : 'shrek monster',
                  'fight' : 'fighting shrek'
                },
            'bloody Room' : {
                  'west' : 'Hall of doom',
                  'south': 'Garden of eden',
                  'item' : 'potion of youth',
                  'north' : 'Pantry',
               },
            'Garden of eden' : {
                  'north' : 'bloody Room'
               },
            'Pantry' : {
                  'south' : 'bloody Room',
                  'item' : 'questionable cookies',
            }
         }

#start the player in the Hall of doom
currentRoom = 'the Empire HQ'

showInstructions()

#the import random  generate random numbers.






#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    print(move[1])
      #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can not go that way it is sealed off!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

    #if they type get to sequence a battle with shrek
   




  ## Define how a player can win
  if currentRoom == 'Garden of eden' and 'sword of life' in inventory and 'potion of youth' in inventory:
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'shrek monster' in rooms[currentRoom]['item']:
    print('Shrek has got you and now you are forced to watch his films till you die... GAME OVER!')
    break
    

