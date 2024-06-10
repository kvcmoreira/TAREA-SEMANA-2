class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
from animal import Animal

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"
from animal import Animal

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau Miau"
from perro import Perro
from gato import Gato

def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

def main():
    mi_perro = Perro()
    mi_gato = Gato()

    hacer_sonido_animal(mi_perro)  # Guau Guau
    hacer_sonido_animal(mi_gato)   # Miau Miau

if __name__ == "__main__":
    main()
