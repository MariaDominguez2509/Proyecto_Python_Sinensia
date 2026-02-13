class Producto: 
    registro = []
    def __init__(self, nombre, ID): 
        self.nombre = nombre
        self.ID = ID
        Producto.registro.append((self.nombre, self.ID))
        print("Producto creado")

    def __eq__(self, prod):
        if isinstance(prod, type(self)): #solamente son iguales si coincide el ID 
            return self.ID == prod.ID
        else: 
            return NotImplemented