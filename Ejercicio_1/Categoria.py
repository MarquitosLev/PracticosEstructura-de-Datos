class Categoria:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return "- Nombre de Categoria: %s"% self.nombre 

    def __eq__(self, otro):
        return self.nombre == otro.nombre
