class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"

    def arrancar(self):
        print("El vehículo está arrancando.")
from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"{self.marca} {self.modelo} con {self.puertas} puertas"

    def arrancar(self):
        print("El coche está arrancando.")
from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def descripcion(self):
        return f"{self.marca} {self.modelo} de tipo {self.tipo}"

    def arrancar(self):
        print("La bicicleta no necesita arrancar.")
from coche import Coche
from bicicleta import Bicicleta

def main():
    mi_coche = Coche("Toyota", "Corolla", 4)
    print(mi_coche.descripcion())
    mi_coche.arrancar()

    mi_bicicleta = Bicicleta("Giant", "Escape 3", "urbana")
    print(mi_bicicleta.descripcion())
    mi_bicicleta.arrancar()

if __name__ == "__main__":
    main()


