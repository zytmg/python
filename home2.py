import PyQt5,time,os
from bs4 import BeautifulSoup
import requests,pygame
canvas = pygame.display.set_mode((1050,660))
canvas.fill((255,255,255))
pygame.display.set_caption('人脸识别')
bg = pygame.image.load("images/bg2.png")
button1 = pygame.image.load("images/button1.png")
button2 = pygame.image.load("images/button2.png")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'https://ai.baidu.com/tech/face/detect'
response = requests.get(url,headers=headers)
while True:
    canvas.blit(bg,(0,0))
    canvas.blit(button1,(700,400))
    canvas.blit(button2,(700,500))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #判断是否是鼠标左键被按下
            if event.button == 1:
                #获取鼠标坐标位置
                pos = pygame.mouse.get_pos()
                mouseX = pos[0]
                mouseY = pos[1]
                #判断设定好的点击区域
                if 700 <= mouseX <= 913 and 400 <= mouseY <= 468:
                    # 退出当前界面窗口
                    os.system("python take_phone.py")
                if 700 <= mouseX <= 913 and 500 <= mouseY <= 568:
                    # 退出当前界面窗口
                    os.system("python open.py")
    pygame.display.update()