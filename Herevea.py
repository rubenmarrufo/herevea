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
from CatastroService import CatastroService

class Herevea: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.actions = []
    self.menu = '&Herevea'
    # TODO: We are going to let the user set this up in a future iteration
    self.toolbar = self.iface.addToolBar(u'Herevea')
    self.toolbar.setObjectName(u'Herevea')
  def initGui(self):  
    icon_path = ":/plugins/Herevea/icon.png"
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(icon_path), \
        "Herevea", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Herevea", self.action)
    
    self.HereveaMapTool = HereveaMapTool(self.iface.mapCanvas())
        
    action = self.add_action(
                icon_path,
                text='Seleccione una parcela del catastro.',
                callback=self.run,
                parent=self.iface.mainWindow())
    
    action.setCheckable(True)
    self.HereveaMapTool.setAction(action)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Herevea",self.action)
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self):        
    # create and show the dialog 
    dlg = HereveaDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
        # do something useful (delete the line containing pass and
        # substitute with your code      
        urlWithParams='contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/png&layers=Catastro&styles=&url=http://ovc.catastro.meh.es/Cartografia/WMS/ServidorWMS.aspx?format%3Dimage/png%26layers%3DCatastro%26styles%3D%26CRS%3DEPSG:4326'
        rlayer = QgsRasterLayer(urlWithParams, 'Catastro', 'wms')
        QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        self.iface.mapCanvas().setMapTool(self.HereveaMapTool)
        
  def add_action(
    self,
    icon_path,
    text,
    callback,
    enabled_flag=True,
    add_to_menu=True,
    add_to_toolbar=True,
    status_tip=None,
    whats_this=None,
    parent=None):
    """Add a toolbar icon to the InaSAFE toolbar.

    :param icon_path: Path to the icon for this action. Can be a resource
        path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
    :type icon_path: str

    :param text: Text that should be shown in menu items for this action.
    :type text: str

    :param callback: Function to be called when the action is triggered.
    :type callback: function

    :param enabled_flag: A flag indicating if the action should be enabled
        by default. Defaults to True.
    :type enabled_flag: bool

    :param add_to_menu: Flag indicating whether the action should also
        be added to the menu. Defaults to True.
    :type add_to_menu: bool

    :param add_to_toolbar: Flag indicating whether the action should also
        be added to the toolbar. Defaults to True.
    :type add_to_toolbar: bool

    :param status_tip: Optional text to show in a popup when mouse pointer
        hovers over the action.
    :type status_tip: str

    :param parent: Parent widget for the new action. Defaults None.
    :type parent: QWidget

    :param whats_this: Optional text to show in the status bar when the
        mouse pointer hovers over the action.

    :returns: The action that was created. Note that the action is also
        added to self.actions list.
    :rtype: QAction
    """

    icon = QIcon(icon_path)
    action = QAction(icon, text, parent)
    action.triggered.connect(callback)
    action.setEnabled(enabled_flag)

    if status_tip is not None:
        action.setStatusTip(status_tip)

    if whats_this is not None:
        action.setWhatsThis(whats_this)

    if add_to_toolbar:
        self.toolbar.addAction(action)

    if add_to_menu:
        self.iface.addPluginToMenu(
            self.menu,
            action)

    self.actions.append(action)

    return action        