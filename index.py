#imports
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
import urllib
from urllib import request
import os
from os import path
import webbrowser
import pafy
from datetime import datetime
import humanize
from PyQt5 import QtCore, QtGui
from datetime import datetime
import time
from main import Ui_MainWindow
from pytube import YouTube
#==============================================
###FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))
class Mainapp(QMainWindow , Ui_MainWindow):
    def __init__(self , parent=None):
        super(Mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.size()
        self.h_title()
        self.connections()
        self.setWindowIcon(QtGui.QIcon('download.png'))
    def yt(self):
        webbrowser.open('https://www.youtube.com/channel/UCNsmcOrb7r3eFeUspoxwspA/')
    def fb(self):
        webbrowser.open('https://www.facebook.com/AmINKwILi/')
    def site(self):
        webbrowser.open('https://ma4rebtech5.blogspot.com/')
    def size(self):
        self.setFixedSize(802,411)
    def Casel(self):
        self.close()
    def h_title(self):
        self.setWindowTitle('Youtube dowloader')
    def progressbar2002(self,blocknum , blocksize ,totoalsize):
        down = blocknum * blocksize
        if totoalsize > 0:
            nisba = down * 100 / totoalsize
            self.progressBar.setValue(nisba)
            #QApplication.processEvents()
    def kwili(self):
        pass

    def get_video_bottom(self):
        try:

            videolink = self.lineEdit_5.text()
            v = pafy.new(videolink)
            i = v.videostreams
            for t in i:
                size = humanize.naturalsize(t.get_filesize())
                nyt = ' {} {} {} {} {}'.format(t.extension,'|',t.quality,'|',size)
                self.comboBox.addItem(nyt)
        except Exception:
            QMessageBox.warning(self, "DOWNLOAD FAILED !! ", "PLEASE ENTER A CORRECT URL  PLEASE TRY AGAIN ❌❌")
            return
    def video_progressbar(self, total, recvd, ratio, rate, eta):
        self.progressBar_2.setValue(ratio * 100)
        #self.lineEdit_10.setText[recvd]
        QApplication.processEvents()
    def ytt_video_bottom(self):
        try:
            videolink = self.lineEdit_5.text()
            saveloCation = self.lineEdit_6.text()
            v = pafy.new(videolink)
            st = v.streams
            dd = self.comboBox.currentIndex()
            iop = st[dd].download(filepath=saveloCation,callback=self.video_progressbar)
        except Exception:
            QMessageBox.warning(self, "DOWNLOAD FAILED !!! ", "THE DOWNLOAD IS FAILED ,PLEASE TRY AGAIN ❌❌")
            return
        QMessageBox.information(self, "DONE...", "The download was successful ✅✅")
        self.lineEdit_6.setText("")
        self.lineEdit_5.setText("")
        self.progressBar_2.setValue(0)
        self.comboBox.clear()
    def connections(self):
        self.pushButton.clicked.connect(self.dowloadbar)
        self.pushButton_2.clicked.connect(self.browa)
        self.pushButton_3.clicked.connect(self.Casel)
        self.pushButton_6.clicked.connect(self.site)
        self.pushButton_5.clicked.connect(self.fb)
        self.pushButton_4.clicked.connect(self.yt)
        self.pushButton_25.clicked.connect(self.get_video_bottom)
        self.pushButton_17.clicked.connect(self.ytt_video_bottom)
        self.pushButton_13.clicked.connect(self.browa2)
        self.pushButton_18.clicked.connect(self.Casel)
        self.pushButton_14.clicked.connect(self.fb)
        self.pushButton_15.clicked.connect(self.yt)
        self.pushButton_16.clicked.connect(self.site)
    def dowloadbar(self):
        # get link - save location - start dowloding
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.progressbar2002)
        except Exception:
            QMessageBox.warning(self,"DOWNLOAD FAILED !! ", "THE DOWNLOAD IS FAILED  PLEASE TRY AGAIN ❌❌")
            return
        QMessageBox.information(self ,"DONE..","The download was successful ✅✅")
        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
    def browa(self):
        saveplace = QFileDialog.getSaveFileName(self, caption=('Save As'), directory=("."),filter=('*.*'))
        text = str(saveplace)
        name = (text[2:].split(',')[0].replace("'", ''))
        self.lineEdit_2.setText(name)
    def browa2(self):
        saveplace = QFileDialog.getExistingDirectory(self, 'Select a Directory')
        self.lineEdit_6.setText(saveplace)
    def browa3(self):
        saveplace = QFileDialog.getExistingDirectory(self, 'Select a Directory')
        self.lineEdit_8.setText(saveplace)
def main():
    app = QApplication(sys.argv)
    window = Mainapp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
#logic






