class Empresa: 
    registro = []
    codigos = set() #para que no haya repetidos 
    def __init__(self, nombre, codigo):
        
        if codigo in Empresa.codigos:
            raise ValueError(f"El código {codigo} ya está registrado")
        else: 
            self.nombre = nombre
            self.codigo = codigo
            self.trabajadores = []
            Empresa.registro.append((self.nombre, self.codigo))
            Empresa.codigos.add(self.codigo)
            print("Empresa creada")

    def contrata(self, empleado):
        self.trabajadores.append((empleado.nombre, empleado.DNI))
        print(self.nombre, "ha contratado a", empleado.nombre)