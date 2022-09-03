class Categoria:
    # nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return "- Nombre de Categoria: %s"% self.nombre 

