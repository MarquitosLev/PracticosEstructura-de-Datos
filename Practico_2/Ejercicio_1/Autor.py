class Autor:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self) -> str:
        return "- Nombre: %s\n \t - Apellido: %s" % (self.nombre, self.apellido)

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro):
        if isinstance(otro, Autor):
            return self.nombre == otro.nombre and self.apellido == otro.apellido
