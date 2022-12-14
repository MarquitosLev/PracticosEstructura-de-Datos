class Empresa:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
    
    def __str__(self) -> str:
        return self.nombre
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre

    def __repr__(self) -> str:
         return self.__str__()