# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\KONSTANTIN\Documents\ui\AddExhibit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddExhibit(object):
    def setupUi(self, AddExhibit):
        AddExhibit.setObjectName("AddExhibit")
        AddExhibit.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(AddExhibit)
        self.centralwidget.setObjectName("centralwidget")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(25, 40, 50, 15))
        self.labelName.setObjectName("labelName")
        self.labelCentury = QtWidgets.QLabel(self.centralwidget)
        self.labelCentury.setGeometry(QtCore.QRect(25, 90, 50, 15))
        self.labelCentury.setObjectName("labelCentury")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(100, 40, 130, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditCentury = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCentury.setGeometry(QtCore.QRect(100, 90, 130, 20))
        self.lineEditCentury.setObjectName("lineEditCentury")
        self.selectImage = QtWidgets.QPushButton(self.centralwidget)
        self.selectImage.setGeometry(QtCore.QRect(25, 170, 80, 30))
        self.selectImage.setObjectName("selectImage")
        self.selectInfo = QtWidgets.QPushButton(self.centralwidget)
        self.selectInfo.setGeometry(QtCore.QRect(180, 170, 80, 30))
        self.selectInfo.setObjectName("selectInfo")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(180, 230, 80, 40))
        self.add.setObjectName("add")
        AddExhibit.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddExhibit)
        QtCore.QMetaObject.connectSlotsByName(AddExhibit)

    def retranslateUi(self, AddExhibit):
        _translate = QtCore.QCoreApplication.translate
        AddExhibit.setWindowTitle(_translate("AddExhibit", "Add exhibit"))
        self.labelName.setText(_translate("AddExhibit", "Name:"))
        self.labelCentury.setText(_translate("AddExhibit", "Century:"))
        self.selectImage.setText(_translate("AddExhibit", "Select image"))
        self.selectInfo.setText(_translate("AddExhibit", "Select info"))
        self.add.setText(_translate("AddExhibit", "Add"))

