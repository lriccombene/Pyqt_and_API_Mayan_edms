import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QTableWidgetItem,QFileDialog
from PyQt5 import uic
from form_altadocumento import Ui_form_altadocumento
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5 import QtCore, QtNetwork
import defer
#from E_altadocumento import  E_alta_documento

from mayan_api_client import API
import json


class DocumentTypeSerializer (object):
    delete_time_period = 0
    delete_time_unit = ""
    documents_url = ""
    documents_count = ""
    id = 0
    label = ""
    #filenames = DocumentTypeFilenameSerializer()
    trash_time_period = 0
    trash_time_unit = ""
    url= ""

class DocumentSerializer (object):
    date_added =""
    description =""
    document_type = DocumentTypeSerializer()
    id =0
    label =""
    language =""
    #latest_version =""DocumentVersionSerializer()
    latest_version =""
    url =""
    uuid =""
    versions_url=""



class DocumentTypeFilenameSerializer (object):
    filename = ''

class DocumentVersionSerializer (object) :
    checksum =''
    comment =''
    document_url =''
    download_url =''
    encoding =''
    file =''
    mimetype =''
    pages_url =''
    size =''
    timestamp =''
    url =''


api = API(host='http://10.0.0.102:80', username='admin', password='slam2016')

class alta_documento(QDialog):
    obj_form= Ui_form_altadocumento()
    id_empresa=""
    email=""
    id_party=""
    def __init__(self):
        QDialog.__init__(self)
        self.obj_form = Ui_form_altadocumento()
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar.clicked.connect(self.guardar)
        #self.obj_form.boton_actualizar.clicked.connect(self.actualizar)
        #self.obj_form.boton_buscar.clicked.connect(self.get_list_doc)
        self.obj_form.boton_buscar.clicked.connect(self.buscar_file)


    def buscar_file(self):
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"")
        wer = str(fname[0])
        self.obj_form.lbl_buscar.setText(wer)


    def descargar(self):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        #url ="http://10.0.0.102:80/api/documents/documents/1/download/"
        #file_path= "/home/user/Documentos/ALTEC/sgd20170513"
        #obj_descarga =_Downloader(url)
        #respose = api.documents.documents(4).download.get()
        #response = api.documents.documents(2).versions.get()
        #with open('/home/user/Documentos/ALTEC/sgd20170513/tmp/medata.pdf', 'wb') as f:
        #    f.write(response)
        #


        # Obtener datos del documento
        #print 'Obteniendo datos del document #:', document_id
        document = api.documents.documents(4).get()

        #print 'Nombre de archivo del documento:', document['label']
        #print 'Descargando...'

        # Crear un archivo para escritura come el mismo nombre del documento a descargar
        with open(document['label'], 'wb') as file_object:
            #file_object.write(api.documents.documents(4).download.get())
            file_object.write(str(api.documents.documents(4).download.get()))

        we=1






    def guardar(self):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        response=""
        import codecs
        with codecs.open(, "r",encoding='utf-8', errors='ignore') as file_object:
        #with codecs.open('/home/user/Documentos/ALTEC/sgd20170513/tmp/prueba.pdf', "r",encoding='utf-8', errors='ignore') as file_object:
            response = api.documents.documents.post({'document_type': 2}, files={'file': file_object})

        self.obj_form.lbl_id.setText(str(response['id']))



    def get_list_doc(self):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        list_doc = api.documents.documents.get()
        #asd =list_doc.results[1].id
        #jData = json.dumps(list_doc.content)


        #print("The response contains {0} properties".format(len(jData)))
        #print("\n")
        #for key in jData:
        count1 = 0
        for key in range(0,int(list_doc['count'])):
            obj_json = list_doc['results'][count1]
            #obj = json.loads(obj_json)
            #asd = repr(obj)

            rowPosition = self.obj_form.tw_document.rowCount()
            self.obj_form.tw_document.insertRow(rowPosition)

            self.obj_form.tw_document.setItem(rowPosition , 0, QTableWidgetItem(str(list_doc['results'][count1]['id'])))
            self.obj_form.tw_document.setItem(rowPosition , 1, QTableWidgetItem(str(list_doc['results'][count1]['label'])))
            count1 = count1 + 1

        #for item in list_doc:
        #    doc= item
        #for item in list_doc:
        #    if item =='results':
        #        for item2 in item:
        #            rowPosition = self.obj_form.tw_document.rowCount()
        #            self.obj_form.tw_document.insertRow(rowPosition)
        #
        #            if(item =='id'):
        #                self.obj_form.tw_document.setItem(rowPosition , 0, QTableWidgetItem(str(item[id])))
        #
        #           if(item =='label'):
        #                self.obj_form.tw_document.setItem(rowPosition , 1, QTableWidgetItem(str("a")))





class _Downloader(object):
    """An asynch downloader that fires a deferred with data when done."""

    def __init__(self, url, file_path=None):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        if file_path is None:
            self.file_handler = None
            self.file_downloaded_size = None
        else:
            self.file_handler = open(file_path, "wb")
            self.file_downloaded_size = 0

        self._qt_network_manager = QtNetwork.QNetworkAccessManager()

        self.deferred = defer.Deferred()
        self.deferred._store_it_because_qt_needs_or_wont_work = self
        request = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

        self.req = self._qt_network_manager.get(request)
        self.req.error.connect(self.error)
        self.req.finished.connect(self.end)
        if self.file_handler is not None:
            self.req.downloadProgress.connect(self._save_partial)

    def _save_partial(self, dloaded, total):
        """Save partially downloaded content."""
        new_data = self.req.readAll()
        self.file_downloaded_size += len(new_data)
        self.file_handler.write(new_data)

    def error(self, error_code):
        """Request finished (*maybe*) on error."""
        error_message = "Downloader error {}: {}".format(error_code, self.req.errorString())
        #logger.warning(error_message)
        #if not self.deferred.called:
        #    self.deferred.errback(NetworkError(error_message))

    def end(self):
        """Send data through the deferred, if wasn't fired before."""
        if self.file_handler is None:
            result = self.req.read(self.req.bytesAvailable())
        else:
            result = self.file_downloaded_size
            self.file_handler.close()

        if result and not self.deferred.called:
            self.deferred.callback(result)
