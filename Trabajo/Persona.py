class Persona: 
    def __init__(self, nombre, DNI, correo): 
        self.nombre = nombre
        self.DNI = DNI
        self.correo = correo

class Cliente(Persona): 
    def compra(self, objeto, empresa, empleado):
        if not insinstance(empresa, Empresa):
            print("No es una empresa")
        else:
            if empresa not in Empresa.registro: 
                print("Empresa no encontrada")
            else: 
                print("Ha comprado", objeto, "de", empresa.nombre, "y se lo vendió", empleado.nombre)

class Empleado(Persona):
    def vende(self, objeto, cliente): 
        print("Ha vendido", objeto, "a", cliente.nombre)

    def trabaja(self, empresa): 
        print("Trabaja para", empresa.nombre)