class Categoria:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return self.nombre 

    def __repr__(self) -> str:
        return self.__str__()
        
    def __eq__(self, otro):
        if isinstance(otro, Categoria):
            return self.nombre == otro.nombre
