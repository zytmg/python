import PyQt5,time,os,sys
from bs4 import BeautifulSoup
import requests,pygame
canvas = pygame.display.set_mode((1050,660))
canvas.fill((255,255,255))
pygame.display.set_caption('人脸识别')
bg = pygame.image.load("images/bg.jpg")
app = pygame.image.load("images/app.png")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'https://ai.baidu.com/tech/face/detect'
response = requests.get(url,headers=headers)
while True:
    canvas.blit(bg,(0,0))
    canvas.blit(app,(940,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    time. sleep(5)
    os.system("python home2.py")
    sys.exit()