import xmltodict
from CatastroService import CatastroService
from InmueblesService import InmueblesService

class ParcelaService:
    
    def __init__(self, x, y):
        catastroService = CatastroService()
        self.coordsInfo = catastroService.getCoordsInfo(x,y)
        self.parcelaInfo = catastroService.getParcelaInfo(self.getNumCatastro())
        inmueblesService = InmueblesService()
        self.inmueblesList = inmueblesService.getInmueblesList(self.parcelaInfo)
        print(self.inmueblesList)
              
    def getDireccion(self):  
        return self.coordsInfo['ldt']               
    
    def getNumCatastro(self):
        pc = self.coordsInfo['pc']
        return pc['pc1'] + pc['pc2']
    
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
            if hasattr(inmueble, 'unidadesConstructivas'):
                for cons in inmueble.unidadesConstructivas:
                    if hasattr(cons, 'localizacionUrbana') and hasattr(cons.localizacionUrbana, 'localizacionInterna') \
                    and hasattr(cons.localizacionUrbana.localizacionInterna,'planta') and cons.localizacionUrbana.localizacionInterna.planta == 0 \
                    and hasattr(cons, uso) and cons.uso != 'Residencial':
                        return False;
        return True;
    
    def numeroInmuebles(self):
        return self.inmueblesList.length
    
    def uso(self):
        return self.inmueblesList[0].uso