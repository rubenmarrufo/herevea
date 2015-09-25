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
    
   def __repr__(self):
       repr=''
       if hasattr(self, 'tipoVia'):
           repr+=self.tipoVia + ' '
       if hasattr(self, 'nombreVia'):
           repr+=self.nombreVia + ' '
       if hasattr(self, 'numero'):
           repr+=self.numero + ' '
       if hasattr(self, 'letra'):
           repr+=self.letra + ' '
       if hasattr(self, 'segundoNumero') and self.segundoNumero != '0':
           repr+=self.segundoNumero + ' '
       if hasattr(self, 'segundaLetra'):
           repr+=self.segundaLetra + ' '
       if hasattr(self, 'kilometro'):
           repr+=self.kilometro + ' '
       if hasattr(self, 'direccionNoEstructurada'):
           repr+=self.direccionNoEstructurada + ' '
       return repr