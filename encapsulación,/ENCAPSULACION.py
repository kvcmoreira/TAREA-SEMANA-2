class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:  # Validación básica
            self.__edad = edad
        else:
            raise ValueError("La edad debe ser positiva")

# Ejemplo de uso
persona = Persona("Juan", 30)
print(persona.get_nombre())  # Juan
persona.set_edad(31)
print(persona.get_edad())    # 31
