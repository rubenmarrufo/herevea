# coding=utf-8
from ParcelaService import ParcelaService
from HuellaService import HuellaService
from Ui_ProgressDialog import Ui_ProgressDialog
from Ui_ProyectoFormDialog import Ui_ProyectoFormDialog
from Ui_UsuarioFormDialog import Ui_UsuarioFormDialog
from Ui_ActuacionFormDialog import Ui_ActuacionFormDialog
from Ui_ErrorDialog import Ui_ErrorDialog
from Ui_ResultFormDialog import Ui_ResultFormDialog
from ParcelaService import ParcelaService
from PyQt4.QtGui import QCursor, QPixmap, QProgressBar
from PyQt4 import QtGui, QtCore
from qgis.gui import *
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class UserInputLauncherService():        
    def __init__(self, iface, parcelaService, callback):               
        self.iface = iface
        self.parcelaService = parcelaService
        self.callback = callback
   
    def launch(self):
        progressMessageBar = self.iface.messageBar().createMessage("Obteniendo informacion del catastro...   ")
        progress = QProgressBar()
        progress.setMaximum(0)
        progress.setMinimum(0)
        progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        progressMessageBar.layout().addWidget(progress)
        self.iface.messageBar().pushWidget(progressMessageBar, self.iface.messageBar().INFO)        
        self.parcelaService.procDone.connect(self.callback)
        self.parcelaService.start()
        
    def fin(self, result):           
        self.iface.messageBar().clearWidgets()
        if not result:
            self.iface.messageBar().pushMessage("Error", "No se obtuvo ningun resultado del catastro en el municipio seleccionado para esas coordenadas", level=QgsMessageBar.CRITICAL, duration=3)    
        else:            
            print self.parcelaService.uso() 
            if self.parcelaService.uso() != 'Residencial':
                self.iface.messageBar().pushMessage("Error", "HEREVEA solo analiza edificios de uso residencial", level=QgsMessageBar.CRITICAL, duration=3)                
            else:
                self.ui_Usuario=Ui_UsuarioFormDialog(self.parcelaService)
                self.ui_Proyecto=Ui_ProyectoFormDialog(self.parcelaService)
                self.ui_Actuacion=Ui_ActuacionFormDialog(self.parcelaService)                                                        
                self.showProyectoForm()
                                                        
    def showUsuarioForm(self):        
        self.ui_Usuario.show()
        result = self.ui_Usuario.exec_()
        if result == 1:
            self.showActuacionForm()
        elif self.ui_Usuario.back == True:
            self.showProyectoForm()           
    
    def showProyectoForm(self):        
        self.ui_Proyecto.show()
        result = self.ui_Proyecto.exec_()
        if result == 1:
            self.showUsuarioForm()
            
    def showActuacionForm(self):
        self.ui_Actuacion.setDatosUsuario(self.ui_Usuario.getValues())        
        self.ui_Actuacion.show()
        result = self.ui_Actuacion.exec_()
        if result == 1:
            self.showResults()
        elif self.ui_Actuacion.back == True:
            self.showUsuarioForm()
            
    def showResults(self):
        proyValues=self.ui_Proyecto.getValues()
        userValues=self.ui_Usuario.getValues()
        actValues = self.ui_Actuacion.getValues()
        huellaService = HuellaService()
        huellaResult = huellaService.Calculate(proyValues,userValues,actValues)
        ui_Result=Ui_ResultFormDialog(self.parcelaService,huellaResult)
        ui_Result.show()
        ui_Result.exec_()                         
        