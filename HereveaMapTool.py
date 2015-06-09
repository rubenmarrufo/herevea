from qgis.gui import QgsMapTool
from qgis.core import QgsMapLayer, QgsMapToPixel, QgsFeature, QgsFeatureRequest, QgsGeometry, QgsMapLayerRegistry
from PyQt4.QtGui import QCursor, QPixmap
from PyQt4.QtCore import Qt
from CatastroService import CatastroService

class HereveaMapTool(QgsMapTool):
    
    def __init__(self, canvas):
        
        super(QgsMapTool, self).__init__(canvas)
        self.canvas = canvas
        self.cursor = QCursor(Qt.CrossCursor)
        self.catastroService = CatastroService()
        
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
            layerPoint = self.toLayerCoordinates( layer, mouseEvent.pos() )
            self.catastroService.getInfo(layerPoint.x(), layerPoint.y())