import pygame
from moviepy.editor import *
from random import randint
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("English project")


clip = VideoFileClip(r"start_video.mp4")
clip.preview()
jump = pygame.mixer.Sound('jump.wav')
bad = pygame.mixer.Sound('bad.wav')
new_part = pygame.mixer.Sound('new_part.mp3')
good_result = pygame.mixer.Sound('ura.wav')

pygame.mixer.music.load("background_misic.wav")
pygame.mixer.music.play(-1)

win = pygame.display.set_mode((700,700))
walkRight = [pygame.image.load('sprites/pygame_right_1.png'), 
pygame.image.load('sprites/pygame_right_2.png'), 
pygame.image.load('sprites/pygame_right_3.png'),
 pygame.image.load('sprites/pygame_right_4.png'), 
 pygame.image.load('sprites/pygame_right_5.png'), 
 pygame.image.load('sprites/pygame_right_6.png')]
walkLeft = [pygame.image.load('sprites/pygame_left_1.png'),
 pygame.image.load('sprites/pygame_left_2.png'), 
 pygame.image.load('sprites/pygame_left_3.png'), 
 pygame.image.load('sprites/pygame_left_4.png'), 
 pygame.image.load('sprites/pygame_left_5.png'), 
 pygame.image.load('sprites/pygame_left_6.png')]
bg = pygame.image.load('sprites/background2.jpg')
bg = pygame.transform.scale(bg, (700, 700))
playerStand = pygame.image.load('sprites/_pygame_idle.png')
#загружаем траву
grass = pygame.image.load('sprites/grass/grass.png')
grass = pygame.transform.scale(grass, (1280, 120))
#загружаем деревья
tree = [pygame.image.load('sprites/tree/1.png'),
pygame.image.load('sprites/tree/2.png'),
pygame.image.load('sprites/tree/3.png'),
pygame.image.load('sprites/tree/4.png'),
pygame.image.load('sprites/tree/5.png'),
pygame.image.load('sprites/tree/6.png'),
]

#загружаем солнце
sun = pygame.image.load('sprites/sun.png').convert()
sun = pygame.transform.scale(sun, (1200, 1200))
sun.set_alpha(60)
#загружаем коробку
box_img = pygame.image.load('sprites/box.png')
box_img = pygame.transform.scale(box_img, (75, 75))
#загружаем звуки паузы
pause_pause= pygame.mixer.Sound('Pause setting.wav')
pause_start = pygame.mixer.Sound('Unpause.wav')

clock = pygame.time.Clock()
x = 50
y = 580
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
x_grass_position = [[0,700,700],[True,False,False]]
level = 1
music_level = 50
sentence_for_window_level1 = ""
sentence_for_window_level2 = ""
sentence_for_window_level3 = ""
part = 1
'''
    Размерность каждого слова преложения не привышает 8 символом
'''
poinst = 0
'''
    слова, текущее положение в процентах
'''
box = [
    
]
def points_counter(count):
    global sentence_for_window_level1,sentence_for_window_level2,sentence_for_window_level3
    f1 = pygame.font.Font(None, 40)
    text = f1.render("score:"+str(count), 90, (255, 0, 0))
    text = pygame.transform.rotate(text,0)
    win.blit(text, (550, 30))
    if level == 1:
        f1 = pygame.font.Font(None, 50)
        text = f1.render(str(part)+"."+sentence_for_window_level1, 90, (0, 0, 200))
        win.blit(text, (40, 50))
    if level == 2:
        f1 = pygame.font.Font(None, 50)
        text = f1.render(str(part)+"."+sentence_for_window_level2, 90, (0, 0, 200))
        win.blit(text, (40, 50))
    if level == 3:
        f1 = pygame.font.Font(None, 50)
        text = f1.render(str(part)+"."+sentence_for_window_level3, 90, (0, 0, 200))
        win.blit(text, (40, 50))

db1 = [
            ["demanding applications","требовательные приложения",False, "demanding applications - требовательные приложения"],
            ["full specs","полные характеристики", False, "full specs - полные характеристики"]
        ]
db2 = [
            ["______applications","demanding",False, "demanding applications"],
            ["full _____","specs", False, "full specs"]
        ]
db3 = [
            ["_____ full specs","to run at", False,"to run at full specs" ],
            ["_____ demanding applications","to handle", False, "to handle demanding applications"]
        ]
def sentence(random):
    global level,part,db1,db2,db3
    if level == 1:
        for_return =[]
        if random == True:
            one = randint(0, len(db1)-1)
            two = randint(0,len((db1[one][1].split(" ")))-1)
            for_return = db1[one][1].split(" ")
            return for_return[two]
        else:
            while True:
                one = randint(0, len(db1)-1)
                if db1[one][2] != True:
                    db1[one][2] = True
                    return db1[one]
    if level == 2:
        for_return =[]
        
        if random == True:
            one = randint(0, len(db2)-1)
            return db2[one][1]
        else:
            while True:
                one = randint(0, len(db2)-1)
                if db2[one][2] != True:
                    db2[one][2] = True
                    return db2[one]
    if level == 3:
        for_return =[]
        
        if random == True:
            one = randint(0, len(db3)-1)
            return db3[one][1]
        else:
            while True:
                one = randint(0, len(db3)-1)
                if db3[one][2] != True:
                    db3[one][2] = True
                    return db3[one]
def drow_grass(speed):
    if x_grass_position[1][0] == True and x_grass_position[1][1] == False and x_grass_position[1][2] == False:
        win.blit(grass,(x_grass_position[0][0],580))
        x_grass_position[0][0] -= speed
        if x_grass_position[0][0] < -540:
            x_grass_position[1][1] = True
    if x_grass_position[1][0] == True and x_grass_position[1][1] == True and x_grass_position[1][2] == False:
        win.blit(grass,(x_grass_position[0][0],580))
        win.blit(grass,(x_grass_position[0][1],580))
        x_grass_position[0][0] -= speed
        x_grass_position[0][1] -= speed
        if x_grass_position[0][0] < -1810:
            x_grass_position[1][0] = False
            x_grass_position[1][2] = True
    if x_grass_position[1][0] == False and x_grass_position[1][1] == True and x_grass_position[1][2] == True:
        win.blit(grass,(x_grass_position[0][1],580))
        win.blit(grass,(x_grass_position[0][2],580))
        x_grass_position[0][1] -= speed
        x_grass_position[0][2] -= speed
        if  x_grass_position[0][1] < -1810:
            x_grass_position[0][0] = 700
            x_grass_position[0][1] = 700
            x_grass_position[1][1] = False
            x_grass_position[1][0] = True
    
    if x_grass_position[1][0] == True and x_grass_position[1][1] == False and x_grass_position[1][2] == True:
        win.blit(grass,(x_grass_position[0][2],580))
        win.blit(grass,(x_grass_position[0][0],580))
        x_grass_position[0][2] -= speed
        x_grass_position[0][0] -= speed
        if x_grass_position[0][0] < -540:
            x_grass_position[1][2] = False
            x_grass_position[1][1] = True
            x_grass_position[0][2] = 700

def drow_box_with_word():
    global box
    for a in range(len(box)):
        word = box[a][0]
        persent = box[a][1]
        f1 = pygame.font.Font(None, 27)
        text = f1.render(word, 90, (0, 0, 0))
        text = pygame.transform.rotate(text,45)
        win.blit(box_img,(625-(persent*6.25),580))
        win.blit(text, (625-(persent*6.25), 590))
        box[a][1] +=1
    if len(box) != 0:
        if box [0][1] == 100:
            del box[0]
           

start = False
bum = [False,0]
word_at_the_moment = []
for_next_level = []
def pause():
    f1 = pygame.font.Font(None, 90)
    text = f1.render("PAUSE ", 90, (150, 0, 0))
    text = pygame.transform.rotate(text,0)
    win.blit(text, (250, 300))
    pygame.display.update()
def drawWindow():
    global animCount,poinst,start,box,word_at_the_moment,level,sentence_for_window_level1, part,sentence_for_window_level2,sentence_for_window_level3
    global for_next_level
    win.blit(bg,(0,0))
    drow_grass(10)
    win.blit(sun,(-400,-450))
    points_counter(poinst)
    if start == False:
        if level == 1:
            if part == 1:
                word_at_the_moment = sentence(False)
                sentence_for_window_level1 = word_at_the_moment[0]
                for_next_level.append(word_at_the_moment[0])
                f1 = pygame.font.Font(None, 90)
                text = f1.render("Level 1", 90, (150, 0, 0))
                text = pygame.transform.rotate(text,0)
                win.blit(text, (250, 300))
                f1 = pygame.font.Font(None, 50)
                text = f1.render("Translate the collocation", 90, (0, 0, 0))
                win.blit(text, (175, 360))
                word_at_the_moment = word_at_the_moment[1].split(" ")
                pygame.display.update()
                #не забуть увеличить время задержки
                pygame.time.delay(6000)
                start = True
            else:
                # добавит весёлый звук и паузу 1 - 1.5 секунд
                pygame.mixer.music.pause()
                word_at_the_moment = sentence(False)
                sentence_for_window_level1 = word_at_the_moment[0]
                for_next_level.append(word_at_the_moment[0])
                word_at_the_moment = word_at_the_moment[1].split(" ")
                new_part.play()        
                pygame.display.update()
                pygame.time.delay(2000)
                start = True
                pygame.mixer.music.play(-1)
        else:
            if level == 3:
                if part == 1:
                    i = 0
                    while i < 20:
                        win.blit(bg,(0,0))
                        drow_grass(10)
                        win.blit(sun,(-400,-450))
                        f1 = pygame.font.Font(None, 47)
                        text = f1.render("1."+db2[0][3], 90, (0, 0, 250))
                        win.blit(text, (90, 230))
                        text = f1.render("2."+db2[1][3], 90, (0, 0, 250))
                        win.blit(text, (90, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        i += 1
                        pygame.event.get()
                        pygame.event.pump()
                    #
                    i = 0
                    word_at_the_moment = sentence(False)
                    sentence_for_window_level3 = word_at_the_moment[0]
                    while i < 12:
                        win.blit(bg,(0,0))
                        drow_grass(10)
                        win.blit(sun,(-400,-450))    
                        f1 = pygame.font.Font(None, 90)
                        text = f1.render("Level 3", 90, (150, 0, 0))
                        text = pygame.transform.rotate(text,0)
                        win.blit(text, (250, 300))
                        f1 = pygame.font.Font(None, 50)
                        text = f1.render("Choose the correct verbs", 90, (0, 0, 0))
                        win.blit(text, (175, 360))
                        if i == 0:
                            word_at_the_moment = word_at_the_moment[1].split(" ")    
                        pygame.display.update()
                        #не забуть увеличить время задержки
                        pygame.time.delay(500)
                        i += 1
                        start = True
                        pygame.event.get()
                        pygame.event.pump()
                else:
                    pygame.mixer.music.pause()
                    word_at_the_moment = sentence(False)
                    sentence_for_window_level3 = word_at_the_moment[0]
                    for_next_level[1] = word_at_the_moment[0]
                    word_at_the_moment = word_at_the_moment[1].split(" ")
                    new_part.play()
                    pygame.display.update()
                    pygame.time.delay(2000)
                    start = True
                    pygame.mixer.music.play(-1)
            if level == 4: 
                i = 0
                while i < 20:
                    win.blit(bg,(0,0))
                    drow_grass(10)
                    win.blit(sun,(-400,-450))
                    f1 = pygame.font.Font(None, 47)
                    text = f1.render("1."+db3[0][3], 90, (0, 0, 250))
                    win.blit(text, (90, 230))
                    text = f1.render("2."+db3[1][3], 90, (0, 0, 250))
                    win.blit(text, (90, 265))
                    pygame.display.update()
                    pygame.time.delay(500)
                    pygame.event.get()
                    pygame.event.pump()
                    i += 1
                #  
                i = 0
                while i < 12:
                    win.blit(bg,(0,0))
                    drow_grass(10)
                    win.blit(sun,(-400,-450))
                    #
                    f1 = pygame.font.Font(None, 90)
                    text = f1.render("You win!", 90, (150, 0, 0))
                    text = pygame.transform.rotate(text,0)
                    win.blit(text, (200, 300))
                    pygame.display.update()
                    pygame.time.delay(500)
                    pygame.event.get()
                    pygame.event.pump()
                    i += 1
                exit(0)
            if level == 2:
                if part == 1:
                    i = 0
                    while i < 20:
                        win.blit(bg,(0,0))
                        drow_grass(10)
                        win.blit(sun,(-400,-450))
                        f1 = pygame.font.Font(None, 32)
                        text = f1.render("1."+db1[0][3], 90, (0, 0, 250))
                        win.blit(text, (70, 230))
                        text = f1.render("2."+db1[1][3], 90, (0, 0, 250))
                        win.blit(text, (70, 250))
                        pygame.display.update()
                        pygame.time.delay(500)
                        i += 1
                        pygame.event.get()
                        pygame.event.pump()
                    i = 0
                    word_at_the_moment = sentence(False)
                    sentence_for_window_level2 = word_at_the_moment[0]
                    while i < 12:                        
                        pygame.display.update()
                        
                        win.blit(bg,(0,0))
                        drow_grass(10)
                        win.blit(sun,(-400,-450))
                        f1 = pygame.font.Font(None, 90)
                        text = f1.render("Level 2", 90, (150, 0, 0))
                        text = pygame.transform.rotate(text,0)
                        win.blit(text, (250, 300))
                        f1 = pygame.font.Font(None, 50)
                        text = f1.render("Find the missing word", 90, (0, 0, 0))
                        win.blit(text, (175, 360))
                        if i == 0:
                            for_next_level[0] = word_at_the_moment[0]
                            word_at_the_moment = word_at_the_moment[1].split(" ")
                        pygame.display.update()
                        pygame.time.delay(500)
                        start = True
                        pygame.event.get()
                        pygame.event.pump()
                        i += 1
                else:
                    pygame.mixer.music.pause()
                    word_at_the_moment = sentence(False)
                    sentence_for_window_level2 = word_at_the_moment[0]
                    for_next_level[1] = word_at_the_moment[0]
                    word_at_the_moment = word_at_the_moment[1].split(" ")
                    new_part.play()
                    pygame.display.update()
                    pygame.time.delay(2000)
                    start = True
                    pygame.mixer.music.play(-1)
    # запускаем коробку
    if len(box) < 5:
        if randint(0,100) > 95:
            if len(box) == 0:
                if randint(0,100) > 80:
                    #правильное слово
                    if level == 3:  
                        box.append([" ".join(word_at_the_moment),0])
                        " ".join(word_at_the_moment)
                    else:
                        box.append([str(word_at_the_moment[0]),0])
                        "".join(word_at_the_moment)
                else:
                    if level == 3:
                        box.append([str((sentence(True))),0])
                    else:
                        box.append([str((sentence(True))),0])
            else:
                if box[len(box)-1][1] > 40:
                    if randint(0,100) > 80:
                    #правильное слово
                        if level == 3:  
                            box.append([" ".join(word_at_the_moment),0])
                        else:                    
                            box.append([str(word_at_the_moment[0]),0])
                            "".join(word_at_the_moment)
                    else:
                        if level == 3:
                            box.append([str((sentence(True))),0])
                        else:
                            box.append([str((sentence(True))),0])

    #Проверяем коснулся ли он коробки
    if bum[0] == False:
        for a in range(len(box)):       
            one  = (625-(box[a][1]*6.25)+55)
            two = (625-(box[a][1]*6.25)-55)
            if x < one and x > two and y > 530:
                if box[a][0] == word_at_the_moment[0] or (level == 3 and box[a][0] == " ".join(word_at_the_moment)):       
                    poinst +=1
                    if level == 3:
                        if(part == 1):
                            part += 1
                            start = False
                            good_result.play()
                        else:
                            start = False
                            level += 1
                            good_result.play()
                        del box[a]
                        break
                    del word_at_the_moment[0]
                    if len(word_at_the_moment) == 0 and level != 3:
                        if(part == 1):
                            part += 1
                            start = False

                        else:
                            start = False
                            level += 1
                            part = 1
                        good_result.set_volume(0.3)
                        good_result.play()
                    else:
                        good_result.set_volume(1)
                        good_result.play()
                else:
                    pygame.mixer.music.pause()
                    f1 = pygame.font.Font(None, 90)
                    text = f1.render("Try again ", 90, (150, 0, 0))
                    win.blit(text, (200, 300))
                    pygame.display.update()
                    bad.play()
                    poinst -= 2
                    pygame.time.delay(2000)
                    pygame.mixer.music.play(-1)
                    
                bum[0] = True
                bum[1] = 30
                del box[a]
                break
    else:
        bum[1] -= 1
        if bum[1] == 0:
            bum[0] = False
    drow_box_with_word()
    if animCount + 1 >= 30:
        animCount = 0
    if  left:
        win.blit(walkLeft[animCount // 5],(x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5],(x,y))
        animCount += 1
    else:
        win.blit(playerStand,(x,y))
    pygame.display.update()
pause_status = False
run = True
#название игры
i = 0
while i < 20:
    win.blit(bg,(0,0))
    drow_grass(10)
    win.blit(sun,(-400,-450))
    f1 = pygame.font.SysFont("calisto", 60)
    text = f1.render("UPgrade", 90, (250, 0, 0))
    win.blit(text, (240, 280))
    text = f1.render("IT English", 90, (250, 0, 0))
    win.blit(text, (220, 340))
    print(pygame.font.get_fonts())
    pygame.display.update()
    
    pygame.time.delay(500)
    pygame.event.get()
    pygame.event.pump()
    i += 1
#Меню


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                print("Была зафиксировно нажитие")
                print("Положение i.pos[0]"+str(i.pos[0]))
                print("Положение i.pos[1]"+str(i.pos[1]))
                if (i.pos[0] > 350 and i.pos[0] < 486)  and(i.pos[1] > 209 and i.pos[1] < 230):
                    music_level = 100-((486-i.pos[0])/1.3)
                    print(str(music_level))
                    pygame.mixer.music.set_volume(music_level*0.01)
    clock.tick((15))
    xS = -90
    yS = 0
    win.blit(bg,(0,0))
    drow_grass(10)
    win.blit(sun,(-400,-450))
    f1 = pygame.font.SysFont("calisto", 90)
    text = f1.render("Settings", 90, (250, 0, 0))
    win.blit(text, (225, 90))

    f2 = pygame.font.SysFont("moolboran", 50)
    text = f2.render("Music", 90, (125, 0, 125))
    win.blit(text, (290+xS, 190+yS))

    pygame.draw.rect(win, (220,0,0), pygame.Rect(430+xS,215+yS,150, 10))

    small = pygame.font.SysFont("moolboran", 25)
    text = small.render("quiet", 90, (220, 0, 0))
    win.blit(text, (410+xS, 190+yS))

    small = pygame.font.SysFont("moolboran", 25)
    text = small.render("loud", 90, (220, 0, 0))
    win.blit(text, (570+xS, 190+yS))
    #Рисуем ограничители
    pygame.draw.rect(win, (220,0,0), pygame.Rect(430+xS,210+yS,5, 20))
    pygame.draw.rect(win, (220,0,0), pygame.Rect(575+xS,210+yS,5, 20))
    pygame.draw.rect(win, (102,205,170), pygame.Rect((1.35 * music_level)+440+xS,210+yS,5, 20))

    f2 = pygame.font.SysFont("moolboran", 50)
    text = f2.render("Pause - press P", 90, (225, 99, 71))
    win.blit(text, (290+xS, 230+yS))

    f2 = pygame.font.SysFont("moolboran", 50)
    text = f2.render("Jump - press Space bar", 90, (0, 0, 128))
    win.blit(text, (290+xS, 270+yS))

    f2 = pygame.font.SysFont("moolboran", 50)
    text = f2.render("Move - press Left/Right arrow", 90, (112, 128, 144))
    win.blit(text, (290+xS, 310+yS))

    f2 = pygame.font.SysFont("moolboran", 50)
    text = f2.render("Start game - press Enter", 90, (225, 0, 0))
    win.blit(text, (290+xS, 350+yS))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        break
    pygame.display.update()



while run:
    clock.tick((25))
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False    
    keys = pygame.key.get_pressed()
    if pause_status:
        if keys[pygame.K_p]:
            pause_status = False
            pause_start.play()
            pygame.mixer.music.play(-1)
            pygame.time.delay(200)
        continue
    if keys[pygame.K_p]:
        pause_status = True
        #pause_pause.play()
        pygame.time.delay(200)
        pause()
        pygame.mixer.music.pause()
        continue

    if keys[pygame.K_LEFT] and x  > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 700 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
      
        if keys[pygame.K_SPACE]:
            isJump = True
            jump.play()
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2)/2
            else:
                y -= (jumpCount ** 2)/2

            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()

pygame.quit()


