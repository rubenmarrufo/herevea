from qgis.gui import QgsMapTool
from qgis.core import QgsMapLayer, QgsMapToPixel, QgsFeature, QgsFeatureRequest, QgsGeometry, QgsMapLayerRegistry
from PyQt4.QtGui import QCursor, QPixmap
from PyQt4.QtCore import Qt
from PyQt4 import QtGui, QtCore
from ParcelaService import ParcelaService
from HuellaService import HuellaService
from Ui_ProgressDialog import Ui_ProgressDialog
from Ui_ProyectoFormDialog import Ui_ProyectoFormDialog
from Ui_UsuarioFormDialog import Ui_UsuarioFormDialog
from Ui_ActuacionFormDialog import Ui_ActuacionFormDialog
from Ui_ResultFormDialog import Ui_ResultFormDialog
from multiprocessing.pool import ThreadPool
import json
import os
import subprocess

class HereveaMapTool(QgsMapTool):
    
    def __init__(self, canvas):
        
        super(QgsMapTool, self).__init__(canvas)
        self.canvas = canvas
        self.cursor = QCursor(Qt.CrossCursor)        
        
    def activate(self):
        self.canvas.setCursor(self.cursor)
    
    def screenToLayerCoords(self, screenPos, layer):
        
        transform = self.canvas.getCoordinateTransform()
        canvasPoint = QgsMapToPixel.toMapCoordinates(   transform, 
                                                        screenPos.x(), 
                                                        screenPos.y() )
        
        # Transform if required
        layerEPSG = layer.crs().authid()
        projectEPSG = self.canvas.mapRenderer().destinationCrs().authid()
        if layerEPSG != projectEPSG:
            renderer = self.canvas.mapRenderer()
            layerPoint = renderer.mapToLayerCoordinates(    layer, 
                                                            canvasPoint )
        else:
            layerPoint = canvasPoint
        
        # Convert this point (QgsPoint) to a QgsGeometry
        return QgsGeometry.fromPoint(layerPoint)


    def canvasReleaseEvent(self, mouseEvent):
        layers = QgsMapLayerRegistry.instance().mapLayers()        
        for name, layer in layers.iteritems():
            if name.startswith('Catastro'):
                layerPoint = self.toLayerCoordinates( layer, mouseEvent.pos() )
                ui_Progress=Ui_ProgressDialog(layerPoint.x(),layerPoint.y())
                ui_Progress.show()
                ui_Progress.exec_()
                self.parcelaService = ui_Progress.getParcelaService()
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
        self.ui_Actuacion.show()
        result = self.ui_Actuacion.exec_()
        if result == 1:
            self.showResults()
        elif self.ui_Actuacion.back == True:
            self.showUsuarioForm()
            
    def showResults(self):
        values = self.ui_Actuacion.getValues()
        huellaService = HuellaService()
        huellaResult = huellaService.Calculate(values)
        ui_Result=Ui_ResultFormDialog(self.parcelaService,huellaResult)
        ui_Result.show()
        ui_Result.exec_()                         