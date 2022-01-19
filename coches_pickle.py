class Car:
    num_cars = 0

    def __init__(self, marca, modelo, cambio, traccion):
        self.marca = marca
        self.modelo = modelo
        self.cambio = cambio
        self.traccion = traccion
archivo = open('coches.txt','w')
archivo.write(self.marca)
archivo.write('\n')
archivo.write(self.modelo)
archivo.write('\n')
archivo.write(self.cambio)
archivo.write('\n')
archivo.write(self.traccion)
archivo.write('\n')
archivo.close()