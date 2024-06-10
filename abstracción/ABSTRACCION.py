Abstraccion/
├── animal.py
├── perro.py
└── main.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

    def get_nombre(self):
        return self.nombre
from animal import Animal

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print(f"{self.nombre} hace: Guau Guau")
from perro import Perro

def main():
    mi_perro = Perro("Fido")
    print(f"El nombre de mi perro es: {mi_perro.get_nombre()}")
    mi_perro.hacer_sonido()

if __name__ == "__main__":
    main()
