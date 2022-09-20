class Persona:
    
    def __init__(self, apellido, nombre, documento):
        self.apellido = apellido
        self.nombre = nombre
        self.documento = documento
        
    def __str__(self) -> str:
        return f"\n{self.apellido} {self.nombre} {self.documento}\n"
        
    def __eq__(self, otro):
        if self.apellido == otro.apellido and self.nombre == otro.nombre and self.documento == otro.documento:
            return True
        else: return False

    def __repr__(self) -> str:
        return self.__str__()