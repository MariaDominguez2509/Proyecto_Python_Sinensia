lista = []
opciones = ["añadir", "eliminar", "actualizar"]

for i, a in enumerate(opciones): 
    print("Opción", i + 1, ":", a)

eleccion = int(input("Escoja una opcion: "))

if eleccion == 1:
    nuevo = input("Añadir: ")
    lista.append(nuevo)
    print("Elemento", nuevo, "añadido")
elif eleccion == 2:
    borra = input("Eliminar: ")
    if borra in a:
        lista.remove(borra)
        print("Elemento", borra, "borrado")
    else:
        print("Elemento no encontrado")
    
elif eleccion == 3:
    cambia = input("Elije el elemento que quiera cambiar: ")
    nuevo = input("Nuevo valor:")
    if cambia in a:
        lista[lista.index(cambia)] = nuevo
    else:
        print("Elemento no encontrado")
    
else:
    print("Opción no disponible")

print("Lista actual:", lista)