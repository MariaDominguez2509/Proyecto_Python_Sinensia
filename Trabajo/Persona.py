class Persona: 
    registro = []
    documentos = set()
    def __init__(self, nombre, DNI): 
        
        if DNI in Persona.documentos: 
            raise ValueError(f"El DNI {DNI} ya está registrado")
        else: 
            self.nombre = nombre
            self.DNI = DNI
            Persona.documentos.add(DNI)
            print("Persona creada")

class Cliente(Persona): 
    def __init__(self, nombre, DNI):
        super().__init__(nombre,DNI)
        Persona.registro.append((self.nombre, "Cliente"))

    def compra(self, objeto, empresa, empleado):
        if not insinstance(empresa, Empresa):
            print("No es una empresa")
        else:
            if empresa not in Empresa.registro: 
                print("Empresa no encontrada")
            else: 
                print("Ha comprado", objeto, "de", empresa.nombre, "y se lo vendió", empleado.nombre)

class Empleado(Persona):
    def __init__(self, nombre, DNI): 
        super().__init__(nombre, DNI)
        Persona.registro.append((self.nombre, "Empleado"))
    def vende(self, objeto, cliente): 
        print("Ha vendido", objeto, "a", cliente.nombre)

    def trabaja(self, empresa): 
        if not insinstance(empresa, Empresa):
            print("No es una empresa")
        else:
            if empresa not in Empresa.registro: 
                print("Empresa no encontrada")
            else: 
                print("Trabaja para", empresa.nombre)