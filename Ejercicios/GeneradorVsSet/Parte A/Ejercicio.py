def generar_usuarios(n):
    # Produce: user001, user002, user003...
    for i in range(1, n + 1):
        yield f"user{i:03d}"


def buscar_con_generador(objetivo, n):
    for usuario in generar_usuarios(n):
        print("Revisando:", usuario)  # para ver el recorrido
        if usuario == objetivo:
            return True
    return False


objetivo = "user007"
esta = buscar_con_generador(objetivo, 10)
print("\n¿Encontrado?", esta)

objetivo1 = "user001"
esta = buscar_con_generador(objetivo1, 10)
print("\n¿Encontrado?", esta)

objetivo10 = "user010"
esta = buscar_con_generador(objetivo10, 10)
print("\n¿Encontrado?", esta)

#Imprime muchos revisando porque va uno a uno 
#hasta encontrar el objetivo

#Si el objetivo está al final pasará antes por todos y 
#tardará más