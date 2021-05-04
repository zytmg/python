import pygame,os
import base64,time
import requests,sys
pygame.init()
canvas = pygame.display.set_mode((1050, 660), 0, 32)
pygame.display.set_caption('人脸识别')
canvas.fill((255,255,255))

fileList = []   # 图片路径列表
def fillText(text,position):
    #设置字体
    TextFont = pygame.font.Font('font/simhei.ttf',50)
    #设置字体其他样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)
def fillText_b(text,position):
    #设置字体
    TextFont = pygame.font.Font('font/simhei.ttf',80)
    #设置字体其他样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)
# 图片缩放尺寸方法
# 图片路径列表
text = []
bg = pygame.image.load("images/bg.png")

#选择图片函数
def selectPhoto():
    pygame.display.update()
    file = 'photo.png'
    if len(file) > 0:   #判断是否选择图片“0”为取消
        fileList.append(file) # 将选中图片添加到列表中
    length = len(fileList)
    if length > 1:
         msg = messagebox.showwarning(title='请注意', message='最多选择1张照片')
    this = pygame.image.load(file)
    canvas.blit(this,(50,110))
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=9sMtLGSLzd8S3nyELphnI0ny&client_secret=j7SmmK8nOp9LQkj9wYcOyAjGibPXfn7m'
    response = requests.get(host)
    content = response.json()
    content = content['access_token']
    return content


def getData():
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    token = getToken()
    params = {'access_token': token}
    for imgUrl in fileList:
        f = open(imgUrl, 'rb')
        temp = f.read()
        image = base64.b64encode(temp)
        data = {
            'image':image,
            'image_type':'BASE64',
            'face_field':'age,gender,face_shape,beauty,mask,expression,face_type'
        }
        response = requests.post(requestUrl, params=params, data=data)
        content = response.json()
        age = content['result']['face_list'][0]['age']  # 人脸得分
        gender = content['result']['face_list'][0]['gender']['type']
        shape = content['result']['face_list'][0]['face_shape']['type']
        beauty = content['result']['face_list'][0]['beauty']
        mask = content['result']['face_list'][0]['mask']['type']
        expression = content['result']['face_list'][0]['expression']['type']
        face_type = content['result']['face_list'][0]['face_type']['type']
        if gender == 'male':
            gender='男'
        else:
            gender='女'
        if shape == 'square':
            shape = '国字脸'
        elif shape == 'triangle':
            shape = '瓜子脸'
        elif shape == 'oval':
            shape = '鹅蛋脸'
        elif shape == 'heart':
            shape = '心形脸'
        else:
            shape = '圆形脸'
        if mask == 0:
            mask = '没戴口罩'
        else:
            mask = '有戴口罩'
        if expression == 'none' or expression == '0':
            expression = '不笑'
        elif expression == 'smile':
            expression = '微笑'
        else:
            expression = '大笑'
        if face_type == 'human':
            face_type = '真实人脸'
        else:
            face_type = '卡通人脸'
        text.append(gender)
        text.append(shape)
        text.append(age)
        text.append(mask)
        text.append(beauty)
        text.append(expression)
        text.append(face_type)
        fillText_b('人脸检测与属性分析',(160,10))
        fillText('性别:'+str(text[0]),(700,109))
        fillText('脸型:'+str(text[1]),(700,183))
        fillText('年龄:'+str(text[2]),(700,257))
        fillText('口罩:'+str(text[3]),(700,331))
        fillText('颜值:'+str(text[4]),(700,405))
        fillText('笑容:'+str(text[5]),(700,479))
        fillText('人物:'+str(text[6]),(700,553))
canvas.blit(bg,(0,0))
selectPhoto()
getData()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            with open("filename.txt", 'r+') as file:
                file.truncate()
    pygame.display.update()