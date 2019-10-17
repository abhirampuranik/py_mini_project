#all rooms
rooms={'centre':{'name':'centre','n':'discussion camp','s':'training camp','w':'weapon store','e':'captives','nw':'health care','ne':'resting camp','sw':'radar','se':'intel room','text':'You are in the centre of you army base camp and under keen eyes\nYou can move around anywhere'},
       'discussion camp':{'name':'discussion camp','s':'centre','w':'health care','e':'resting camp','sw':'weapon store','se':'captives','text':'You are in the Discussion camp where the army head and the force head are having a meeting\nYou have walls in the north direction'},
       'health care':{'name':'health care','s':'weapon store','e':'discussion camp','se':'centre','text':'You are in the Health care where army forces are getting treated and doctors are moving around\nYou have walls in the north and west direction'},
       'resting camp':{'name':'resting camp','s':'captives','w':'discussion camp','sw':'centre','text':'You are in resting camp where the army forces are taking rest and having casual talks\nYou have walls in the north and east direction'},
       'weapon store':{'name':'weapon store','n':'health care','s':'radar','e':'centre','ne':'discussion camp','se':'training camp','text':'You are in weapon store where army forces are testing out weapons and getting their weapons repaired\nYou have walls in the west direction'},
       'captives':{'name':'captives','n':'resting camp','s':'intel room','w':'centre','nw':'discussion camp','sw':'training camp','text':'You are in the dark part of the camp , i.e., the captives where intruders are caught, questioned, and tortured to reveal the aim they came in\nYou have walls in the east direction'},
       'radar':{'name':'radar','n':'weapon store','e':'training camp','ne':'centre','text':'You are in the radar room where higher officials are in look out for intruders and having the satellites positioned at the enemy bases\nYou have walls in the south and west direction'},
       'training camp':{'name':'training camp','n':'centre','w':'radar','e':'intel room','nw':'weapon store','ne':'captives','text':'You are in the training camp where army forces are getting trained and trying out the weapons\nYou have walls in the south direction'},
       'intel room':{'name':'intel room','n':'captives','w':'training camp','nw':'centre','text':'You are in the intel room where confidential information is exchanged with the officials of the army\nYou have walls in the south and east direction'}}
direction=['n','s','e','w','ne','nw','se','sw']
current_room=rooms['centre']

#game commencement
print("Welcome to game of Army base\nYou can move around using the abbreviated letter of the directions",direction,'\nPress q to quit the game')


while True:
    print()
    print(current_room['text'])  #telling the user where he is now
    while True:
        movement=input("\nGive me the direction: ").lower()
        if (movement == 'q'):
            break
        #changing the current position
        if movement in direction:
            if movement in current_room:
                current_room=rooms[current_room[movement]]
                break
            else:
                print("Invalid move, You have got walls over there")
        else:
            print('Invalid input, Check spelling')
    if (movement=='q'):
         break

