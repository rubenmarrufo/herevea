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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "Herevea plugin" 
def description():
  return "Herramienta del proyecto Herevea"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load Herevea class from file Herevea
  from Herevea import Herevea 
  return Herevea(iface)
