#all rooms
import random
rooms={'centre':{'name':'centre','n':'discussion camp','s':'training camp','w':'weapon store','e':'captives','nw':'health care','ne':'resting camp','sw':'radar','se':'intel room','text':'You are in the centre of you army base camp\nYou can move around anywhere'},
       'discussion camp':{'name':'discussion camp','s':'centre','w':'health care','e':'resting camp','sw':'weapon store','se':'captives','text':'You are in the Discussion camp\nYou have walls in the north direction'},
       'health care':{'name':'health care','s':'weapon store','e':'discussion camp','se':'centre','text':'You are in the Health care\nYou have walls in the north and west direction'},
       'resting camp':{'name':'resting camp','s':'captives','w':'discussion camp','sw':'centre','text':'You are in resting camp\nYou have walls in the north and east direction'},
       'weapon store':{'name':'weapon store','n':'health care','s':'radar','e':'centre','ne':'discussion camp','se':'training camp','text':'You are in weapon store\nYou have walls in the west direction'},
       'captives':{'name':'captives','n':'resting camp','s':'intel room','w':'centre','nw':'discussion camp','sw':'training camp','text':'You are in the captives\nYou have walls in the east direction'},
       'radar':{'name':'radar','n':'weapon store','e':'training camp','ne':'centre','text':'You are in the radar room\nYou have walls in the south and west direction'},
       'training camp':{'name':'training camp','n':'centre','w':'radar','e':'intel room','nw':'weapon store','ne':'captives','text':'You are in the training camp\nYou have walls in the south direction'},
       'intel room':{'name':'intel room','n':'captives','w':'training camp','nw':'centre','text':'You are in the intel room\nYou have walls in the south and east direction'}}
direction=['n','s','e','w','ne','nw','se','sw']
current_room=rooms['centre']

#game commencement
print("Welcome to game of Army base\nYou are now a messenger, you need to go as the system says by typing the directions",direction,'\nPress q to quit the game')

init_room = random.choice(list(rooms.keys()))
if init_room==rooms['centre']:
    init_room = random.choice(list(rooms.keys()))
fin_room = random.choice(list(rooms.keys()))
if fin_room==init_room:
    fin_room = random.choice(list(rooms.keys()))

def advance():
    direction = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']
    current_room = rooms['centre']
    print()
    print("Go to",init_room)
    while current_room['name']!=init_room:
        print()
        print(current_room['text'])  # telling the user where he is now
        while True:
            movement = input("\nGive me the direction: ").lower()
            if (movement == 'q'):
                return
            # changing the current position
            if movement in direction:
                if movement in current_room:
                    current_room = rooms[current_room[movement]]
                    break
                else:
                    print("Invalid move, You have got walls over there")
            else:
                print('Invalid input, Check spelling')


    message=input('You are in the correct room, pick up the information by typing \'pick\'')
    print()
    if message=='pick':
        print()
        print('Go to',fin_room)
        while current_room['name'] != fin_room:
            print()
            print(current_room['text'])
            while True:
                movement = input("\nGive me the direction: ").lower()
                if movement=='q':
                    return
                if movement in direction:
                    if movement in current_room:
                            current_room = rooms[current_room[movement]]
                            break
                    else:
                         print('Invalid input, you have walls over there')
                else:
                    print('Invalid input')

        print("You are in the correct room")


        message=input("Drop the message by typing \'drop\'")
        if message=='drop':
            print("Successfully message sent")

advance()
