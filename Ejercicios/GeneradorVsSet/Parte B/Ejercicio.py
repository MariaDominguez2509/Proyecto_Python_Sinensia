def generar_usuarios(n):
    for i in range(1, n + 1):
        yield f"user{i:03d}"


def construir_set(n):
    base = set(generar_usuarios(n))
    return base


base = construir_set(10)
print("Base cargada:", base)

objetivo = "user007"
print("\n¿Encontrado?", objetivo in base)

#En este caso no recorre la lista, solo busca dónde
#está el objeto (usuario) indicado 

#Esta es la mejor opción si hay que hacer muchas búquedas
#Incluso si solo hubiera que hacer una, es más rapido y no 
#habría que recorrer la lista. 