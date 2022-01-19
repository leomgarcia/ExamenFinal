import json
lista_coche = []
archivo = open('coches.txt','w')
while True:
    marca_coche = input("marca coche: ")
    archivo.write(marca_coche)
    archivo.write("\n")
    if marca_coche == "fin":
        break
    modelo = input("Modelo: ")
    archivo.write(modelo)
    archivo.write("\n")
    cambio = input("Cambio: ")
    archivo.write(cambio)
    archivo.write("\n")
    traccion = input("Traccion: ")
    archivo.write(traccion)
    archivo.write("\n")
    linea= {}
    linea["marca coche: "] = marca_coche
    linea["modelo: "] = modelo
    linea["cambio: "] = cambio
    linea["traccion: "] = traccion
    lista_coche.append(linea)
print("\tLista de coches:\n", lista_coche)
archivo.close()
with open('programacion.json','w') as f:
  json.dump(lista_coche,f,indent=4,sort_keys = True)