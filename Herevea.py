# coding=utf-8
"""
/***************************************************************************
Name			 	 : Herevea plugin
Description          : Herramienta del proyecto Herevea
Date                 : 22/May/15 
copyright            : (C) 2015 by Ruben Jimenez Marrufo
email                : ruben_marrufo@hotmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources
import os
import requests
# Import the code for the dialog
from HereveaDialog import HereveaDialog
from HereveaMapTool import HereveaMapTool
from Ui_SeleccionFormDialog import Ui_SeleccionFormDialog
from Ui_AcercaDeDialog import Ui_AcercaDeDialog 
from CatastroService import CatastroService
from UserInputLauncherService import UserInputLauncherService 
from Ui_ResultFormDialog import Ui_ResultFormDialog

class Herevea: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.actions = []
    self.menu = '&Herevea'
    self.seleccionForm=None
    self.selectionToolAdded=False
    
  def initGui(self): 
    dir = os.path.dirname(__file__)
    icon_path = os.path.join(dir,'img\Her.png')
    self.hereveaAction = QAction(QIcon(icon_path), \
        "Herevea", self.iface.mainWindow())    
    self.acercaDeAction = QAction(QIcon(''), \
        "Acerca de...", self.iface.mainWindow())
    icon_path_sel = os.path.join(dir,'img\HerSelect.png')
    self.seleccionAction = QAction(QIcon(icon_path_sel), \
        "Seleccionar parcela", self.iface.mainWindow())
    self.seleccionAction.setCheckable(True)
    # connect the action to the run method
    QObject.connect(self.hereveaAction, SIGNAL("activated()"), self.selection)
    QObject.connect(self.acercaDeAction, SIGNAL("activated()"), self.acercaDe)
    QObject.connect(self.seleccionAction, SIGNAL("activated()"), self.setMapTool)
    self.iface.addPluginToMenu("&Herevea", self.hereveaAction)
    self.iface.addPluginToMenu("&Herevea", self.acercaDeAction)  
    self.iface.addToolBarIcon(self.hereveaAction)

            
  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Herevea",self.acercaDeAction)
    self.iface.removePluginMenu("&Herevea",self.hereveaAction)
    self.iface.removeToolBarIcon(self.seleccionAction)
    self.iface.removeToolBarIcon(self.hereveaAction)    
        
  def selection(self):
    #uiResult = Ui_ResultFormDialog()  
    #uiResult.show()
    #uiResult.exec_()      
    # create and show the dialog 
    dlg = HereveaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1:
        try:
            self.addCatastroMap() 
            if self.seleccionForm == None:
                self.seleccionForm = Ui_SeleccionFormDialog(CatastroService())
            self.seleccionForm.show()
            result = self.seleccionForm.exec_()
            if result == 1:
                self.centrarMapa()
                self.addMapToolIcon()             
                if self.seleccionForm.parcelaService == None:                                
                    if hasattr(self, 'HereveaMapTool'):
                        self.HereveaMapTool.provincia=self.seleccionForm.provincia()
                        self.HereveaMapTool.municipio=self.seleccionForm.municipio()
                else:   
                    self.launcher=UserInputLauncherService(self.iface, self.seleccionForm.parcelaService, self.fin)
                    self.launcher.launch()
        except requests.ConnectionError as e:
            self.iface.messageBar().pushMessage("Error", unicode("Herevea no pudo conectar con el catastro. Compruebe su conexión a internet y vuelva a intentarlo", "utf-8"), level=QgsMessageBar.CRITICAL, duration=3)

  def setMapTool(self):
    self.HereveaMapTool = HereveaMapTool(self.iface,self.seleccionForm.provincia(),self.seleccionForm.municipio())                
    self.iface.mapCanvas().setMapTool(self.HereveaMapTool)
    
  def addMapToolIcon(self):
    self.iface.messageBar().pushMessage("Herevea", unicode("Localice la parcela y use la herramienta de selección para iniciar el análisis", "utf-8"), level=QgsMessageBar.INFO, duration=3)
    if not self.selectionToolAdded:
        group = QActionGroup( self.iface.mainWindow() )
        group.setExclusive(True)
        for action in self.iface.mapNavToolToolBar().actions():
            group.addAction(action)
        group.addAction(self.seleccionAction)                               
        self.iface.addToolBarIcon(self.seleccionAction)
        self.selectionToolAdded=True
    

  def addCatastroMap(self):    
    layers = QgsMapLayerRegistry.instance().mapLayers()
    if not any("Catastro" in name for name, layer in layers.iteritems()):
        urlWithParams='contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/png&layers=Catastro&styles=&url=http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?format%3Dimage/png%26layers%3DCatastro%26styles%3D%26CRS%3DEPSG:4326'
        rlayer = QgsRasterLayer(urlWithParams, 'Catastro', 'wms')
        QgsMapLayerRegistry.instance().addMapLayer(rlayer)    
        
  def centrarMapa(self):
    coord=self.seleccionForm.coordenadas()    
    zoom = self.seleccionForm.zoom()
    self.iface.actionZoomToSelected().trigger()
    self.iface.mapCanvas().zoomScale(zoom)
    self.iface.mapCanvas().setCenter(coord)    
    
  def fin(self, result):
    self.launcher.fin(result)       
  
  def acercaDe(self):
    dlg = Ui_AcercaDeDialog()
    dlg.show()
    result = dlg.exec_()

  def resolve(name, basepath=None):
    if not basepath:
      basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)       