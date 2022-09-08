from Especie import Especie
class Raza:

    def __init__(self, nombre:str, Especie:Especie):
        self.nombre = nombre
        self.especie = Especie

    def __str__(self):
        return "- Nombre: %s\n - Especie: %s"% (self.nombre, self.especie) 

    def __eq__(self, otro):
        if self.nombre == otro.nombre and self.especie == otro.especie:
            return True
        else : return False

    def __repr__(self):
        return self.__str__()