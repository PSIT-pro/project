import pygame
from random import randint

time_clocks = pygame.time.Clock()
#ทดสอบ 6

#เซตหน้าจอ
pygame.init()
width_screen = 1366
height_screen = 768

#เซตอัพหน้าต่าง window
ic = pygame.image.load("core/icon.jpg")
game_layout_display = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Snake Snake Fish Fish")
pygame.display.set_icon(ic)
pygame.display.update()

#รูปประกอบทั้งหมด

#รูปกระดาน
mainboard = pygame.image.load("set1/border.png")

#รูปลูกเต๋า 6 แบบ
d1 = pygame.image.load("set1/dice_image1.png")
d2 = pygame.image.load("set1/dice_image2.png")
d3 = pygame.image.load("set1/dice_image3.png")
d4 = pygame.image.load("set1/dice_image4.png")
d5 = pygame.image.load("set1/dice_image5.png")
d6 = pygame.image.load("set1/dice_image6.png")

#ภาพตัวหมาก 4 สี
red_c = pygame.image.load("set1/redfish.png")
yellow_c = pygame.image.load("set1/yellowfish.png")
green_c = pygame.image.load("set1/greenfish.png")
blue_c = pygame.image.load("set1/bluefish.png")

#หน้าเมนู
menu_background = pygame.image.load("set1/BGgreen.jpg")
post = pygame.image.load("set1/BGgreen.jpg")

#พื้นหลังหน้าโหลด
initial_background = pygame.image.load("set1/click5.jpg")
initial_background2 = pygame.image.load("set1/click1.jpg")
initial_background3 = pygame.image.load("set1/click2.jpg")
initial_background4 = pygame.image.load("set1/click3.jpg")
initial_background5 = pygame.image.load("set1/click4.jpg")

#หน้าชนะ
win1 = pygame.image.load("set1/redwin.jpg")
win2 = pygame.image.load("set1/yellowwin.jpg")
win3 = pygame.image.load("set1/greenwin.jpg")
win4 = pygame.image.load("set1/bluewin.jpg")

#เครดิต
creditations1 = pygame.image.load("set1/end.jpg")

#รายชื่อ
name = pygame.image.load("set1/end.jpg")

#เพลงประกอบ
pygame.mixer.music.load("sound/BGsong.wav")
snake_sound = pygame.mixer.Sound("sound/snake2.wav")
win = pygame.mixer.Sound("sound/win.wav")
lose = pygame.mixer.Sound("sound/lose.wav")
ladder = pygame.mixer.Sound("sound/ladder2.wav")

#ตำแหน่งเมาส์
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

#เซตสี
black_color = (10, 10, 10)
white_color = (250, 250, 250)
red_color = (200, 0, 0)
blue_red_color = (240, 0, 0)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
purple_color = (43, 3, 132)
blue_purple_color = (60, 0, 190)

# Message displaying for buttons
def message_display_screen(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects_screen(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects_screen(text, font):
    textSurface = font.render(text, True, white_color)
    return textSurface, textSurface.get_rect()


# Message displaying for field
def message_display1_screen(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects1_screen(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


#ตำแหน่งที่หมากแต่ละตัวจะไป เปลี่ยนค่า x,y
def movement(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y

#อักษรที่แจ้งเตือน ตอนตกบันได ตกงู บอกคนชนะ
def text_objects1(text, font):
    textSurface = font.render(text, True, blue_color)
    return textSurface, textSurface.get_rect()

#การทำงานของบันได
def ladders(x):
    if x == 5:
        return 26
    elif x == 33:
        return 47
    elif x == 50:
        return 70
    elif x == 63:
        return 78
    elif x == 73:
        return 92
    else:
        return x

#การทำงานของงู
def snakes(x):
    if x == 23:
        return 2
    elif x == 14:
        return 8
    elif x == 46:
        return 36
    elif x == 58:
        return 43
    elif x == 75:
        return 64
    elif x == 67:
        return 53
    elif x == 99:
        return 83
    else:
        return x

#การทำงานของลูกเต๋า
def dice(d):
    if d == 1: #ทอยได้ 1
        d = d1
    elif d == 2: #ทอยได้ 2
        d = d2
    elif d == 3: #ทอยได้ 3
        d = d3
    elif d == 4: #ทอยได้ 4
        d = d4
    elif d == 5: #ทอยได้ 5
        d = d5
    elif d == 6: #ทอยได้ 6
        d = d6

    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 1000:
        game_layout_display.blit(d, (300, 500))
        pygame.display.update()

#หน้าต่างผู้ชนะ
def winner(w):
    if w == 1: #ผู้เล่น 1 ชนะ
        w = win1
    elif w == 2: #ผู้เล่น 2 ชนะ
        w = win1
    elif w == 3: #ผู้เล่น 3 ชนะ
        w = win1
    elif w == 4: #ผู้เล่น 4 ชนะ
        w = win1

    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 5000:
        game_layout_display.blit(w, (420, 100))
        pygame.display.update()

def button2(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


# Buttons for playing:
def button1(t, xm, ym, x, y, wid, hei, int, after, fast):
    # mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)


#การทอยลูกเต๋า
def turn(sc, lefted, section):
    d = randint(1, 6)  #ระบบสุ่ม
    print(d)
    if d == 6:
        six = True
    else:
        six = False
    p = dice(d)
    sc += d #แต้มรวมของตัวเอง
    if sc <= 100:
        laddle = ladders(sc)  #เช็คกับตำแหน่งบันได
        if laddle != sc:
            lefted = True #ถ้าเป็นจริง จะปรับตำแหน่ง 
            pygame.mixer.Sound.play(ladder)
            time_clock = pygame.time.get_ticks()
            sc = laddle
        sink = snakes(sc) 
        if sink != sc:  #เช็คกับตำแแหน่งงู
            section = True #ถ้าเป็นจริง จะปรับตำแหน่ง
            pygame.mixer.Sound.play(snake_sound)
            sc = sink

    else:  #เงื่อนไขถ้าแต้มเกิน 100 จะไม่เดินให้
        sc = 100
    return sc, lefted, section, six

#กดออกเกม
def Quit():
    pygame.quit()
    quit()

#ฟังค์ชันปุ่ม
def button(t, xm, ym, x, y, wid, hei, int, after, fast, best):
    if x + wid > xm > x and y + hei > ym > y:
        pygame.draw.rect(game_layout_display, after, [x - 2.5, y - 2.5, wid + 5, hei + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if best == 1:
                choice()
            elif best == 5:
                return 5
            elif best == 0:
                Quit()
            elif best == "s" or best == 2 or best == 3 or best == 4:
                return best
            elif best == 7:
                choice()
            else:
                return True

    else:
        pygame.draw.rect(game_layout_display, int, [x, y, wid, hei])
    message_display_screen(t, (x + wid + x) / 2, (y + hei + y) / 2, fast)

#หน้าต่างโหลดการเริ่มเกม
def introduction():
    time_clock = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time_clock < 2500:
        game_layout_display.blit(initial_background, (0, 0))
        pygame.display.update()
    while True:
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background2, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background3, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background4, (0, 0))
            pygame.display.update()
        time_clock = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time_clock < 500:
            game_layout_display.blit(initial_background5, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()

#ปุ่มดูเครดิต
def creditation():
    while True:
        game_layout_display.blit(creditations1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1], 0, 500, 200, 50, red_color, blue_red_color, 25, 20):
            main_menu() #ปุ่มกดกลับหน้าเมนู
        pygame.display.update()

#ปุ่มดูรายชื่อ
def name_list():
    while True:
        game_layout_display.blit(name, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button("Back", mouse[0], mouse[1],0, 500, 200, 50, red_color, blue_red_color, 25, 20):
            main_menu() #ปุ่มกดกลับหน้าเมนู
        pygame.display.update()

#หน้าต่าง Main Menu
def main_menu():
    pygame.mixer.music.play(-1)
    m = True
    while m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#ออกเกม
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_layout_display.blit(menu_background, (0, 0))
        button("Play", mouse[0], mouse[1], 575, 400, 250, 50, green_color, blue_green_color, 35,1)

        button("Quit", mouse[0], mouse[1], 600, 580, 200, 50, red_color, blue_red_color, 25, 0)

        mouse = pygame.mouse.get_pos()
        if button2("Mute Music", mouse[0], mouse[1], 1165, 710, 200, 50, purple_color, blue_purple_color, 25):
            pygame.mixer.music.pause()
        if button2("Play Music", mouse[0], mouse[1], 1165, 650, 200, 50, purple_color, blue_purple_color, 25):
            pygame.mixer.music.unpause()
        if button2("Credits", mouse[0], mouse[1], 600, 460, 200, 50, purple_color, blue_purple_color, 25):
            creditation()
        if button2("Member", mouse[0], mouse[1], 600, 520, 200, 50, purple_color, blue_purple_color, 25):
            name_list()

        pygame.display.update()


#ตั่งค่าเมนู
def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        #ฟังก์ชันการเลือกจำนวนผุ้เล่น
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        best1 = best2 = best3 = best4 = best5 = -1
        game_layout_display.blit(menu_background, (0, 0))
        #ปุ่มเล่น 1 คน
        best1 = button("Single Player", mouse[0], mouse[1], (width_screen / 2 - 150), 250, 300, 50, green_color,
                       blue_green_color, 30, "s")
        #ปุ่มเล่น 2 คน
        best2 = button("2 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 350, 300, 50, green_color,
                       blue_green_color, 30, 2)
        #ปุ่มเล่น 3 คน
        best3 = button("3 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 450, 300, 50, green_color,
                       blue_green_color, 30, 3)
        #ปุ่มเล่น 4 คน
        best4 = button("4 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 550, 300, 50, green_color,
                       blue_green_color, 30, 4)
        #ปุ่มกลับหน้าก่อน
        best5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red_color, blue_red_color, 30, 5)
        if best5 == 5:
            main_menu()
        if best1 == "s":
            playing(21)
        if best2 == 2:
            playing(2)
        if best3 == 3:
            playing(3)
        if best4 == 4:
            playing(4)

        pygame.display.update()

#ระบบการเล่น
def playing(best):
    best6 = -1
    time = 3000
    if best6 == 7:
        choice()
    game_layout_display.blit(post, (0, 0))
    game_layout_display.blit(mainboard, (width_screen / 2 - 250, height_screen / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    game_layout_display.blit(red_c, (xcy, ycy))
    if 5 > best > 1 or best == 21:
        game_layout_display.blit(yellow_c, (xcy, ycy))

    if 5 > best > 2 or best == 21:
        game_layout_display.blit(green_c, (xcg, ycg))

    if 5 > best > 2:
        game_layout_display.blit(blue_c, (xcb, ycb))
    gamer1 = "Player 1"
    gamer1score = 0
    if best == 21:
        gamer2 = "Computer"
        gamer2score = 0
    if 5 > best > 1:
        gamer2 = "Player 2"
        gamer2score = 0
    if 5 > best > 2:
        gamer3 = "Player 3"
        gamer3score = 0
    if 5 > best > 3:
        gamer4 = "Player 4"
        gamer4score = 0
    tips = 1
    play = True
    while True:
        less = False
        set = False
        time = 3000
        game_layout_display.blit(post, (0, 0))
        game_layout_display.blit(mainboard, (width_screen / 2 - 250, height_screen / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        if best == 21:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_color, grey_color, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    if not six:
                        tips += 1
                    xcr, ycr = movement(gamer1score)
                    if gamer1score == 100:
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1_screen("Player 1 Wins", 650, 50, 50, blue_color)
                            x = winner(1)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

            button1("Computer", mouse[0], mouse[1], 400, 700, 200, 50, yellow_color, grey_color, 30)
            if True:
                if tips == 2:
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3 or best == 21:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_display1_screen("Computer Wins", 650, 50, 50, black_color)
                            x = winner(1)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
        if 5 > best > 1:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red_color, grey_color, 30):
                if tips == 1:
                    gamer1score, less, set, six = turn(gamer1score, less, set)
                    xcr, ycr = movement(gamer1score)
                    if not six:
                        tips += 1
                    if gamer1score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_display1_screen("Player 1 Wins", 650, 50, 50, black_color)
                            x = winner(1)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

            if button1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow_color, grey_color, 30):
                if tips == 2:
                    gamer2score, less, set, six = turn(gamer2score, less, set)
                    xcy, ycy = movement(gamer2score)
                    if not six:
                        tips += 1
                        if best < 3:
                            tips = 1

                    if gamer2score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_display1_screen("Player 2 Wins", 650, 50, 50, black_color)
                            x = winner(2)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        if 5 > best > 2:
            if button1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green_color, grey_color, 30):
                if tips == 3:
                    gamer3score, less, set, six = turn(gamer3score, less, set)
                    xcg, ycg = movement(gamer3score)
                    if not six:
                        tips += 1
                        if best < 4:
                            tips = 1

                    if gamer3score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_display1_screen("Player 3 Wins", 650, 50, 50, black_color)
                            x = winner(3)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        if 5 > best > 3:
            if button1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue_color, grey_color, 30):
                if tips == 4:
                    gamer4score, less, set, six = turn(gamer4score, less, set)
                    xcb, ycb = movement(gamer4score)
                    if not six:
                        tips += 1
                        if best < 5:
                            tips = 1

                    if gamer4score == 100:
                        time_clock = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time_clock < 2000:
                            message_display1_screen("Player 4 Wins", 650, 50, 50, black_color)
                            x = winner(4)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        best6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red_color, blue_red_color, 30, 7)
        game_layout_display.blit(red_c, (xcr, ycr))
        if 5 > best > 1 or best == 21:
            game_layout_display.blit(yellow_c, (xcy + 2, ycy))

        if 5 > best > 2:
            game_layout_display.blit(green_c, (xcg + 4, ycg))

        if 5 > best > 3:
            game_layout_display.blit(blue_c, (xcb + 6, ycb))

        if less:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                print("There's a Ladder!")
                message_display1_screen("There's a Ladder!", 650, 50, 35, black_color)
                pygame.display.update()
        if set:
            time_clock = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time_clock < 2000:
                print("There's a Snake!")
                message_display1_screen("There's a Snake!", 650, 50, 35, black_color)
                pygame.display.update()

        time_clocks.tick(7)
        pygame.display.update()
 
introduction()
main_menu()
