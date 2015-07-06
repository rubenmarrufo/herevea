import xmltodict
from CatastroService import CatastroService
from Inmueble import Inmueble
from collections import OrderedDict

class InmueblesService:
    
    def __init__(self):        
        self.catastroService = CatastroService()
        self.inmueblesList = []
            
    def getInmueblesList(self, parcelaInfo):                       
        if any("lrcdnp" in item for item in parcelaInfo.keys()):            
            self.manageInmueblesList(parcelaInfo)
        elif any("bico" in item for item in parcelaInfo.keys()):
            self.inmueblesList.append(Inmueble(parcelaInfo['bico']))
        return self.inmueblesList
    
    def manageInmueblesList(self, parcelaInfo):
        parcelaInfo = parcelaInfo['lrcdnp']
        inmuebles = parcelaInfo['rcdnp'] if type(parcelaInfo) == OrderedDict else [parcelaInfo['rcdnp']]
        for inmueble in inmuebles:            
            if any("rc" in item for item in inmueble.keys()):                    
                inmuebleRefCat = inmueble['rc']['pc1'] + inmueble['rc']['pc2']                
                if any("car" in item for item in inmueble['rc'].keys()):
                    inmuebleRefCat += inmueble['rc']['car']
                if any("cc1" in item for item in inmueble['rc'].keys()):
                    inmuebleRefCat += inmueble['rc']['cc1']
                if any("cc2" in item for item in inmueble['rc'].keys()):
                    inmuebleRefCat += inmueble['rc']['cc2']
                self.getInmueblesList(self.catastroService.getParcelaInfo(inmuebleRefCat))              