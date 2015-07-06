import xmltodict
from LocalizacionInterna import LocalizacionInterna
from Direccion import Direccion

class LocalizacionUrbana:
    def __init__(self, lourb):
        if(any("dir" in item for item in lourb.keys())):
            self.direccion = Direccion(lourb['dir'])
        if(any("loint" in item for item in lourb.keys())):
            self.localizacionInterna = LocalizacionInterna(lourb['loint'])
        if(any("dp" in item for item in lourb.keys())):
            self.codigoPostal = lourb['dp']
        if(any("dm" in item for item in lourb.keys())):
            self.distritoMunicipal = lourb['dm']		