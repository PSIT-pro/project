import pygame
from random import randint

#หน้าต่างเกม
pygame.init()
screen = pygame.display.set_mode((1366, 768)) #ขนาดจอ
pygame.display.set_caption("ทดสอบระบบ by TonNamXD") #ชื่อหน้าจอ

#หน้าไอคอนเกม
icon = pygame.image.load("pic/icon.jpg") #เลือกรูปไอคอน
pygame.display.set_icon(icon) #เซตรูปไอคอน

#ใส่ฉากหลัง
bg = pygame.image.load("pic/bg-1.png") #เลือกฉากหลัง

#ภาพลูกเต๋า
d1 = pygame.image.load("object/dice_image1.png")
d2 = pygame.image.load("object/dice_image2.png")
d3 = pygame.image.load("object/dice_image3.png")
d4 = pygame.image.load("object/dice_image4.png")
d5 = pygame.image.load("object/dice_image5.png")
d6 = pygame.image.load("object/dice_image6.png")

#ภาพปุ่มสุ่ม
random = pygame.image.load("pic/Random_Button.png")

def dice(d):
    if d == 1:
        return d1
    elif d == 2:
        return d2
    elif d == 3:
        return d3
    elif d == 4:
        return d4
    elif d == 5:
        return d5
    elif d == 6:
        return d6

#ฟังค์ชันปุ่ม
class Button():
    def __init__(self,x,y,image): #รูปปุ่ม
        self.image = pygame.transform.scale(image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):

        pos = pygame.mouse.get_pos()
        
        #เช็คว่าคลิกยัง
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                d = randint(1, 6)
                print(d)
                d = dice(d)
                screen.blit(d,(100, 100))
                pygame.display.update()
                pygame.time.delay(500)

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #ตำแหน่งปุ่ม
        screen.blit(self.image, (100, 500))

random_button = Button(100,500,random)


#เงื่อนไขอีเวนท์ การเปลี่ยนหน้าต่างเกม
while True:

        #คำสั่งในการแสดงฉาก
    screen.blit(bg,(0, 0)) #ให้เริ่มรูปภาพที่ตำแหน่งไหน

    random_button.draw()
    
    #คำสั่งหน้าต่างปิดเกม
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT: #คำสั่งปิดหน้าต่าง
            quit()

    pygame.display.update()