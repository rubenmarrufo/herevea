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
    
    def plantasBajoRasante(self):
        plantas = 0
        for inmueble in self.inmueblesList:
            if hasattr(inmueble, 'unidadesConstructivas'):
                for cons in inmueble.unidadesConstructivas:
                    if hasattr(cons, 'localizacionUrbana') and hasattr(cons.localizacionUrbana, 'localizacionInterna') \
                    and hasattr(cons.localizacionUrbana.localizacionInterna,'planta') and int(float(cons.localizacionUrbana.localizacionInterna.planta)) < 0:
                        plantas += 1
        return plantas
    
    def plantaBajoViviendas(self):
        for inmueble in self.inmueblesList:
            if hasattr(inmueble, 'unidadesConstructivas'):
                for cons in inmueble.unidadesConstructivas:
                    if hasattr(cons, 'localizacionUrbana') and hasattr(cons.localizacionUrbana, 'localizacionInterna') \
                    and hasattr(cons.localizacionUrbana.localizacionInterna,'planta') and cons.localizacionUrbana.localizacionInterna.planta == 0 \
                    and hasattr(cons, uso) and cons.uso != 'Residencial':
                        return False;
        return True;
    
    def uso(self):
        return self.inmueblesList[0].uso