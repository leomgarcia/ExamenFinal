def bubble_sort(lista):
  for n in range(len(lista-1,0,-1)):
    for i in range(n):
      if lista[i]>lista[i+1]:
        temp = lista[i]
        lista[i] = lista[i+1]
        lista[i+1] = temp

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