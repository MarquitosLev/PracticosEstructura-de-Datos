from Autor import Autor
from Categoria import Categoria

class Libro:

    def __init__(self, num_invent:int, titulo:str, Autor:Autor, Categoria:Categoria, anio_publi: int):
        self.num_invent = num_invent
        self.titulo = titulo
        self.autor = Autor
        self.categoria = Categoria
        self.anio_publi = anio_publi

    #Retorna cadena con los atributos
    def __str__(self):
        return "\n- N° Inventario: %s\n- Título: %s\n- Autor: %s\n- Categoria: %s\n- Anio Publicación: %s\n" % (self.num_invent, self.titulo, self.autor, self.categoria, self.anio_publi)

    def __repr__(self) -> str:
        return self.__str__()

    #retorna si 2 objetos de la misma clase son iguales
    def __eq__(self, otro):
        if self.anio_publi == otro.anio_publi and self.titulo == otro.titulo and self.autor == otro.autor:
            return True
        else: return False
