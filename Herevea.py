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
# Import the code for the dialog
from HereveaDialog import HereveaDialog
from HereveaMapTool import HereveaMapTool

#from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
#from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
#from xlwt import easyxf # http://pypi.python.org/pypi/xlwt

class Herevea: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.actions = []
    self.menu = '&Herevea'
    # TODO: We are going to let the user set this up in a future iteration
    #self.toolbar = self.iface.addToolBar(u'Herevea')
    #self.toolbar.setObjectName(u'Herevea')
  def initGui(self):  
    icon_path = ":/plugins/Herevea/icon.png"
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(icon_path), \
        "Agregar capa catastro", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run)
    
    self.action2 = QAction(QIcon(icon_path), \
        "Analizar parcela", self.iface.mainWindow())    
    # connect the action to the run method
    QObject.connect(self.action2, SIGNAL("activated()"), self.selection) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Herevea", self.action)
    self.iface.addPluginToMenu("&Herevea", self.action2)
    
    self.HereveaMapTool = HereveaMapTool(self.iface.mapCanvas())
            
  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Herevea",self.action)
    self.iface.removePluginMenu("&Herevea",self.action2)
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self):    
    layers = QgsMapLayerRegistry.instance().mapLayers()
    if not any("Catastro" in name for name, layer in layers.iteritems()):
        urlWithParams='contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/png&layers=Catastro&styles=&url=http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?format%3Dimage/png%26layers%3DCatastro%26styles%3D%26CRS%3DEPSG:4326'
        rlayer = QgsRasterLayer(urlWithParams, 'Catastro', 'wms')
        QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        
  def selection(self):
    # create and show the dialog 
    dlg = HereveaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
        self.iface.mapCanvas().setMapTool(self.HereveaMapTool)

  def resolve(name, basepath=None):
    if not basepath:
      basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)       