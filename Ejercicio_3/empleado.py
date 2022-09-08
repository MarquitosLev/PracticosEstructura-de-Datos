from oficina import Oficina

class Empleado:

    def __init__(self, Legajo : str, Documento : int, Apellido : str, Nombre : str, Oficina : Oficina) -> None:
        self.Legajo = Legajo
        self.Documento = Documento
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Oficina = Oficina
    
    def __str__(self) -> str:
        return "-Legajo: %s\n -Documento: %s\n -Apellido: %s\n -Nombre: %s\n -Oficina: %s" % (self.Legajo, self.Documento, self.Apellido, self.Nombre, self.Oficina)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro : object) -> bool:
        if self.Documento == otro.Documento:
            return True
        else:
            return False
