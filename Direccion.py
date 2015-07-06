import xmltodict

class Direccion:
   def __init__(self, direccionInfo):
       if(any("cv" in item for item in direccionInfo.keys())):
           self.codigoVia = direccionInfo['cv']
       if(any("tv" in item for item in direccionInfo.keys())):
           self.tipoVia = direccionInfo['tv']
       if(any("nv" in item for item in direccionInfo.keys())):
           self.nombreVia = direccionInfo['nv']
       if(any("pnp" in item for item in direccionInfo.keys())):
           self.numero = direccionInfo['pnp']
       if(any("plp" in item for item in direccionInfo.keys())):
           self.letra = direccionInfo['plp']
       if(any("snp" in item for item in direccionInfo.keys())):
           self.segundoNumero = direccionInfo['snp']
       if(any("slp" in item for item in direccionInfo.keys())):
           self.segundaLetra = direccionInfo['slp']
       if(any("km" in item for item in direccionInfo.keys())):
           self.kilometro = direccionInfo['km']
       if(any("td" in item for item in direccionInfo.keys())):
           self.direccionNoEstructurada = direccionInfo['td']