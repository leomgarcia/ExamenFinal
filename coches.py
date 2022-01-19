lista_coche = []

while True:
    marca_coche = input("Marca coche: ")
    if marca_coche == "fin":
        break
    modelo = input("Modelo: ")
    cambio = input("Cambio: ")
    traccion = input("Traccion: ")
    linea= {}
    linea["marca coche: "] = marca_coche
    linea["modelo: "] = modelo
    linea["cambio: "] = cambio
    linea["traccion: "] = traccion
    lista_coche.append(linea)
print("\tLista de coches:\n", lista_coche)

lista_coches = []