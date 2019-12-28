import pygame

rooms = {
    'centre': {'name': 'centre', 'n': 'discussion camp', 's': 'training camp', 'w': 'weapon store', 'e': 'captives',
               'nw': 'health care', 'ne': 'resting camp', 'sw': 'radar', 'se': 'intel room',
               'text': 'You are in the centre of you army base camp and under keen eyes\nYou can move around anywhere'},
    'discussion camp': {'name': 'discussion camp', 's': 'centre', 'w': 'health care', 'e': 'resting camp',
                        'sw': 'weapon store', 'se': 'captives',
                        'text': 'You are in the Discussion camp where the army head and the force head are having a meeting\nYou have walls in the north direction'},
    'health care': {'name': 'health care', 's': 'weapon store', 'e': 'discussion camp', 'se': 'centre',
                    'text': 'You are in the Health care where army forces are getting treated and doctors are moving around\nYou have walls in the north and west direction'},
    'resting camp': {'name': 'resting camp', 's': 'captives', 'w': 'discussion camp', 'sw': 'centre',
                     'text': 'You are in resting camp where the army forces are taking rest and having casual talks\nYou have walls in the north and east direction'},
    'weapon store': {'name': 'weapon store', 'n': 'health care', 's': 'radar', 'e': 'centre', 'ne': 'discussion camp',
                     'se': 'training camp',
                     'text': 'You are in weapon store where army forces are testing out weapons and getting their weapons repaired\nYou have walls in the west direction'},
    'captives': {'name': 'captives', 'n': 'resting camp', 's': 'intel room', 'w': 'centre', 'nw': 'discussion camp',
                 'sw': 'training camp',
                 'text': 'You are in the dark part of the camp , i.e., the captives where intruders are caught, questioned, and tortured to reveal the aim they came in\nYou have walls in the east direction'},
    'radar': {'name': 'radar', 'n': 'weapon store', 'e': 'training camp', 'ne': 'centre',
              'text': 'You are in the radar room where higher officials are in look out for intruders and having the satellites positioned at the enemy bases\nYou have walls in the south and west direction'},
    'training camp': {'name': 'training camp', 'n': 'centre', 'w': 'radar', 'e': 'intel room', 'nw': 'weapon store',
                      'ne': 'captives',
                      'text': 'You are in the training camp where army forces are getting trained and trying out the weapons\nYou have walls in the south direction'},
    'intel room': {'name': 'intel room', 'n': 'captives', 'w': 'training camp', 'nw': 'centre',
                   'text': 'You are in the intel room where confidential information is exchanged with the officials of the army\nYou have walls in the south and east direction'}}
direction = ['n', 's', 'e', 'w']
current_room = rooms['centre']
rooms_reached = 0

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
action = ''
key = False
weapon = False
reload = False
killed = False
unlocked = False
done = False

#image =pygame.image.load(r'C:\Users\user\Desktop\0001.jpg')
"""def textbox(var, avai_list):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            var = textx.lower()
            if var in avai_list:
                if var in current_room:
                    current_room = rooms[current_room[movement]]
                else:
                    invalid1()
            else:
                invalid2()
            textx = ''
        elif event.key == pygame.K_BACKSPACE:
            textx = textx[:-1]"""


def HealthCare():
    pygame.draw.rect(screen, yellow, (53, 53, 195, 145))
    screen.blit(text1, (80, 115))
    screen.blit(text12, (750, 450))
    screen.blit(text13, (750, 465))
    screen.blit(text14, (750, 480))
    screen.blit(text15, (750, 495))
    screen.blit(text16, (750, 510))


def DiscussionCamp():
    pygame.draw.rect(screen, yellow, (253, 53, 195, 145))
    screen.blit(text2, (255, 115))
    screen.blit(text22, (750, 450))
    screen.blit(text23, (750, 465))
    screen.blit(text24, (750, 480))
    screen.blit(text25, (750, 495))
    screen.blit(text26, (750, 510))


def RestingCamp():
    pygame.draw.rect(screen, yellow, (453, 53, 195, 145))
    screen.blit(text3, (475, 115))
    screen.blit(text17, (750, 450))
    screen.blit(text18, (750, 465))
    screen.blit(text19, (750, 480))
    screen.blit(text20, (750, 495))
    screen.blit(text21, (750, 510))


def WeaponStore():
    pygame.draw.rect(screen, yellow, (53, 203, 195, 145))
    screen.blit(text4, (70, 275))
    screen.blit(text27, (750, 450))
    screen.blit(text28, (750, 465))
    screen.blit(text29, (750, 480))
    screen.blit(text30, (750, 495))
    screen.blit(text31, (750, 510))


def Centre():
    pygame.draw.rect(screen, yellow, (253, 203, 195, 145))
    screen.blit(text5, (275, 250))
    screen.blit(text55, (750, 450))
    screen.blit(text56, (750, 465))
    screen.blit(text57, (750, 480))
    screen.blit(text58, (750, 495))


def Captives():
    pygame.draw.rect(screen, yellow, (453, 203, 195, 145))
    screen.blit(text6, (495, 267))
    screen.blit(text32, (750, 450))
    screen.blit(text33, (750, 465))
    screen.blit(text34, (750, 480))
    screen.blit(text35, (750, 495))
    screen.blit(text36, (750, 510))
    screen.blit(text37, (750, 525))


def Radar():
    pygame.draw.rect(screen, yellow, (53, 353, 195, 145))
    screen.blit(text7, (120, 420))
    screen.blit(text38, (750, 450))
    screen.blit(text39, (750, 465))
    screen.blit(text40, (750, 480))
    screen.blit(text41, (750, 495))
    screen.blit(text42, (750, 510))
    screen.blit(text43, (750, 525))
    screen.blit(text44, (750, 540))


def TrainingCamp():
    pygame.draw.rect(screen, yellow, (253, 353, 195, 145))
    screen.blit(text8, (270, 415))
    screen.blit(text45, (750, 450))
    screen.blit(text46, (750, 465))
    screen.blit(text47, (750, 480))
    screen.blit(text48, (750, 495))
    screen.blit(text49, (750, 510))


def IntelRoom():
    pygame.draw.rect(screen, yellow, (453, 353, 195, 145))
    screen.blit(text9, (495, 415))
    screen.blit(text50, (750, 450))
    screen.blit(text51, (750, 465))
    screen.blit(text52, (750, 480))
    screen.blit(text53, (750, 495))
    screen.blit(text54, (750, 510))

def invalid1():
    screen.blit(text60,(750,200))

def invalid2():
    screen.blit(text61,(750,200))


def task_center():
    screen.blit(text64, (750,30))


def task_intelroom():
    global key
    screen.blit(text65, (750, 30))
    screen.blit(text66, (750, 50))
    screen.blit(text67, (750, 70))
    screen.blit(text120, (750, 90))
    screen.blit(text121, (750, 110))
    if action == 'pick key':
        task_intelroom1()
        key = True


def task_weaponstore():
    global weapon
    screen.blit(text69, (750, 60))
    screen.blit(text70, (750, 75))
    if action == 'pick':
        task_weaponstore1()
        weapon = True

def task_trainingcamp():
    global reload
    screen.blit(text71, (750, 30))
    screen.blit(text72, (750, 50))
    if action == 'reload':
        task_trainingcamp1()
        reload = True


def task_discussioncamp():
    screen.blit(text100, (750, 60))
    screen.blit(text101, (750, 75))
    screen.blit(text102, (750, 90))


def task_radarroom():
    screen.blit(text103, (750, 60))
    screen.blit(text104, (750, 75))
    screen.blit(text106, (750, 90))


def task_captives():
    global killed, unlocked
    screen.blit(text107, (750, 60))
    screen.blit(text108, (750, 75))
    if action == 'kill' and weapon and reload:
        task_captives1()
        killed = True
    if action == 'unlock' and key and killed:
        task_captives2()
        unlocked = True
    if action == 'escape' and unlocked:
        gameover()


def task_intelroom1():
    screen.blit(text122, (750, 150))
    screen.blit(text123, (750, 170))

def task_weaponstore1():
    screen.blit(text124, (750, 150))
    screen.blit(text125, (750, 170))
    screen.blit(text126, (750, 190))

def task_trainingcamp1():
    screen.blit(text73, (750, 150))
    screen.blit(text74, (750, 170))
    screen.blit(text75, (750, 190))
    screen.blit(text76, (750, 210))
    screen.blit(text77, (750, 230))


def task_captives1():
    screen.blit(text109, (750, 150))
    screen.blit(text110, (750, 170))
def task_captives2():
    screen.blit(text111, (750, 190))
    screen.blit(text112, (750, 210))


def gameover():
    global done
    done = True
    screen.fill(white)
    screen.blit(text1000, (90, 20))

screen = pygame.display.set_mode((1024, 600))
screen.fill((255, 255, 255))

fontx = pygame.font.Font(None, 32)
input_box = pygame.Rect(500, 100, 140, 32)
color = pygame.Color('dodgerblue2')
textx = ''

font = pygame.font.Font("freesansbold.ttf", 32)
font1 = pygame.font.Font("freesansbold.ttf", 45)
font2 = pygame.font.Font("freesansbold.ttf", 23)
font3 = pygame.font.Font("freesansbold.ttf", 22)
font4 = pygame.font.Font("freesansbold.ttf", 15)

text = font.render("MAP", 1, red)
text1 = font2.render("Health Care", 1, black)
text2 = font3.render("Discussion Camp", 1, black)
text3 = font2.render("Resting camp", 1, black)
text4 = font2.render("Weapon store", 1, black)
text5 = font1.render("Centre", 1, black)
text6 = font2.render("Captives", 1, black)
text7 = font2.render("Radar", 1, black)
text8 = font2.render("Training camp", 1, black)
text9 = font2.render("Intel room", 1, black)
#text10 = font2.render("RESET", 1, black)
text11 = font2.render("DESCRIPTION", 1, black)
text12 = font4.render('You are in the Health care', 1, black)
text13 = font4.render('where army forces are getting', 1, black)
text14 = font4.render('treated and doctors are moving', 1, black)
text15 = font4.render('around. You have walls in', 1, black)
text16 = font4.render('the north and west direction', 1, black)

text17 = font4.render('You are in resting camp', 1, black)
text18 = font4.render('where the army forces are', 1, black)
text19 = font4.render('taking rest and having casual', 1, black)
text20 = font4.render('talks. You have walls in the north', 1, black)
text21 = font4.render('and east direction', 1, black)

text22 = font4.render('You are in the Discussion camp', 1, black)
text23 = font4.render('where the army head and', 1, black)
text24 = font4.render('the force head are having a', 1, black)
text25 = font4.render('meeting. You have walls in the', 1, black)
text26 = font4.render('north direction', 1, black)

text27 = font4.render('You are in weapon store where', 1, black)
text28 = font4.render('army forces are testing out', 1, black)
text29 = font4.render('weapons and getting their weapons', 1, black)
text30 = font4.render('repaired. You have walls in the', 1, black)
text31 = font4.render('west direction', 1, black)

text32 = font4.render('You are in the dark part of the', 1, black)
text33 = font4.render('camp , i.e., the captives where', 1, black)
text34 = font4.render('intruders are caught, questioned,', 1, black)
text35 = font4.render('and tortured to reveal the', 1, black)
text36 = font4.render('aim they came in. You have', 1, black)
text37 = font4.render('walls in the east direction', 1, black)

text38 = font4.render('You are in the radar room', 1, black)
text39 = font4.render('where higher officials are in', 1, black)
text40 = font4.render('look out for intruders and', 1, black)
text41 = font4.render('having the satellites positioned', 1, black)
text42 = font4.render('at the enemy bases. You have', 1, black)
text43 = font4.render('walls in the south and', 1, black)
text44 = font4.render('west direction', 1, black)

text45 = font4.render('You are in the training camp', 1, black)
text46 = font4.render('where army forces are getting', 1, black)
text47 = font4.render('trained and trying out the', 1, black)
text48 = font4.render('weapons. You have walls in', 1, black)
text49 = font4.render('the south direction', 1, black)

text50 = font4.render('You are in the intel room where', 1, black)
text51 = font4.render('confidential information is', 1, black)
text52 = font4.render('exchanged with the officials', 1, black)
text53 = font4.render('of the army. You have walls in', 1, black)
text54 = font4.render('the south and east direction', 1, black)

text55 = font4.render('You are in the centre of you', 1, black)
text56 = font4.render('army base camp and under', 1, black)
text57 = font4.render('keen eyes. You can move', 1, black)
text58 = font4.render('around anywhere', 1, black)
text59 = font2.render('INPUT', 1,black)


text60 = font4.render("Invalid move, You have got walls over there",1,red)
text61 = font4.render('Invalid input, Check spelling',1,red)
text62 = font3.render('n,s,e,w',1,black)
text63 = font2.render('Available Movements:',1,black)


text64 = font4.render("Search for intel room",1,black)

text65 = font4.render('Here the officials are talking',1,black)
text66 = font4.render('that high security is present',1,black)
text67 = font4.render('in the captives room.',1,black)
#text68 = font4.render('weapons store and pick the weapon',1,black)
text120 = font4.render('Pick the key to open the',1,black)
text121 = font4.render('Captives Room (Type \"pick key\")',1,black)

text122 = font4.render('You have Successfully picked the Key',1,red)
text123 = font4.render('Now go to the Weapon store',1,red)

text69 = font4.render('You are in the WeaponStore.Now Pick ',1,black)
text70 = font4.render('the necessary weapons(Type \"pick\")',1,black)

text124 = font4.render('You have successfully picked your',1,red)
text125 = font4.render('Weapons.Now go to the training',1,red)
text126 = font4.render('camp to load your weapons',1,red)

text71 = font4.render('You are in the Training camp.',1,black)
text72 = font4.render('To load your weapon type reload.',1,black)

text73 = font4.render('Go to the Dicussion camp',1,red)
text74 = font4.render('to find the place where you can',1,red)
text75 = font4.render('deactivate all Cameras in the',1,red)
text76 = font4.render('base camp without the soldiers',1,red)
text77 = font4.render('getting alerted.',1,red)


text79 = font2.render('TASK:',1,red)

text100 = font4.render('The systems that deactivate ', 1, black)
text101 = font4.render('all cameras are in the radar ', 1, black)
text102 = font4.render('room.  Go to radar room.', 1, black)

text103 = font4.render('You are in the radar room ', 1, black)
text104 = font4.render('Deactivated the cameras. ', 1, black)

text106 = font4.render('Go to captives. ', 1, black)

text107 = font4.render('To kill everyone near the captives',1, black)
text108 = font4.render('room type \"kill\".', 1, black)

text109 = font4.render('To unlock the captives door using', 1, red)
text110 = font4.render('the Key,Type \"unlock\"', 1, red)

text111 = font4.render('You have successfully saved your army', 1, red)
text112 = font4.render('personnel.To escape Type escape', 1, red)



text1000 = font1.render('Awesome, You Saved him alive',1,black)



while True:

    screen.fill(white)
    screen.blit(text, (325, 2))
    input_box = pygame.Rect(840, 350, 140, 32)

    pygame.draw.line(screen, black, (50, 50), (650, 50), 5)
    pygame.draw.line(screen, black, (50, 50), (50, 500), 5)
    pygame.draw.line(screen, black, (50, 500), (650, 500), 5)
    pygame.draw.line(screen, black, (650, 500), (650, 50), 5)
    pygame.draw.line(screen, black, (250, 50), (250, 500), 5)
    pygame.draw.line(screen, black, (450, 50), (450, 500), 5)
    pygame.draw.line(screen, black, (50, 200), (650, 200), 5)
    pygame.draw.line(screen, black, (50, 350), (650, 350), 5)

    screen.blit(text11, (750, 425))
    screen.blit(text59, (750, 350))
    screen.blit(text62, (750, 325))
    screen.blit(text63, (750, 305))
    screen.blit(text79, (750, 2))

    pygame.draw.line(screen, black, (700, 0), (700, 600), 10)

    #pygame.draw.rect(screen, yellow, (840, 500, 100, 50))
    #screen.blit(text10, (850, 510))

    if current_room['name'] == 'intel room' and rooms_reached == 0:
        rooms_reached = 1
    elif current_room['name'] == 'weapon store' and rooms_reached==1:
        rooms_reached = 2
    elif current_room['name'] == 'training camp' and rooms_reached==2:
        rooms_reached = 3
    elif current_room['name'] == 'discussion camp' and rooms_reached==3:
        rooms_reached = 4
    elif current_room['name'] == 'radar' and rooms_reached==4:
        rooms_reached = 5
    elif current_room['name'] == 'captives' and rooms_reached==5:
        rooms_reached = 6







    if current_room['name'] == 'centre':
        Centre()
    elif current_room['name'] == 'discussion camp':
        DiscussionCamp()
    elif current_room['name'] == 'health care':
        HealthCare()
    elif current_room['name'] == 'resting camp':
        RestingCamp()
    elif current_room['name'] == 'weapon store':
        WeaponStore()
    elif current_room['name'] == 'captives':
        Captives()
    elif current_room['name'] == 'radar':
        Radar()
    elif current_room['name'] == 'training camp':
        TrainingCamp()
    elif current_room['name'] == 'intel room':
        IntelRoom()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if textx.lower() in ['pick', 'reload', 'escape', 'kill', 'pick key', 'unlock']:
                        action = textx
                movement = textx.lower()
                if movement in direction:
                    if movement in current_room:
                        current_room = rooms[current_room[movement]]
                    else:
                        invalid1()
                else:
                    invalid2()
                textx = ''
            elif event.key == pygame.K_BACKSPACE:
                textx = textx[:-1]


            else:
                textx += event.unicode

    # Render the current text.
    txt_surface = fontx.render(textx, True, (0, 0, 0))

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)

    if rooms_reached == 0:
        task_center()
    elif rooms_reached == 1:
        task_intelroom()
        #lost_screen()
    elif rooms_reached == 2:
        task_weaponstore()
    elif rooms_reached == 3:
        task_trainingcamp()
    elif rooms_reached == 4:
        task_discussioncamp()
    elif rooms_reached == 5:
        task_radarroom()
    elif rooms_reached == 6:
        task_captives()



    pygame.display.flip()