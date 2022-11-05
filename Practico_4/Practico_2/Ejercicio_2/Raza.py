from Especie import Especie
class Raza:

    def __init__(self, nombre:str, especie:Especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self) -> str:
        return f"{self.nombre} {self.especie.nombre}"

    def __eq__(self, otro):
        if self.nombre == otro.nombre and self.especie == otro.especie:
            return True
        else : return False

    def __repr__(self):
        return self.__str__()