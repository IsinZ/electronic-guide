import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox 
import cv2

sys.path.insert(0, 'GUI')

import MainWindow
import LoginWindow
import AddExhibit
import book_recognizer

class StartWin(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(self.size())
        self.login.clicked.connect(self.logBtn)
        self.qr.clicked.connect(self.cryptQR)
        self.recognizer.clicked.connect(self.bookRecognizer)
        
    def logBtn(self):
        self.logWin = LoginWin()
        self.logWin.show()
        
    def bookRecognizer(self):
        tpls = []
        result = []
        returned = []
        resArr = []
        for i in os.listdir('infrastructure/Database/Books/Covers/'):
            tpls.append(os.path.join('infrastructure/Database/Books/Covers/', i))
        parameters = {'books' : tpls, 'kneighbours' : 2, 'coefficient' : 0.75, 'detector' : 'ORB'}
        l = len(tpls)
        for i in range(l):
            result.append(0)
            resArr.append(0)
            
        cap = cv2.VideoCapture(0)
        recognizer = book_recognizer.BookRecognizer.create('bfmatcher', parameters)
        _, frame = cap.read()
        ym, xm, _ = frame.shape
        
        for i in range(1, 50):
            cv2.rectangle(frame, (xm//2 - 110, ym//2 - 150), 
                                 (xm//2 + 110, ym//2 + 145), (0, 255, 255))
            cv2.imshow('Recognize', frame)
            cv2.waitKey(100)
            _, frame = cap.read()
            
        while(True):
            _, frame = cap.read()
            cropFrame = frame[ym//2 - 170 : ym//2 + 170,
                                  xm//2 - 120 : xm//2 + 120]
            cv2.rectangle(frame, (xm//2 - 110, ym//2 - 150), 
                                 (xm//2 + 110, ym//2 + 145), (0, 255, 255))
            returned = recognizer.recognize(cropFrame)
            out = str(100 * max(resArr) / 400)
            out = out + '%'
            cv2.putText(frame, out, (200, 200), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 255), 2)
            cv2.imshow('Recognize', frame)
            cv2.waitKey(100)
            for i in range(l):
                resArr[i] = resArr[i] + returned[i]
            if max(resArr) > 500:
                ID = resArr.index(max(resArr))
                cv2.destroyAllWindows()
                break
        print(ID, resArr)
        
    def cryptQR(self):
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while(True):
            _, frame = cap.read()
            cv2.imshow('Detector', frame)
            cv2.waitKey(100)
            data, _, _ = detector.detectAndDecode(frame)
            if (len(data)):
                print(data)
                cv2.destroyAllWindows()
                break
                
class LoginWin(QtWidgets.QMainWindow, LoginWindow.Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.setFixedSize(self.size())  
        self.ok.clicked.connect(self.Ok)
        
    def Ok(self):
        #Здесь должна быть функция проверки логина и пароля, если ок, то выполняем следующее
        if ((self.lineEditLogin.text()=='login')&(self.lineEditPass.text() == 'password')):
            self.close()
            self.addExh = AddExh()
            self.addExh.show()
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
        
    def selectInfoBtn(self):
        self.infoFilePath = QFileDialog.getOpenFileName(self, 'Open info file', '', '*.txt')[0]
        
    def selectImgBtn(self):
        self.imgFilePath = QFileDialog.getOpenFileName(self, 'Open image file', '', '*.jpg')[0]

    def addEx(self):
        print(self.lineEditName.text(), '\n')
        print(self.lineEditCentury.text(), '\n')
        print(self.infoFilePath, '\n')
        print(self.imgFilePath, '\n')
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StartWin()  
    window.show() 
    app.exec_()  

if __name__ == '__main__':  
    main()
    