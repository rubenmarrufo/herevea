import xmltodict
from Direccion import Direccion

class LocalizacionInterna:
    def __init__(self, loint):
        if(any("bq" in item for item in loint.keys())):
            self.bloque = loint['bq']
        if(any("es" in item for item in loint.keys())):
            self.escalera = loint['es']
        if(any("pt" in item for item in loint.keys())):
            self.planta = loint['pt']
        if(any("pu" in item for item in loint.keys())):
            self.puerta = loint['pu']
        