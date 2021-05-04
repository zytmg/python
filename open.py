import sys
import os
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self, name = 'MainForm'):
        super(MainForm,self).__init__()
        self.setWindowTitle(name)
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.resize(300,50)   # 设置窗体大小
        # btn 1
        self.btn_chooseFile = QPushButton(self)  
        self.btn_chooseFile.setObjectName("btn_chooseFile")  
        self.btn_chooseFile.setText("选取文件")
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn_chooseFile)
        self.setLayout(layout)
        # 设置信号
        self.btn_chooseFile.clicked.connect(self.slot_btn_chooseFile)
    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "照片 (*.png;*.jpeg;*.jpg)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return
        else:
            with open('filename.txt','w',encoding='utf-8') as f:
                f.write(fileName_choose)
            os.system("python index2.py")
            sys.exit()
if __name__=="__main__":
    app = QApplication(sys.argv)
    mainForm = MainForm('选择文件')
    mainForm.show()
    sys.exit(app.exec_())