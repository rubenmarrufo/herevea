import xmltodict
from LocalizacionUrbana import LocalizacionUrbana

class Inmueble:
    def __init__(self, inmuebleInfo):
        if(any("bi" in item for item in inmuebleInfo.keys())):
            if(any("idbi" in item for item in inmuebleInfo['bi'].keys())): 
                self.setIdbi(inmuebleInfo['bi']['idbi'])
            if(any("dt" in item for item in inmuebleInfo['bi'].keys())): 
                self.setDt(inmuebleInfo['bi']['dt'])
            if(any("debi" in item for item in inmuebleInfo['bi'].keys())): 
                self.setDebi(inmuebleInfo['bi']['debi'])            
    
    def setIdbi(self, idbi):
        self.tipoInmueble = idbi['cn']
        if(any("rc" in item for item in idbi.keys())): 
            self.numCatastro = idbi['rc']['pc1'] + idbi['rc']['pc2']
            if(any("car" in item for item in idbi['rc'].keys())):
                self.numCatastro += idbi['rc']['car']
            if(any("cc1" in item for item in idbi['rc'].keys())):
                self.numCatastro += idbi['rc']['cc1']
            if(any("cc2" in item for item in idbi['rc'].keys())):
                self.numCatastro += idbi['rc']['cc2']
    
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
    
    def setDebi(self, debi):
        if(any("luso" in item for item in debi.keys())):
            self.uso = debi['luso']
        if(any("sfc" in item for item in debi.keys())):
            self.superficie = debi['sfc']
        if(any("cpt" in item for item in debi.keys())):
            self.coeficienteParticipacion = debi['cpt']
        if(any("ant" in item for item in debi.keys())):
            self.antiguedad = debi['ant']    