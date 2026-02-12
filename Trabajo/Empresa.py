class Empresa: 
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.trabajadores = []
        Empresa.registro.append(self)

    def contrata(self, empleado):
        self.trabajadores.append(empleado)
        print("Ha contratado a", empleado.nombre)