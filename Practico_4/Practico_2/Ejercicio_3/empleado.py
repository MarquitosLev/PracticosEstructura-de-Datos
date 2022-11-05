from sys import int_info
from oficina import Oficina

class Empleado:

    def __init__(self, Legajo : int, Documento : int, Apellido : str, Nombre : str, Oficina : Oficina) -> None:
        self.Legajo = Legajo
        self.Documento = Documento
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Oficina = Oficina
    
    def __str__(self) -> str:
        return "\n  - Legajo: %s\n  - Documento: %s\n  - Apellido: %s\n  - Nombre: %s\n  - Oficina: %s" % (self.Legajo, self.Documento, self.Apellido, self.Nombre, self.Oficina)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro : object) -> bool:
        if self.Documento == otro.Documento:
            return True
        else:
            return False
    
    def __lt__(self, other : object):
        if self.Legajo > other.Legajo:
            return True
        else:
            return False
