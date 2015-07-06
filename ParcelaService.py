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
     