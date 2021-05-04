import cv2,os,easygui
easygui.msgbox('请按a键拍照，再按shift保存照片')
tp = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 打开摄像头
while True:
    ret, frame = tp.read()
    frame = cv2.flip(frame, 1) # 摄像头是和人对立的，将图像左右调换回来正常显示
    cv2.imshow("take phone", frame) # 生成摄像头窗口
    if cv2.waitKey(1) & 0xFF == ord('a'): # 如果按下a 就截图保存并退出
        cv2.imwrite("photo.png", frame) # 保存路径
        os.system("python index1.py")
        break
tp.release()
cv2.destroyAllWindows()