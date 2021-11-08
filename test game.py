import pygame

#หน้าต่างเกม
pygame.init()
screen = pygame.display.set_mode((1366, 768)) #ขนาดจอ
pygame.display.set_caption("ทดสอบระบบ by TonNamXD") #ชื่อหน้าจอ

#หน้าไอคอนเกม
icon = pygame.image.load("icon.jpg") #เลือกรูปไอคอน
pygame.display.set_icon(icon) #เซตรูปไอคอน

#ใส่ฉากหลัง
bg = pygame.image.load("bg.png") #เลือกฉากหลัง

#เงื่อนไขอีเวนท์ การเปลี่ยนหน้าต่างเกม
while True:

    #คำสั่งหน้าต่างปิดเกม
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT: #คำสั่งปิดหน้าต่าง
            quit()

    #คำสั่งในการแสดงฉาก
    screen.blit(bg,(0, 0)) #ให้เริ่มรูปภาพที่ตำแหน่งไหน

    pygame.display.update()