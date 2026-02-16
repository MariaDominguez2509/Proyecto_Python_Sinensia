from Empresa import Empresa

class Lugar: 
    codigos = set()
    def __init__(self, nombre, cod_postal, empresas): 
        self.nombre = nombre
        self.cod_postal = cod_postal
        self.empresas = empresas #las empresas que estén en dicho lugar 
        Lugar.codigos.add(self.cod_postal)

    def empresa_nueva(self, empresa): 
        if isinstance(empresa, Empresa): 
            self.empresas.append(empresa.nombre)
        else: 
            print("No es una empresa")