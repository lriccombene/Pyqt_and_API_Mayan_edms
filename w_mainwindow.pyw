import sys,datetime
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox, QTableWidgetItem,QMainWindow
from mainwindow import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QFileDialog
from w_form_altadocumento import alta_documento
from w_form_buscardocumentos import buscardocumentos

class Mainwindow(QMainWindow):
    singleton =""
    singleton_idusu=""
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        self.obj_form_main = Ui_MainWindow()
        self.obj_form_main.setupUi(self)
        self.obj_form_main.actionAlta_de_Documentos.triggered.connect(self.altadoc)
        self.obj_form_main.actionBuscar_Documentos.triggered.connect(self.buscardocumentos)

    def altadoc(self):
        self.form_altadocumentos = alta_documento()
        self.form_altadocumentos.show()


    def buscardocumentos(self):
        self.form_buscardocumentos = buscardocumentos()
        self.form_buscardocumentos.show()


app = QApplication(sys.argv)
dialogo= Mainwindow()
dialogo.show()

app.exec_()
