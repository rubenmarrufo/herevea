import time
from PyQt4 import QtCore, QtGui
from ParcelaService import ParcelaService
from PyQt4.QtGui import QProgressBar
from PyQt4.QtCore import *

class Ui_ProgressDialog():
    
    def __init__(self, iface, provincia,municipio,x,y,callback):
        #super(Ui_ProgressDialog, self).__init__(parent)
        self.thread = ParcelaService(provincia,municipio)
        self.thread.initCoords(x,y)
        self.iface = iface
        progressMessageBar = iface.messageBar().createMessage("Obteniendo informacion del catastro...   ")
        progress = QProgressBar()
        progress.setMaximum(0)
        progress.setMinimum(0)
        progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        progressMessageBar.layout().addWidget(progress)
        iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)
                    
        self.thread.procDone.connect(self.fin)        
        self.thread.start()
            
    def getParcelaService(self):
        pass
    
    def fin(self, result):
        a=result
        #return self.thread    
 ##self.hide()           
