# coding=utf-8
from qgis.gui import *
from qgis.core import *
from PyQt4.QtGui import QCursor, QPixmap, QProgressBar
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from Ui_ProgressDialog import Ui_ProgressDialog
from ParcelaService import ParcelaService
from UserInputLauncherService import UserInputLauncherService 
from multiprocessing.pool import ThreadPool
import json
import os
import subprocess

class HereveaMapTool(QgsMapToolEmitPoint):
    
    def __init__(self, iface, provincia, municipio):        
        super(QgsMapToolEmitPoint, self).__init__(iface.mapCanvas())
        self.iface = iface
        self.provincia = provincia
        self.municipio = municipio
        self.canvas = iface.mapCanvas()
        self.cursor = QCursor(Qt.CrossCursor)   
        self.showMessage()    
        
    def activate(self):
        self.canvas.setCursor(self.cursor)
        
    def showMessage(self):
        self.iface.messageBar().pushMessage("Seleccion", "Haz clic sobre la parcela a analizar", level=QgsMessageBar.INFO, duration=3)      
    
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

    def canvasPressEvent(self, mouseEvent):        
        layers = QgsMapLayerRegistry.instance().mapLayers()        
        for name, layer in layers.iteritems():
            if name.startswith('Catastro'):
                layerPoint = self.toLayerCoordinates( layer, mouseEvent.pos() )
                self.parcelaService = ParcelaService(self,self.provincia,self.municipio) 
                self.parcelaService.initCoords(layerPoint.x(),layerPoint.y())
                self.launcher = UserInputLauncherService(self.iface,self.parcelaService,self.fin)
                self.launcher.launch() 
                
    def fin(self, result):        
        self.launcher.fin(result) 
                      
