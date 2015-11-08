# coding=utf-8
import xmltodict
import operator
from PyQt4 import QtCore
from CatastroService import CatastroService
from InmueblesService import InmueblesService
from PyQt4.QtCore import *
from qgis.core import *

class ParcelaService(QThread):
    procDone = QtCore.pyqtSignal(bool)  
    def __init__(self, parentThread, provincia, municipio):
        QThread.__init__(self, parentThread )
        self.catastroService = CatastroService()
        self.provincia=provincia
        self.municipio=municipio  
        self.numCatastro=None     
        self.x=None
        self.y=None
                  
    def initCoords(self, x, y):
        self.x=x
        self.y=y
        
    def initRefCatastral(self, refCatastro):
        try:
            self.numCatastro=refCatastro        
            xyInfo = self.catastroService.getParcelaCoords(self.numCatastro,self.provincia,self.municipio)
            self.x = float(xyInfo['xcen'])
            self.y = float(xyInfo['ycen'])
        except:
            pass
            
    def run(self):
        try:            
            if self.numCatastro == None:
                self.coordsInfo = self.catastroService.getCoordsInfo(self.x,self.y)
                pc = self.coordsInfo['pc']
                self.numCatastro = pc['pc1'] + pc['pc2']            
            self.parcelaInfo = self.catastroService.getParcelaInfo(self.numCatastro,self.provincia,self.municipio)
            inmueblesService = InmueblesService(self.provincia,self.municipio)
            self.inmueblesList = inmueblesService.getInmueblesList(self.parcelaInfo)            
            if len(self.inmueblesList) == 0:
                self.procDone.emit(False)
            else:
                self.procDone.emit(True)                                 
        except Exception as ex:  
            self.procDone.emit(False)              
            
    def getDireccion(self):  
        inmueble=self.inmueblesList[0]
        if hasattr(inmueble, 'localizacionUrbana') and hasattr(inmueble.localizacionUrbana, 'direccion'):
            return unicode(inmueble.localizacionUrbana.direccion)
        else:            
            return unicode(inmueble.direccion)
    
    def getNumCatastro(self):        
        return self.numCatastro
    
    def getAntiguedad(self):
        antiguedad = 9999
        for item in self.inmueblesList:
            if int(float(item.antiguedad)) < antiguedad:
                antiguedad = int(float(item.antiguedad)) 
        return antiguedad
    
    def getSuperficie(self):
        superficie = 0
        for item in self.inmueblesList:
            superficie += float(item.superficie) 
        return superficie
    
    def isInmuebleUnico(self):
        return True if len(self.inmueblesList) == 1 else False
    
    def plantas(self):
        plantasBajo = 0
        plantasSobre = 0
        for inmueble in self.inmueblesList:
            if hasattr(inmueble, 'localizacionUrbana') and hasattr(inmueble.localizacionUrbana, 'localizacionInterna') \
            and hasattr(inmueble.localizacionUrbana.localizacionInterna,'planta') and inmueble.localizacionUrbana.localizacionInterna.planta.isdigit():
                if int(float(inmueble.localizacionUrbana.localizacionInterna.planta)) < plantasBajo:
                    plantasBajo = int(float(inmueble.localizacionUrbana.localizacionInterna.planta))
                if int(float(inmueble.localizacionUrbana.localizacionInterna.planta)) > plantasSobre:
                    plantasSobre = int(float(inmueble.localizacionUrbana.localizacionInterna.planta))
            if hasattr(inmueble, 'unidadesConstructivas'):
                for cons in inmueble.unidadesConstructivas:
                    if hasattr(cons, 'localizacionUrbana') and hasattr(cons.localizacionUrbana, 'localizacionInterna') \
                    and hasattr(cons.localizacionUrbana.localizacionInterna,'planta') and cons.localizacionUrbana.localizacionInterna.planta.isdigit():
                        if int(float(cons.localizacionUrbana.localizacionInterna.planta)) > plantasSobre:                        
                            plantasSobre = int(float(cons.localizacionUrbana.localizacionInterna.planta))
                        if int(float(cons.localizacionUrbana.localizacionInterna.planta)) < plantasBajo:
                            plantasBajo = int(float(cons.localizacionUrbana.localizacionInterna.planta))
        return { 'plantasBajo':abs(plantasBajo) ,'plantasSobre':plantasSobre + 1 }
    
    def plantaBajoViviendas(self):
        for inmueble in self.inmueblesList:
            if hasattr(inmueble, 'localizacionUrbana') and hasattr(inmueble.localizacionUrbana, 'localizacionInterna') \
            and hasattr(inmueble.localizacionUrbana.localizacionInterna,'planta') and \
            (inmueble.localizacionUrbana.localizacionInterna.planta.isdigit() and int(float(inmueble.localizacionUrbana.localizacionInterna.planta))==0 and hasattr(inmueble, 'uso') and inmueble.uso == 'Residencial') or \
            (inmueble.localizacionUrbana.localizacionInterna.planta=='OD' and hasattr(inmueble, 'uso') and inmueble.uso == 'Residencial'):                
                return True;
            if hasattr(inmueble, 'unidadesConstructivas'):
                for cons in inmueble.unidadesConstructivas:
                    if hasattr(cons, 'localizacionUrbana') and hasattr(cons.localizacionUrbana, 'localizacionInterna') \
                    and hasattr(cons.localizacionUrbana.localizacionInterna,'planta') and cons.localizacionUrbana.localizacionInterna.planta.isdigit() \
                    and int(float(cons.localizacionUrbana.localizacionInterna.planta))==0 and hasattr(cons, 'uso') and cons.uso == 'Residencial':
                        return True;        
        return False;
    
    def numeroInmuebles(self):
        return len(self.inmueblesList)
    
    def uso(self):
        usos=dict([])
        if len(self.inmueblesList) == 0:
            return ''
        for inmueble in self.inmueblesList:
            if not hasattr(inmueble, 'uso') and not hasattr(inmueble, 'superficie'):
                return ''
            elif inmueble.uso in usos:
                usos[inmueble.uso]+=float(inmueble.superficie)
            else:
                usos[inmueble.uso]=float(inmueble.superficie)
        return max(usos.iteritems(), key=operator.itemgetter(1))[0]
    