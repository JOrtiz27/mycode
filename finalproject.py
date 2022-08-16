#RPG GAME "the messanger"
import time 
#import time allows a function to returns the number of seconds passed since he cmd
print("Welcome player you have been woken up and sent to HQ for your orders once there you recieve orders to travel to the front lines and  meet up with Kilo.co and deliever a time sensitive message to their commander to not attack obj Bravo on friday @0300 as it is a trap by the federation and for them to wait till air support that morning  @0500 as they will carpet bomb the objective....what will you do???")
time.sleep(3)
# Gives the player choices on what to do. 
print(" A. go awol and join the federation and have your comadres die B. take the orders and steal top secret maps then flee to the federation C. embark on this daring mission and save your fellow Empire brothers for honor and glory")
time.sleep(3)
print("enter your choice here ")
choice = input ()
if (choice == 'A'):
    print("you have been caught by the federation and accused as a spy and is excuted on live TV as propaganda GAME OVER")
    exit()
if (choice == 'B'):
        print("you almost escaped to the Federation but you were followed when you took the maps and was hunted down by the Royal Mithril Battalion and killed off GAME OVER ")
        exit()
if (choice == 'C'):
    print("You rode off with your horse an arrive to Rhine where you are attacked by a solo recon team of four federalist soldiers ")
    time.sleep(1)
print ("YOU JUMPED OFF YOUR HORSE TO COVER WHAT DO YOU NOW, A. SHOOT BACK WHERE YOU ARE PIN DOWN OR  B. SPRINT AND SHOOT BEHIND THE BARRIER")
time.sleep(3)
print("enter your choice here ")
choice = input ()
if (choice == 'A'):
    print("you got shot in the head and died, GAME OVER")
    exit()
    if (choice == 'B'):
        print("you made it behind the barrier and with your M1897 shot gun you shot two shooters that rushed you  but there two more left") 
        time.sleep(10)
        # The "if" command allows a player to make a choice with conditions attached
rooms = {
    'Great Hall': {'name': 'Great Hall', 'South': 'Dining Room', 'North': 'Armory',
                   'East': 'Hallway', 'West': 'Bedroom', 'text': 'The Great Hall, begin your quest'},

    'Bedroom': {'name': 'Bedroom', 'East': 'Great Hall', 'contents': 'Magic wand',
                'text': 'A Bedroom. There appears to be a Magic wand in the corner'},

    'Hallway': {'name': 'Hallway', 'West': 'Great Hall', 'North': 'Cellar', 'contents': 'Sword',
                'text': 'A Hallway. There appears to be a Sword on the wall'},

    'Cellar': {'name': 'Cellar', 'South': 'Hallway', 'contents': 'Book',
               'text': 'A Cellar. There is a Book on a shelf'},

    'Dining Room': {'name': 'Dining Room', 'North': 'Great Hall', 'East': 'Kitchen', 'contents': 'Potion',
                    'text': 'The Dining Room. It looks like somebody left their Potion behind...'},

    'Kitchen': {'name': 'Kitchen', 'West': 'Dining Room', 'contents': 'Shield',
                'text': 'A Kitchen. What a strange place to find a Shield'},

    'Armory': {'name': 'Armory', 'South': 'Great Hall', 'East': 'Proving Grounds', 'contents': 'Armor',
               'text': 'The Armory. That Armor looks like it would fit you...'},

    'Proving Grounds': {'name': 'Proving Grounds', 'contents': 'Minotaur',
                        'text': 'The Proving Grounds. Are you ready for your showdown?'}
}

def show_instructions():
    # print a main menu and the commands
    print('-------------------------------------------------------')
    print("Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the minotaur.")
    print("Move commands: South, North, East, West")
    print("Add to Inventory: get 'item name'")
    print('-------------------------------------------------------')


print('''--------------------------------------------------------------------------------------------------------
A great beast has taken over your lands. You are a young Viking, tasked with defeating the minotaur
and becoming the village hero. The grand hall holds everything you need. To defeat the beast, you must find the
six treasures located within the grand hall and defeat the beast that plagues your land!
--------------------------------------------------------------------------------------------------------''')
time.sleep(4)
show_instructions()
time.sleep(4)
while True:
    # display current location
    print()
    print('You are in {}.'.format(currentRoom['text']))
    # get user input
    command = input('\nWhat do you do? ').strip()
    # movement
    if command in directions:
        if command in currentRoom:
            currentRoom = rooms[currentRoom[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # bad command
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in currentRoom['contents']:
            carrying.append(item)
            print('You grabbed {}.'.format(currentRoom['contents']))
        else:
            print("I don't see that here.")
while currentRoom in ['Proving Grounds']:
    if len(carrying) in 6:
        print('You collected all of the items, and defeated the minotaur!')
    else:
        print('It looks like you have not found everything, you have been defeated!')

