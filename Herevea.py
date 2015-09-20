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

# Initialize Qt resources from file resources.py
import resources
import os
# Import the code for the dialog
from HereveaDialog import HereveaDialog
from HereveaMapTool import HereveaMapTool
from Ui_SeleccionFormDialog import Ui_SeleccionFormDialog
from Ui_AcercaDeDialog import Ui_AcercaDeDialog 
from CatastroService import CatastroService
from UserInputLauncherService import UserInputLauncherService 

class Herevea: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.actions = []
    self.menu = '&Herevea'
    self.seleccionForm=None
    
  def initGui(self): 
    dir = os.path.dirname(__file__)
    icon_path = os.path.join(dir,'img\Herevea.png')
    self.hereveaAction = QAction(QIcon(icon_path), \
        "Herevea", self.iface.mainWindow())    
    self.acercaDeAction = QAction(QIcon(icon_path), \
        "Acerca de...", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.hereveaAction, SIGNAL("activated()"), self.selection)
    QObject.connect(self.acercaDeAction, SIGNAL("activated()"), self.acercaDe)
    self.iface.addPluginToMenu("&Herevea", self.hereveaAction)
    self.iface.addPluginToMenu("&Herevea", self.acercaDeAction)    
            
  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Herevea",self.acercaDeAction)
    self.iface.removePluginMenu("&Herevea",self.hereveaAction)
    #self.iface.removeToolBarIcon(self.action)
        
  def selection(self):       
    # create and show the dialog 
    dlg = HereveaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
        if self.seleccionForm == None:
            self.seleccionForm = Ui_SeleccionFormDialog(CatastroService())
        self.seleccionForm.show()
        result = self.seleccionForm.exec_()
        if result == 1:
            if self.seleccionForm.parcelaService == None:
                self.HereveaMapTool = HereveaMapTool(self.iface,self.seleccionForm.provincia(),self.seleccionForm.municipio())
                layers = QgsMapLayerRegistry.instance().mapLayers()
                self.iface.mapCanvas().setMapTool(self.HereveaMapTool)
                if not any("Catastro" in name for name, layer in layers.iteritems()):
                    urlWithParams='contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/png&layers=Catastro&styles=&url=http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?format%3Dimage/png%26layers%3DCatastro%26styles%3D%26CRS%3DEPSG:4326'
                    rlayer = QgsRasterLayer(urlWithParams, 'Catastro', 'wms')
                    QgsMapLayerRegistry.instance().addMapLayer(rlayer)
            else:  
                self.launcher=UserInputLauncherService(self.iface, self.seleccionForm.parcelaService, self.fin)
                self.launcher.launch()
                
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