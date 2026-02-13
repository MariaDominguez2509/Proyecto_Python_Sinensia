from Producto import Producto
from Empresa import Empresa

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

    def compra(self, producto, empresa, empleado):
        if not isinstance(empresa, Empresa):
            print("No es una empresa")
            if not isinstance(producto, Producto):
                print(producto.nombre, "no es un producto")
        else:
            print(self.nombre, "ha comprado", producto.nombre, "de", empresa.nombre, "y se lo vendió", empleado.nombre)
        

class Empleado(Persona):
    def __init__(self, nombre, DNI): 
        super().__init__(nombre, DNI)
        Persona.registro.append((self.nombre, "Empleado"))
    def vende(self, producto, cliente): 
        if not isinstance(producto, Producto): 
            print(producto.nombre, "no es un producto")
        else:
            print(self.nombre, "ha vendido", producto.nombre, "a", cliente.nombre)
   

    def trabaja(self, empresa): 
        if not isinstance(empresa, Empresa):
            print("No es una empresa")
        else:
            print("Trabaja para", empresa.nombre)