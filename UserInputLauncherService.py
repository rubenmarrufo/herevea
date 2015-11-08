# coding=utf-8
from ParcelaService import ParcelaService
from HuellaService import HuellaService
from Ui_ProgressDialog import Ui_ProgressDialog
from Ui_ProyectoFormDialog import Ui_ProyectoFormDialog
from Ui_UsuarioFormDialog import Ui_UsuarioFormDialog
from Ui_ActuacionFormDialog import Ui_ActuacionFormDialog
from Ui_ErrorDialog import Ui_ErrorDialog
from Ui_IntroFormDialog import Ui_IntroFormDialog
from Ui_ResultFormDialog import Ui_ResultFormDialog
from Ui_DemolicionConstruccionDialog import Ui_DemolicionConstruccionDialog
from ParcelaService import ParcelaService
from PyQt4.QtGui import QCursor, QPixmap, QProgressBar
from PyQt4 import QtGui, QtCore
from qgis.gui import *
from qgis.core import *
from qgis.utils import *
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
            if self.parcelaService.uso() == '':
                self.iface.messageBar().pushMessage("Error", "No se obtuvo ningun resultado del catastro en el municipio seleccionado para esas coordenadas", level=QgsMessageBar.CRITICAL, duration=3)
            elif self.parcelaService.uso() != 'Residencial':
                self.iface.messageBar().pushMessage("Error", "HEREVEA solo analiza edificios de uso residencial", level=QgsMessageBar.CRITICAL, duration=3)                
            else:
                self.addParcelaPoint(self.parcelaService.numCatastro, self.parcelaService.x, self.parcelaService.y)
                self.ui_Usuario=Ui_UsuarioFormDialog(self.parcelaService)
                self.ui_Proyecto=Ui_ProyectoFormDialog(self.parcelaService)
                self.ui_Actuacion=Ui_ActuacionFormDialog(self.parcelaService)   
                self.ui_Intro=Ui_IntroFormDialog(self.parcelaService)
                self.ui_DemolicionConstruccion=Ui_DemolicionConstruccionDialog(self.parcelaService)
                self.showProyectoForm()
                
    def addParcelaPoint(self, numCatastro,x,y):
        settings = QSettings()
        # Take the "CRS for new layers" config, overwrite it while loading layers and...
        oldProjValue = settings.value( "/Projections/defaultBehaviour", "prompt", type=str )
        settings.setValue( "/Projections/defaultBehaviour", "useProject" )        
        layers = QgsMapLayerRegistry.instance().mapLayers()
        for lyr in QgsMapLayerRegistry.instance().mapLayers().values():
            print lyr.name()
            if lyr.name().startswith("Herevea: Parcela"):                
                QgsMapLayerRegistry.instance().removeMapLayer(lyr.id())        
        layer = QgsVectorLayer('Point?crs=EPSG:4326', 'Herevea: Parcela ' + numCatastro, "memory")  
             
        pr = layer.dataProvider() 
        pt = QgsFeature()
        point1 = QgsPoint(x,y)
        pt.setGeometry(QgsGeometry.fromPoint(point1))
        pr.addFeatures([pt])
        QgsMapLayerRegistry.instance().addMapLayers([layer])
        settings.setValue( "/Projections/defaultBehaviour", oldProjValue )
    
    def showProyectoForm(self):        
        self.ui_Proyecto.show()
        result = self.ui_Proyecto.exec_()
        if result == 1:
            self.showUsuarioForm()
                                                                    
    def showUsuarioForm(self):        
        self.ui_Usuario.show()
        result = self.ui_Usuario.exec_()
        if result == 1:
            self.ui_Intro.toRehab()
            self.showIntroForm()
        elif self.ui_Usuario.back == True:
            self.ui_Usuario.back=False
            self.showProyectoForm()
            
    def showIntroForm(self):
        self.ui_Intro.show()
        result = self.ui_Intro.exec_()
        if result == 1:
            if self.ui_Intro.rehab==True:
                self.showActuacionForm()
            elif self.ui_Intro.demCons==True:
                self.showDemCons()
        elif self.ui_Intro.back == True:            
            self.ui_Intro.back=False
            if self.ui_Intro.rehab==True:
                self.showUsuarioForm()
            elif self.ui_Intro.demCons==True:
                self.ui_Intro.rehab=True
                self.ui_Intro.demCons=False
                self.showActuacionForm()                
            
    def showActuacionForm(self):
        self.ui_Actuacion.setDatosCatastro(self.ui_Proyecto.getValues())
        self.ui_Actuacion.setDatosUsuario(self.ui_Usuario.getValues())        
        self.ui_Actuacion.show()
        result = self.ui_Actuacion.exec_()
        if result == 1:
            self.ui_Intro.toDemCons()
            self.showIntroForm()
        elif self.ui_Actuacion.back == True:
            self.ui_Actuacion.back = False
            self.ui_Intro.toRehab()
            self.showIntroForm()
    
    def showDemCons(self):
        self.ui_DemolicionConstruccion.show()
        self.ui_DemolicionConstruccion.setup(self.ui_Proyecto.getValues(),self.ui_Usuario.getValues())
        result = self.ui_DemolicionConstruccion.exec_()
        if result == 1:
            self.showResults()
        elif self.ui_DemolicionConstruccion.back==True:
            self.ui_DemolicionConstruccion.back=False            
            self.showIntroForm()
        
    def showResults(self):
        proyValues=self.ui_Proyecto.getValues()
        userValues=self.ui_Usuario.getValues()
        actValues = self.ui_Actuacion.getValues()
        demConsValues = self.ui_DemolicionConstruccion.getValues()
        huellaService = HuellaService()
        huellaResult = huellaService.Calculate(proyValues,userValues,actValues, demConsValues)
        if huellaResult is None:
            return           
        elif 'error' in huellaResult:
            ui_Error = Ui_ErrorDialog(u'Hubo un error intentando realizar el análisis: ' + unicode(huellaResult["error"]))
            ui_Error.show()
            ui_Error.exec_()
        else:
            self.ui_Result=Ui_ResultFormDialog(self.parcelaService,huellaResult)
            self.ui_Result.show()
            result = self.ui_Result.exec_()
            if self.ui_Result.back==True:
                self.ui_Result.back=False            
                self.showDemCons()                         
        