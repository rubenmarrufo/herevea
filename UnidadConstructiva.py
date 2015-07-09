import xmltodict
from LocalizacionUrbana import LocalizacionUrbana

class UnidadConstructiva:
    def __init__(self, cons):
        if any("lcd" in item for item in cons.keys()):
            self.uso = cons['lcd']
        if(any("dt" in item for item in cons.keys())): 
            self.setDt(cons['dt'])
        if(any("dfcons" in item for item in cons.keys())):
            if(any("stl" in item for item in cons['dfcons'].keys())):
                self.superficie = cons['dfcons']['stl']
    
    def setDt(self, dt):
        if(any("np" in item for item in dt.keys())):
            self.provincia = dt['np']
        if(any("nm" in item for item in dt.keys())):
            self.municipio = dt['nm'] 
        if(any("nem" in item for item in dt.keys())):
            self.entidadMenor = dt['nem']
        if(any("locs" in item for item in dt.keys())):
            if(any("lous" in item for item in dt['locs'].keys())):
                if(any("lourb" in item for item in dt['locs']['lous'].keys())):
                    self.localizacionUrbana = LocalizacionUrbana(dt['locs']['lous']['lourb'])
    