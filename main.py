#pyuic5 maingui.ui -o MainWindow.py

#https://d3rlna7iyyu8wu.cloudfront.net/skip_armstrong/skip_armstrong_stereo_subs.m3u8

import sys
from PyQt5 import QtWidgets, uic

import shutil
import os
import random
import subprocess


import re
import time
import threading


from MainWindow import Ui_MainWindow

def cmd2(cmd):
    os.system(cmd)
    print("Running")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.downloadFile)
        self.pushButton_2.clicked.connect(self.addDes)
        self.pushButton_4.clicked.connect(self.copyByFileNameList)
        self.pushButton_3.clicked.connect(self.addPath)
        self.pushButton_5.clicked.connect(self.selectFile)
        


    def showMsg(self):
        print(self.lineEdit.text())
    def addPath(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEdit_2.setText(folderpath)
        print(folderpath)
    def addDes(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lineEdit.setText(folderpath)
        print(folderpath)


    def runCmd(self, cmd):
        msg = os.system(cmd)
        print(msg)
        #make for run new thread to download

    def downloadFile(self, linkUrl):
        #link = self.lineEdit.text()
        data = str(self.plainTextEdit.toPlainText())
        data = re.sub('"', '', data)
        #print(data)
        arr = data.splitlines()
        dst = self.lineEdit.text()
        print(arr)
        self.copybypath(arr, dst)
        #folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        
    def copyByFileNameList(self):
        data = str(self.plainTextEdit_2.toPlainText())
        data = re.sub('"', '', data)
        #print(data)
        arr = data.splitlines()
        folderName = self.lineEdit_2.text()
        filePathArr = []
        for i in arr:
            filePathArr.append(folderName+ '\\' + i)
            
        dst = self.lineEdit.text()
        self.copybypath(filePathArr, dst)
    
        
    def copybypath(self, pathArr, dst):
        for src in pathArr:
            try:
                echo = shutil.copy2(src, dst)
                print(echo)
            except :
                self.label.setText('ERROR : ' + src)
                pass
            
    def selectFile(self):
        subprocess.Popen(r'explorer /select,"D:\\DEV\\copy multiple file\\sssss.txt", "D:\\DEV\\copy multiple file\\dd.txt"')
        pass
            
            
        
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()