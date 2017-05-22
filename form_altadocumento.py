# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_altadocumento.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_altadocumento(object):
    def setupUi(self, form_altadocumento):
        form_altadocumento.setObjectName("form_altadocumento")
        form_altadocumento.resize(758, 482)
        form_altadocumento.setStyleSheet("background-color: rgb(82, 175, 50);\n"
"font: 75 12pt \"Courier 10 Pitch\";")
        self.gridLayout_5 = QtWidgets.QGridLayout(form_altadocumento)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(form_altadocumento)
        self.frame.setStyleSheet("background-color: rgb(29, 67, 111);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 100, 19))
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lbl_id = QtWidgets.QLabel(self.tab)
        self.lbl_id.setGeometry(QtCore.QRect(150, 140, 61, 17))
        self.lbl_id.setObjectName("lbl_id")
        self.boton_buscar = QtWidgets.QPushButton(self.tab)
        self.boton_buscar.setGeometry(QtCore.QRect(630, 40, 80, 27))
        self.boton_buscar.setStyleSheet("background-color: rgb(82, 175, 50);")
        self.boton_buscar.setObjectName("boton_buscar")
        self.lbl_buscar = QtWidgets.QLabel(self.tab)
        self.lbl_buscar.setGeometry(QtCore.QRect(100, 40, 511, 20))
        self.lbl_buscar.setObjectName("lbl_buscar")
        self.boton_guardar = QtWidgets.QPushButton(self.tab)
        self.boton_guardar.setGeometry(QtCore.QRect(270, 140, 80, 27))
        self.boton_guardar.setStyleSheet("background-color: rgb(82, 175, 50);")
        self.boton_guardar.setObjectName("boton_guardar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 11, 154, 25))
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 87, 25))
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3.raise_()
        self.boton_buscar.raise_()
        self.lbl_id.raise_()
        self.lbl_buscar.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(form_altadocumento)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_altadocumento)

    def retranslateUi(self, form_altadocumento):
        _translate = QtCore.QCoreApplication.translate
        form_altadocumento.setWindowTitle(_translate("form_altadocumento", "Formulario alta de archivo"))
        self.label_3.setText(_translate("form_altadocumento", "ID:"))
        self.lbl_id.setText(_translate("form_altadocumento", "asd"))
        self.boton_buscar.setText(_translate("form_altadocumento", "buscar"))
        self.lbl_buscar.setText(_translate("form_altadocumento", "asd"))
        self.boton_guardar.setText(_translate("form_altadocumento", "Guardar"))
        self.label.setText(_translate("form_altadocumento", "Usuario :  Admin"))
        self.label_2.setText(_translate("form_altadocumento", "archivo: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_altadocumento", "Guardar archivo"))

