import sys, os, re
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from datetime import datetime
from shutil import copyfile
import exhibit_recognizer
import cv2

sys.path.insert(0, 'GUI')

import MainWindow
import LoginWindow
import AddExhibit
import Info

sys.path.insert(0, 'infrastructure')

from CSVDatabase import CSVDatabase
from Data_types.Exhibit import Exhibit

path = 'infrastructure/Database/'

# функция, которая создает id для нового объекта
def GetNewID():
    newID = str(datetime.now())
    newID = newID.replace('-', '')
    newID = newID.replace(' ', '')
    newID = newID.replace(':', '')
    newID = newID.replace('.', '')
    return newID

class StartWin(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(self.size())
        self.login.clicked.connect(self.logBtn)
        self.qr.clicked.connect(self.cryptQR)
        self.recognizer.clicked.connect(self.exhibitRecognizer)
        self.setItems()
        
    def setItems(self):
        CSV = CSVDatabase()
        exs = CSV.getAllExhibits()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        # self.tableWidget.verticalHeader().hide() # скрыть нумерацию строк
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # запрет редактирования
        self.tableWidget.setHorizontalHeaderLabels(['Exhibit ID', 'Name',
                                                    'Century'])
        for ex in exs:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0,
                                     QtWidgets.QTableWidgetItem(ex.ex_id))
            self.tableWidget.setItem(rowPosition, 1,
                                     QtWidgets.QTableWidgetItem(ex.name))
            self.tableWidget.setItem(rowPosition, 2,
                                     QtWidgets.QTableWidgetItem(ex.century))
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnWidth(0, 130)
        self.tableWidget.setColumnWidth(1, 243)
        self.tableWidget.setColumnWidth(2, 60)
        
    def logBtn(self):
        self.logWin = LoginWin()
        self.logWin.show()
        self.close()
        
    def exhibitRecognizer(self):
        tpls = []
        result = []
        returned = []
        resArr = []
        for i in os.listdir('infrastructure/Database/Img/'):
            if (re.fullmatch('\d+img\D+', i)):
                tpls.append(os.path.join('infrastructure/Database/Img/', i))
        parameters = {'exhibits' : tpls, 'kneighbours' : 2, 'coefficient' : 0.75, 'detector' : 'ORB'}
        l = len(tpls)
        if (l == 0):
            print("Should be one or more exhibits")
            return -1
        
        for i in range(l):
            result.append(0)
            resArr.append(0)
            
        cap = cv2.VideoCapture("https://192.168.42.129:8080/video")
        recognizer = exhibit_recognizer.ExhibitRecognizer.create('bfmatcher', parameters)
        _, frame = cap.read()
        ym, xm, _ = frame.shape
        
        for i in range(1, 50):
            cv2.rectangle(frame, (xm//2 - 110, ym//2 - 150), 
                                 (xm//2 + 110, ym//2 + 145), (0, 255, 255))
            cv2.imshow('Recognize', frame)
            key = cv2.waitKey(100)
            if (key == 27):
                cap.release()
                cv2.destroyAllWindows()
                return -1
            
            _, frame = cap.read()
            
        while(True):
            _, frame = cap.read()
            cropFrame = frame[ym//2 - 170 : ym//2 + 170,
                                  xm//2 - 120 : xm//2 + 120]
            cv2.rectangle(frame, (xm//2 - 110, ym//2 - 150), 
                                 (xm//2 + 110, ym//2 + 145), (0, 255, 255))
            returned = recognizer.recognize(cropFrame)
            cv2.imshow('Recognize', frame)
            key = cv2.waitKey(100)
            for i in range(l):
                resArr[i] = resArr[i] + returned[i]
            if max(resArr) > 500:
                break
            print(resArr)
            if (key == 27):
                cap.release()
                cv2.destroyAllWindows()
                return -1
        ID = resArr.index(max(resArr))
        cv2.destroyAllWindows()
        res = tpls[ID][len(tpls[i]) - 27 : len(tpls[i]) - 7]
        print(res)
        return res
        
    def cryptQR(self):
        cap = cv2.VideoCapture("http://192.168.42.129:8080/video")
        detector = cv2.QRCodeDetector()
        while(True):
            _, frame = cap.read()
            cv2.imshow('Detector', frame)
            key = cv2.waitKey(100)
            if (key == 27):
                cap.release()
                cv2.destroyAllWindows()
                return -1
            
            data, _, _ = detector.detectAndDecode(frame)
            if (len(data)):
                print(data)
                cv2.destroyAllWindows()
                return(data)
                
class LoginWin(QtWidgets.QMainWindow, LoginWindow.Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.setFixedSize(self.size())  
        self.ok.clicked.connect(self.Ok)
        
    def Ok(self):
        #Здесь должна быть функция проверки логина и пароля, если ок, то выполняем следующее
        if ((self.lineEditLogin.text() == 'l')&(self.lineEditPass.text() == 'p')):
            self.addExh = AddExh()
            self.addExh.show()
            self.close()
        else:
            self.labelError.setText('Incorrect login or password')
            
class AddExh(QtWidgets.QMainWindow, AddExhibit.Ui_AddExhibit):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.setFixedSize(self.size())  
        self.selectImage.clicked.connect(self.selectImgBtn)
        self.selectInfo.clicked.connect(self.selectInfoBtn)
        self.add.clicked.connect(self.addEx)
        
    def closeEvent(self, event):
        self.startWin = StartWin()
        self.startWin.show()
        event.accept()
        
    def selectInfoBtn(self):
        self.infoFilePath = QFileDialog.getOpenFileName(self, 'Open info file', '', '*.txt')[0]
        
    def selectImgBtn(self):
        self.imgFilePath = QFileDialog.getOpenFileName(self, 'Open image file', '', '*.jpg')[0]
        
    def addEx(self):
        ex_id = GetNewID()
        name = self.lineEditName.text()
        century = self.lineEditCentury.text()
        image_path = ex_id + 'img'
        info_path = ex_id + 'info'
        ex = Exhibit(ex_id, name, century, image_path, info_path)
        CSV = CSVDatabase()
        if (CSV.addExhibit(ex) == -1):
            self.label1.setText('This exhibit already exists')
        else:
            copyfile(self.infoFilePath, 'infrastructure/Database/Info/' +
                     info_path + '.txt')
            copyfile(self.imgFilePath, 'infrastructure/Database/Img/' +
                     image_path + '.jpg')
            self.label1.setText('Success!')
            
class Info(QtWidgets.QMainWindow, Info.Ui_Info):
    def __init__(self, ex_id):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(self.size())
        CSV = CSVDatabase()
        ex = CSV.getExhibit(ex_id)
        if (ex == -1):
            self.info.setText('There is no exhibit with this id')
        else:
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 15, QtGui.QFont.Bold))
            self.info.append('NAME: ')
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 13, QtGui.QFont.Normal))
            self.info.append(ex.name + '\n')
            #
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 15, QtGui.QFont.Bold))
            self.info.append('CENTURY: ')
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 13, QtGui.QFont.Normal))
            self.info.append(ex.century + '\n')
            #
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 15, QtGui.QFont.Bold))
            self.info.append('INFORMATION:')
            self.info.setCurrentFont(QtGui.QFont('Times New Roman', 13, QtGui.QFont.Normal))
            with open(path + 'Info/' + ex.info_path + '.txt', 'r') as fInfoR:
                self.info.append(fInfoR.read())
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StartWin()
    # window = Info(1)
    window.show()
    app.exec_()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':  
    main()
    