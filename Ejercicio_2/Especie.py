class Especie:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return "- Especie:", self.nombre 

    def __eq__(self, otro):
        return self.nombre == otro.nombre

    def __repr__(self) -> str:
        return "- Especie: %s" % (self.nombre)
