import pygame


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

pygame.init()
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
yellow = (255,255,0)





def HealthCare():
    pygame.draw.rect(screen, yellow, (50, 50, 200, 150))
    screen.blit(text1, (80, 115))
    screen.blit(text12,(750,180))
    screen.blit(text13,(750,200))
    screen.blit(text14,(750,220))
    screen.blit(text15,(750,240))
    screen.blit(text16,(750,260))
    
def DiscussionCamp():
    pygame.draw.rect(screen, yellow, (250, 50, 200, 150))
    screen.blit(text2, (255, 115))
    screen.blit(text22,(750,180))
    screen.blit(text23,(750,200))
    screen.blit(text24,(750,220))
    screen.blit(text25,(750,240))
    screen.blit(text26,(750,260))
def RestingCamp():
    pygame.draw.rect(screen, yellow, (450, 50, 200, 150))
    screen.blit(text3, (475, 115))
    screen.blit(text17,(750,180))
    screen.blit(text18,(750,200))
    screen.blit(text19,(750,220))
    screen.blit(text20,(750,240))
    screen.blit(text21,(750,260))
    
def WeaponStore():
    pygame.draw.rect(screen, yellow, (50, 200, 200, 150))
    screen.blit(text4, (70, 275))
    screen.blit(text27,(750,180))
    screen.blit(text28,(750,200))
    screen.blit(text29,(750,220))
    screen.blit(text30,(750,240))
    screen.blit(text31,(750,260))
    
def Centre():
    pygame.draw.rect(screen, yellow, (250, 200, 200, 150))
    screen.blit(text5, (275, 250))
    screen.blit(text55,(750,180))
    screen.blit(text56,(750,200))
    screen.blit(text57,(750,220))
    screen.blit(text58,(750,240))
    
def Captives():
    pygame.draw.rect(screen, yellow, (450, 200, 200, 150))
    screen.blit(text6, (495, 267))
    screen.blit(text32,(750,180))
    screen.blit(text33,(750,200))
    screen.blit(text34,(750,220))
    screen.blit(text35,(750,240))
    screen.blit(text36,(750,260))
    screen.blit(text37,(750,280))
def Radar():
    pygame.draw.rect(screen, yellow, (50, 350, 200, 150))
    screen.blit(text7, (120, 420))
    screen.blit(text38,(750,180))
    screen.blit(text39,(750,200))
    screen.blit(text40,(750,220))
    screen.blit(text41,(750,240))
    screen.blit(text42,(750,260))
    screen.blit(text43,(750,280))
    screen.blit(text44,(750,300))
def TrainingCamp():
    pygame.draw.rect(screen, yellow, (250, 350, 200, 150))
    screen.blit(text8, (270, 415))
    screen.blit(text45,(750,180))
    screen.blit(text46,(750,200))
    screen.blit(text47,(750,220))
    screen.blit(text48,(750,240))
    screen.blit(text49,(750,260))

def IntelRoom():
    pygame.draw.rect(screen, yellow, (450, 350, 200, 150))
    screen.blit(text9, (495, 415))
    screen.blit(text50,(750,180))
    screen.blit(text51,(750,200))
    screen.blit(text52,(750,220))
    screen.blit(text53,(750,240))
    screen.blit(text54,(750,260))




screen = pygame.display.set_mode((1000,600))
screen.fill((255,255,255))

fontx = pygame.font.Font(None, 32)
input_box = pygame.Rect(500, 100, 140, 32)
color = pygame.Color('dodgerblue2')
textx = ''

font = pygame.font.Font("freesansbold.ttf", 32)
font1 = pygame.font.Font("freesansbold.ttf", 45)
font2 = pygame.font.Font("freesansbold.ttf", 23)
font3 = pygame.font.Font("freesansbold.ttf", 22)
font4 = pygame.font.Font("C:\WINDOWS\FONTS\ARIAL.TTF",15)
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
text10 = font2.render("RESET",1,black)
text11 = font2.render("DESCRIPTION",1,(200, 200, 200))
text12 = font4.render('You are in the Health care' ,1,black)
text13 = font4.render('where army forces are getting',1,black)
text14 = font4.render('treated and doctors are moving',1,black)
text15 =  font4.render('around. You have walls in',1,black)
text16 = font4.render('the north and west direction',1,black)

text17 = font4.render('You are in resting camp',1,black)
text18 = font4.render('where the army forces are' ,1,black)
text19 = font4.render('taking rest and having casual' ,1,black)
text20 = font4.render('talks. You have walls in the north',1,black)
text21 = font4.render('and east direction',1,black)

text22 = font4.render('You are in the Discussion camp' ,1,black)
text23 = font4.render('where the army head and',1,black)
text24 = font4.render('the force head are having a',1,black)
text25 = font4.render( 'meeting. You have walls in the',1,black)
text26 = font4.render('north direction',1,black)

text27 = font4.render('You are in weapon store where',1,black)
text28 = font4.render('army forces are testing out',1,black)
text29 = font4.render('weapons and getting their weapons',1,black)
text30 = font4.render('repaired. You have walls in the',1,black)
text31 = font4.render('west direction',1,black)

text32 = font4.render('You are in the dark part of the',1,black)
text33 = font4.render('camp , i.e., the captives where',1,black)
text34 = font4.render('intruders are caught, questioned,',1,black)
text35 = font4.render('and tortured to reveal the',1,black)
text36 = font4.render('aim they came in. You have',1,black)
text37 = font4.render('walls in the east direction',1,black)

text38 = font4.render('You are in the radar room',1,black)
text39 = font4.render('where higher officials are in',1,black)
text40 = font4.render('look out for intruders and',1,black)
text41 = font4.render('having the satellites positioned',1,black)
text42 = font4.render('at the enemy bases. You have',1,black)
text43 = font4.render('walls in the south and',1,black)
text44 = font4.render('west direction',1,black)

text45 = font4.render('You are in the training camp',1,black)
text46 = font4.render('where army forces are getting',1,black)
text47 = font4.render('trained and trying out the',1,black)
text48 = font4.render('weapons. You have walls in',1,black)
text49 = font4.render('the south direction',1,black)

text50 = font4.render('You are in the intel room where',1,black)
text51 = font4.render('confidential information is',1,black)
text52 = font4.render('exchanged with the officials',1,black)
text53 = font4.render('of the army. You have walls in',1,black)
text54 = font4.render('the south and east direction',1,black)

text55 = font4.render('You are in the centre of you',1,black)
text56 = font4.render('army base camp and under',1,black)
text57 = font4.render('keen eyes. You can move',1,black)
text58 = font4.render('around anywhere',1,black)



                      



while True:
    
    screen.fill(white)
    screen.blit(text, (325,2))
    input_box = pygame.Rect(840, 100, 140, 32)

    pygame.draw.line(screen, black, (50, 50), (650, 50), 5)
    pygame.draw.line(screen, black, (50, 50), (50, 500), 5)
    pygame.draw.line(screen, black, (50, 500), (650, 500), 5)
    pygame.draw.line(screen, black, (650, 500), (650, 50), 5)
    pygame.draw.line(screen, black, (250, 50), (250, 500), 5)
    pygame.draw.line(screen, black, (450, 50), (450, 500), 5)
    pygame.draw.line(screen, black, (50, 200), (650, 200), 5)
    pygame.draw.line(screen, black, (50, 350), (650, 350), 5)
    screen.blit(text1, (80, 115))
    screen.blit(text2, (255, 115))
    screen.blit(text3, (475, 115))
    screen.blit(text4, (70, 275))
    screen.blit(text5, (275, 250))
    screen.blit(text6, (495, 267))
    screen.blit(text7, (120, 420))
    screen.blit(text8, (270, 415))
    screen.blit(text9, (495, 415))
    screen.blit(text11,(750,150))

    pygame.draw.line(screen, black, (700, 0), (700, 600), 10)

    pygame.draw.rect(screen,yellow,(840,500,100,50))
    screen.blit(text10,(850,510))
    
    
    
    

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
                movement = textx.lower()
                if movement in direction:
                    if movement in current_room:
                        current_room = rooms[current_room[movement]]
                    else:
                        print("Invalid move, You have got walls over there")
                else:
                    print('Invalid input, Check spelling')
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
    
    

    pygame.display.flip()
