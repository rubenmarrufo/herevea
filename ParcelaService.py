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
        self.provincia=provincia
        self.municipio=municipio  
        self.numCatastro=None     
          
    def initCoords(self, x, y):
        self.x=x
        self.y=y
        print x 
        
    def initRefCatastral(self, refCatastro):        
        self.numCatastro=refCatastro
                
    def run(self):
        try:
            print "running"
            catastroService = CatastroService()
            if self.numCatastro == None:
                self.coordsInfo = catastroService.getCoordsInfo(self.x,self.y)
                pc = self.coordsInfo['pc']
                self.numCatastro = pc['pc1'] + pc['pc2']
            self.parcelaInfo = catastroService.getParcelaInfo(self.numCatastro,self.provincia,self.municipio)
            inmueblesService = InmueblesService(self.provincia,self.municipio)
            self.inmueblesList = inmueblesService.getInmueblesList(self.parcelaInfo)
            print "running 2"
            if len(self.inmueblesList) == 0:
                self.procDone.emit(False)
            else:
                self.procDone.emit(True)                                 
        except Exception as ex:  
            print ex
            self.procDone.emit(False)              
            
    def getDireccion(self):  
        return self.inmueblesList[0].direccion
    
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
            and hasattr(inmueble.localizacionUrbana.localizacionInterna,'planta') and inmueble.localizacionUrbana.localizacionInterna.planta.isdigit() \
            and int(float(inmueble.localizacionUrbana.localizacionInterna.planta))==0 and hasattr(inmueble, 'uso') and inmueble.uso == 'Residencial':                
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
            if inmueble.uso in usos:
                usos[inmueble.uso]+=float(inmueble.superficie)
            else:
                usos[inmueble.uso]=float(inmueble.superficie)
        print usos
        return max(usos.iteritems(), key=operator.itemgetter(1))[0]
    