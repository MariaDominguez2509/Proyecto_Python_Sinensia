from Producto import Producto
from Empresa import Empresa
from abc import ABC, abstractmethod

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

    @abstractmethod
    def presentacion(self):
        pass

    @staticmethod
    def encontrar(dni): 
        a = {x[2]: x for x in Persona.registro}
        if dni in a: 
            print("El nombre de la persona con DNI", dni, "es", a[dni][0])
        else: 
            print("Persona no encontrada")

    @staticmethod
    def estatico(): 
        print("Prueba de método estático") 

class Cliente(Persona): 
    def __init__(self, nombre, DNI):
        super().__init__(nombre,DNI)
        Persona.registro.append((self.nombre, "Cliente", self.DNI))

    def compra(self, producto, empresa, empleado):
        if not isinstance(empresa, Empresa):
            print("No es una empresa")
            if not isinstance(producto, Producto):
                print(producto.nombre, "no es un producto")
        else:
            print(self.nombre, "ha comprado", producto.nombre, "de", empresa.nombre, "y se lo vendió", empleado.nombre)

    def presentacion(self):
        print("Soy", self.nombre, "y soy un Cliente")  

    @staticmethod
    def estatico():
        print("Funciona cuando lo cambio?")

class Empleado(Persona):
    def __init__(self, nombre, DNI): 
        super().__init__(nombre, DNI)
        Persona.registro.append((self.nombre, "Empleado", self.DNI))
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
    
    def presentacion(self):
        print("Soy", self.nombre, "y soy un Empleado")