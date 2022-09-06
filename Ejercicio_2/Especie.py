class Especie:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return "- Nombre de Especie: %s" % self.nombre 

    def __eq__(self, otro):
        return self.nombre == otro.nombre