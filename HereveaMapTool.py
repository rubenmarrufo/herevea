from qgis.gui import QgsMapTool
from qgis.core import QgsMapLayer, QgsMapToPixel, QgsFeature, QgsFeatureRequest, QgsGeometry, QgsMapLayerRegistry
from PyQt4.QtGui import QCursor, QPixmap
from PyQt4.QtCore import Qt
from PyQt4 import QtGui, QtCore
from ParcelaService import ParcelaService
from Ui_ProyectoFormDialog import Ui_ProyectoFormDialog
from Ui_UsuarioFormDialog import Ui_UsuarioFormDialog
from Ui_ActuacionFormDialog import Ui_ActuacionFormDialog
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
                self.parcelaService = ParcelaService(layerPoint.x(),layerPoint.y())                
                #inmueblesList = self.catastroService.getInmueblesList(numcatastro)
                #ui_InmueblesList=Ui_InmueblesListDialog(inmueblesList, numcatastro)
                #ui_Proyecto.show()
                #result = ui_Proyecto.exec_()
                ui_Proyecto=Ui_ProyectoFormDialog(self.parcelaService)
                ui_Proyecto.show()
                result = ui_Proyecto.exec_()
                if result == 1:
                    ui_Usuario=Ui_UsuarioFormDialog(self.parcelaService)
                    ui_Usuario.show()
                    result = ui_Usuario.exec_()  
                    if result == 1:
                        ui_Actuacion=Ui_ActuacionFormDialog(self.parcelaService)
                        ui_Actuacion.show()
                        result = ui_Actuacion.exec_() 
                        if result == 1: 
                            values = ui_Actuacion.getValues()
                            dir = os.path.dirname(__file__)
                            filename = os.path.join(dir,'toexcel/data.txt')
                            with open(filename, 'w+') as outfile:
                                json.dump(values, outfile)
                            application = os.path.join(dir,'toexcel/Herevea.exe')
                            cmd = [application]
                            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
                            process.wait()
                            for line in process.stdout:
                                print(line)