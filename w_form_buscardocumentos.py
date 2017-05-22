import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem
from PyQt5 import uic
from form_buscardocumentos import Ui_form_buscadordocumentos
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5 import QtCore, QtNetwork

from mayan_api_client import API
import json


api = API(host='http://10.0.0.102:80', username='admin', password='slam2016')

class buscardocumentos(QDialog):

    # en este formulario vamos a buscar todos los documentos existentes de un usuario

    obj_form= Ui_form_buscadordocumentos()
    id_descarga = ""

    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_buscadordocumentos()
        self.obj_form.setupUi(self)
        self.obj_form.boton_buscar.clicked.connect(self.get_list_doc)
        self.obj_form.tw_document.cellClicked.connect(self.seleccion_item_tabla)
        self.obj_form.boton_descargar.clicked.connect(self.descargar)

    def get_list_doc(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        list_doc = api.documents.documents.get()
        count1 = 0
        for key in range(0,int(list_doc['count'])):
            obj_json = list_doc['results'][count1]
            #obj = json.loads(obj_json)
            #asd = repr(obj)

            rowPosition = self.obj_form.tw_document.rowCount()
            self.obj_form.tw_document.insertRow(rowPosition)

            self.obj_form.tw_document.setItem(rowPosition , 0, QTableWidgetItem(str(list_doc['results'][count1]['id'])))
            self.obj_form.tw_document.setItem(rowPosition , 1, QTableWidgetItem(str(list_doc['results'][count1]['label'])))
            self.obj_form.tw_document.setItem(rowPosition , 2, QTableWidgetItem(str(list_doc['results'][count1]['date_added'])))

            count1 = count1 + 1

    def seleccion_item_tabla(self, clickedIndex):
        nom_archivo = self.obj_form.tw_document.item(clickedIndex,1)
        self.id_descarga= self.obj_form.tw_document.item(clickedIndex,0)
        self.obj_form.lne_nom_arch.setText(nom_archivo.text())


    def descargar(self):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        # Obtener datos del documento
        #print 'Obteniendo datos del document #:', document_id
        document = api.documents.documents(13).get()
        #print 'Nombre de archivo del documento:', document['label']
        #print 'Descargando...'
        # Crear un archivo para escritura come el mismo nombre del documento a descargar
        with open(document['label'], 'wb') as file_object:
            #file_object.write(api.documents.documents(4).download.get())
            id= self.id_descarga.text()
            file_object.write(api.documents.documents(13).download.get())

        file_object.close()
        wei=0
