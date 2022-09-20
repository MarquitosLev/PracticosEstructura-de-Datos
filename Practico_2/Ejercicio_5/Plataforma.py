class Plataforma:
    def __init__(self, nombre:str, es_portatil: bool) -> None:
        self.nombre = nombre
        self.es_portatil = es_portatil

    def __str__(self) -> str:
        return f"En {self.nombre}, es portatil? {self.es_portatil}"
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.es_portatil == otro.es_portatil
    
    def __repr__(self) -> str:
         return self.__str__()